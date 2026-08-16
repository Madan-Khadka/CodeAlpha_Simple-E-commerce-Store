// ========== NAVBAR TOGGLE ==========
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // Animate hamburger
            const bars = this.querySelectorAll('.bar');
            bars.forEach((bar, index) => {
                bar.style.transition = 'all 0.3s ease';
            });
            
            if (navMenu.classList.contains('active')) {
                bars[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                bars[1].style.opacity = '0';
                bars[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
            } else {
                bars[0].style.transform = 'rotate(0) translate(0, 0)';
                bars[1].style.opacity = '1';
                bars[2].style.transform = 'rotate(0) translate(0, 0)';
            }
        });
    }

    // ========== AUTO DISMISS MESSAGES ==========
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'all 0.5s ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(100px)';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });

    // ========== QUANTITY CONTROLS ==========
    const quantityBtns = document.querySelectorAll('.quantity-btn');
    quantityBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const input = this.closest('.quantity-control').querySelector('.quantity-input');
            const currentValue = parseInt(input.value) || 0;
            const maxStock = parseInt(input.getAttribute('max')) || 999;
            
            if (this.dataset.action === 'increase') {
                if (currentValue < maxStock) {
                    input.value = currentValue + 1;
                    submitQuantityChange(input);
                } else {
                    showNotification('Maximum quantity reached', 'warning');
                }
            } else if (this.dataset.action === 'decrease') {
                if (currentValue > 1) {
                    input.value = currentValue - 1;
                    submitQuantityChange(input);
                } else {
                    if (confirm('Remove this item from cart?')) {
                        const form = this.closest('form');
                        if (form) {
                            const removeInput = document.createElement('input');
                            removeInput.type = 'hidden';
                            removeInput.name = 'remove';
                            removeInput.value = 'true';
                            form.appendChild(removeInput);
                            form.submit();
                        }
                    }
                }
            }
        });
    });

    // ========== QUANTITY INPUT CHANGE ==========
    const quantityInputs = document.querySelectorAll('.quantity-input');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            const value = parseInt(this.value) || 0;
            const maxStock = parseInt(this.getAttribute('max')) || 999;
            
            if (value < 1) {
                this.value = 1;
                showNotification('Minimum quantity is 1', 'warning');
            } else if (value > maxStock) {
                this.value = maxStock;
                showNotification('Only ' + maxStock + ' items available', 'warning');
            }
            
            if (value !== parseInt(this.value)) {
                submitQuantityChange(this);
            }
        });
    });

    function submitQuantityChange(input) {
        const form = input.closest('form');
        if (form) {
            // Set the quantity in the form
            const hiddenInput = form.querySelector('input[name="quantity"]');
            if (hiddenInput) {
                hiddenInput.value = input.value;
            }
            form.submit();
        }
    }

    // ========== ADD TO CART ANIMATION ==========
    const addToCartBtns = document.querySelectorAll('.btn-cart, .add-to-cart-btn');
    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            // Show loading state
            const originalText = this.innerHTML;
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Adding...';
            this.disabled = true;
            
            setTimeout(() => {
                this.innerHTML = originalText;
                this.disabled = false;
            }, 1000);
        });
    });

    // ========== REMOVE ITEM CONFIRMATION ==========
    const removeBtns = document.querySelectorAll('.remove-btn, .delete-btn');
    removeBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to remove this item?')) {
                e.preventDefault();
            }
        });
    });

    // ========== CART ITEM COUNT UPDATE ==========
    function updateCartCount(count) {
        const badge = document.querySelector('.cart-badge');
        if (badge) {
            badge.textContent = count;
            if (count > 0) {
                badge.style.display = 'inline-block';
            } else {
                badge.style.display = 'none';
            }
        }
    }

    // ========== SEARCH FUNCTIONALITY ==========
    const searchForm = document.querySelector('.search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const input = this.querySelector('input[type="search"]');
            if (input && input.value.trim() === '') {
                e.preventDefault();
                showNotification('Please enter a search term', 'warning');
            }
        });
    }

    // ========== NOTIFICATION SYSTEM ==========
    function showNotification(message, type = 'info') {
        const container = document.querySelector('.messages-container') || createMessageContainer();
        const alert = document.createElement('div');
        alert.className = `alert alert-${type}`;
        alert.innerHTML = `
            <span class="alert-icon">
                <i class="fas ${getIconForType(type)}"></i>
            </span>
            <span class="alert-message">${message}</span>
            <button class="alert-close" onclick="this.parentElement.remove()">
                <i class="fas fa-times"></i>
            </button>
        `;
        container.appendChild(alert);
        
        // Auto dismiss
        setTimeout(() => {
            alert.style.transition = 'all 0.5s ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(100px)';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    }

    function createMessageContainer() {
        const container = document.createElement('div');
        container.className = 'messages-container';
        document.body.insertBefore(container, document.querySelector('main'));
        return container;
    }

    function getIconForType(type) {
        const icons = {
            success: 'fa-check-circle',
            error: 'fa-exclamation-circle',
            danger: 'fa-exclamation-circle',
            warning: 'fa-exclamation-triangle',
            info: 'fa-info-circle'
        };
        return icons[type] || icons.info;
    }

    // ========== PRODUCT FILTER ==========
    const filterForm = document.querySelector('.filter-form');
    if (filterForm) {
        filterForm.addEventListener('change', function() {
            this.submit();
        });
    }

    // ========== SCROLL TO TOP ==========
    // Create scroll to top button
    const scrollBtn = document.createElement('button');
    scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollBtn.className = 'scroll-top-btn';
    scrollBtn.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        font-size: 1.2rem;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        opacity: 0;
        transform: translateY(20px);
        pointer-events: none;
        z-index: 999;
    `;
    document.body.appendChild(scrollBtn);

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            scrollBtn.style.opacity = '1';
            scrollBtn.style.transform = 'translateY(0)';
            scrollBtn.style.pointerEvents = 'auto';
        } else {
            scrollBtn.style.opacity = '0';
            scrollBtn.style.transform = 'translateY(20px)';
            scrollBtn.style.pointerEvents = 'none';
        }
    });

    scrollBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // ========== IMAGE LOADING ==========
    const productImages = document.querySelectorAll('.product-image img');
    productImages.forEach(img => {
        img.addEventListener('error', function() {
            this.style.display = 'none';
            const parent = this.closest('.product-image');
            if (parent) {
                const noImage = document.createElement('div');
                noImage.className = 'no-image';
                noImage.innerHTML = `
                    <i class="fas fa-image"></i>
                    <span>No Image</span>
                `;
                parent.appendChild(noImage);
            }
        });
    });

    console.log('Mohan Store - E-commerce Website Loaded Successfully!');
});