from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Category, Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')
        
        # Create categories
        categories_data = [
            {'name': 'Electronics', 'description': 'Latest electronic gadgets and devices'},
            {'name': 'Fashion', 'description': 'Trendy clothing and accessories'},
            {'name': 'Shoes', 'description': 'Comfortable and stylish footwear'},
            {'name': 'Books', 'description': 'Books for knowledge and entertainment'},
            {'name': 'Accessories', 'description': 'Accessories to complete your look'},
            {'name': 'Home & Living', 'description': 'Products for your home and lifestyle'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create products
        products_data = [
            {
                'name': 'Wireless Bluetooth Headphones',
                'category': 'Electronics',
                'description': 'High-quality wireless headphones with noise cancellation and 24-hour battery life. Perfect for music lovers and professionals.',
                'price': 2999,
                'stock': 50,
                'is_active': True,
            },
            {
                'name': 'Smartphone Pro Max',
                'category': 'Electronics',
                'description': 'Latest generation smartphone with 6.7-inch display, 108MP camera, and 5000mAh battery. Available in multiple colors.',
                'price': 59999,
                'stock': 25,
                'is_active': True,
            },
            {
                'name': 'Running Shoes',
                'category': 'Shoes',
                'description': 'Lightweight running shoes with cushioning technology. Designed for comfort and performance during your runs.',
                'price': 2499,
                'stock': 100,
                'is_active': True,
            },
            {
                'name': 'Fashion Backpack',
                'category': 'Fashion',
                'description': 'Stylish and durable backpack for everyday use. Multiple compartments and water-resistant material.',
                'price': 1499,
                'stock': 75,
                'is_active': True,
            },
            {
                'name': 'Python Programming Book',
                'category': 'Books',
                'description': 'Comprehensive guide to Python programming. Covers basics to advanced concepts with practical examples.',
                'price': 799,
                'stock': 150,
                'is_active': True,
            },
            {
                'name': 'Smart Watch',
                'category': 'Electronics',
                'description': 'Fitness tracker with heart rate monitor, GPS, and smartphone notifications. Available in multiple colors.',
                'price': 8999,
                'stock': 40,
                'is_active': True,
            },
            {
                'name': 'Leather Wallet',
                'category': 'Accessories',
                'description': 'Genuine leather wallet with multiple card slots and coin compartment. Compact and durable design.',
                'price': 999,
                'stock': 200,
                'is_active': True,
            },
            {
                'name': 'Home Decor Set',
                'category': 'Home & Living',
                'description': 'Elegant home decor set including vases, candles, and decorative pieces. Perfect for modern homes.',
                'price': 3499,
                'stock': 30,
                'is_active': True,
            },
            {
                'name': 'Casual T-Shirt',
                'category': 'Fashion',
                'description': 'Premium cotton t-shirt available in multiple colors. Comfortable fit for everyday wear.',
                'price': 599,
                'stock': 120,
                'is_active': True,
            },
            {
                'name': 'Wireless Earbuds',
                'category': 'Electronics',
                'description': 'True wireless earbuds with noise isolation and long battery life. Compact charging case included.',
                'price': 1999,
                'stock': 60,
                'is_active': True,
            },
        ]
        
        for product_data in products_data:
            category = categories.get(product_data['category'])
            if category:
                product, created = Product.objects.get_or_create(
                    name=product_data['name'],
                    category=category,
                    defaults={
                        'description': product_data['description'],
                        'price': Decimal(str(product_data['price'])),
                        'stock': product_data['stock'],
                        'is_active': product_data['is_active'],
                    }
                )
                if created:
                    self.stdout.write(f'Created product: {product.name}')
        
        # Create admin user if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Created admin user: admin / admin123')
        
        self.stdout.write(self.style.SUCCESS('Sample data loaded successfully!'))