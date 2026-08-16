from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.db.models import Q, Sum
from django.core.paginator import Paginator
from decimal import Decimal
import json

from .models import (
    Category, Product, Cart, CartItem, 
    Order, OrderItem
)
from .forms import (
    UserRegistrationForm, UserLoginForm, 
    UserProfileForm, CheckoutForm
)

# ============= HOME PAGE =============
def home(request):
    """Home page view"""
    categories = Category.objects.all()
    featured_products = Product.objects.filter(
        is_active=True
    ).order_by('-created_at')[:8]  # Latest 8 products
    
    context = {
        'categories': categories,
        'featured_products': featured_products,
    }
    return render(request, 'home.html', context)

# ============= PRODUCT VIEWS =============
def product_list(request):
    """Display all products with pagination"""
    products = Product.objects.filter(is_active=True)
    
    # Get category filter
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Get search query
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )
    
    # Pagination (6 products per page)
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'products': products_page,
        'categories': categories,
        'search_query': search_query,
        'category_slug': category_slug,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, slug):
    """Display product details"""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'products/product_detail.html', context)

def category_products(request, slug):
    """Display products by category"""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_active=True)
    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'products/category_products.html', context)

def search_products(request):
    """Search products"""
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query),
            is_active=True
        )
    else:
        products = Product.objects.none()
    
    context = {
        'products': products,
        'query': query,
        'count': products.count(),
    }
    return render(request, 'products/search_results.html', context)

# ============= AUTHENTICATION VIEWS =============
def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('store:home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Mohan Store.')
            return redirect('store:home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('store:home')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                
                # Redirect to previous page or home
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('store:home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def user_logout(request):
    """User logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('store:home')

@login_required
def profile(request):
    """User profile view"""
    user = request.user
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('store:profile')
    else:
        form = UserProfileForm(instance=user)
    
    # Get user's orders
    orders = Order.objects.filter(user=user).order_by('-created_at')[:5]
    
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, 'accounts/profile.html', context)

# ============= CART VIEWS =============
@login_required
def view_cart(request):
    """View shopping cart"""
    cart = Cart.objects.filter(user=request.user).first()
    
    if not cart:
        cart = Cart.objects.create(user=request.user)
    
    context = {
        'cart': cart,
        'total_items': cart.total_items(),
        'subtotal': cart.subtotal(),
    }
    return render(request, 'cart/cart.html', context)

@login_required
def add_to_cart(request, product_id):
    """Add product to cart"""
    product = get_object_or_404(Product, id=product_id, is_active=True)
    
    # Check stock
    if product.stock <= 0:
        messages.error(request, f'Sorry, {product.name} is out of stock.')
        return redirect('store:product_detail', slug=product.slug)
    
    # Get or create cart
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Get or create cart item
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        # Check if adding more exceeds stock
        if cart_item.quantity + 1 > product.stock:
            messages.error(request, f'Cannot add more. Only {product.stock} items available.')
            return redirect('store:view_cart')
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'Increased {product.name} quantity in cart.')
    else:
        messages.success(request, f'{product.name} added to cart!')
    
    return redirect('store:view_cart')

@login_required
def update_cart_item(request, item_id):
    """Update cart item quantity"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        
        if quantity <= 0:
            cart_item.delete()
            messages.info(request, 'Item removed from cart.')
        elif quantity > cart_item.product.stock:
            messages.error(request, f'Only {cart_item.product.stock} items available.')
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated successfully.')
    
    return redirect('store:view_cart')

@login_required
def remove_from_cart(request, item_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.info(request, f'{product_name} removed from cart.')
    return redirect('store:view_cart')

@login_required
def clear_cart(request):
    """Clear entire cart"""
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart.items.all().delete()
        messages.info(request, 'Cart cleared.')
    return redirect('store:view_cart')

# ============= ORDER VIEWS =============
@login_required
def checkout(request):
    """Checkout view"""
    cart = Cart.objects.filter(user=request.user).first()
    
    if not cart or cart.items.count() == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('store:view_cart')
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Check stock for all items
                    for item in cart.items.all():
                        if item.quantity > item.product.stock:
                            messages.error(
                                request, 
                                f'Sorry, only {item.product.stock} units of {item.product.name} available.'
                            )
                            return redirect('store:view_cart')
                    
                    # Create order
                    order = Order.objects.create(
                        user=request.user,
                        full_name=form.cleaned_data['full_name'],
                        email=form.cleaned_data['email'],
                        phone=form.cleaned_data['phone'],
                        address=form.cleaned_data['address'],
                        city=form.cleaned_data['city'],
                        total_amount=cart.subtotal(),
                        payment_method='cod',
                        notes=form.cleaned_data.get('notes', '')
                    )
                    
                    # Create order items and update stock
                    for cart_item in cart.items.all():
                        OrderItem.objects.create(
                            order=order,
                            product=cart_item.product,
                            product_name=cart_item.product.name,
                            price=cart_item.product.price,
                            quantity=cart_item.quantity,
                            subtotal=cart_item.subtotal()
                        )
                        
                        # Reduce stock
                        cart_item.product.stock -= cart_item.quantity
                        cart_item.product.save()
                    
                    # Clear cart
                    cart.items.all().delete()
                    
                    messages.success(request, f'Order #{order.order_number} placed successfully!')
                    return redirect('store:order_success', order_id=order.id)
                    
            except Exception as e:
                messages.error(request, f'Error placing order: {str(e)}')
                return redirect('store:view_cart')
    else:
        # Pre-fill form with user data
        initial_data = {
            'full_name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
        }
        form = CheckoutForm(initial=initial_data)
    
    context = {
        'cart': cart,
        'form': form,
        'total': cart.subtotal(),
        'total_items': cart.total_items(),
    }
    return render(request, 'orders/checkout.html', context)

@login_required
def order_success(request, order_id):
    """Order success page"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})

@login_required
def order_list(request):
    """List user's orders"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'orders': orders,
        'count': orders.count(),
    }
    return render(request, 'orders/order_list.html', context)

@login_required
def order_detail(request, order_id):
    """Order detail view"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
        'items': order.items.all(),
        'status_badge': get_status_badge(order.status),
    }
    return render(request, 'orders/order_detail.html', context)

def get_status_badge(status):
    """Helper function to get status badge class"""
    status_map = {
        'pending': 'warning',
        'processing': 'info',
        'shipped': 'primary',
        'delivered': 'success',
        'cancelled': 'danger',
    }
    return status_map.get(status, 'secondary')