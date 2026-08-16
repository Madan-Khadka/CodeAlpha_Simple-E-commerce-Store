# CodeAlpha_Simple-E-commerce-Store
# Simple E-commerce Store

> A professional full-stack e-commerce web application built with Django, Python, HTML, CSS, and JavaScript.

---

## Internship Task

**Program:** Full Stack Development Tasks & Instructions — CodeAlpha
**Organization:** CodeAlpha
**Task:** Task 1 – Simple E-commerce Store
**Language:** Python
**Backend:** Django
**Frontend:** HTML, CSS, JavaScript
**Database:** SQLite
**Project Type:** Full-Stack E-commerce Web Application

---

## Project Overview

**Simple E-commerce Store** is a professional full-stack online shopping web application developed using **Django and Python**.

The project provides a complete basic e-commerce workflow where users can create an account, log in, browse products, search and filter products, view product details, manage their shopping cart, checkout, place orders, and track their order status.

The application also includes a **Django Admin Panel** where administrators can manage products, categories, users, stock, and customer orders.

The main purpose of this project is to demonstrate practical knowledge of **full-stack web development, Django, database management, authentication, shopping cart functionality, order processing, and responsive frontend design**.

---

## Core Features

### User Features

* User registration
* User login
* User logout
* User authentication
* User profile
* Product listing
* Product details
* Product search
* Category filtering
* Add to cart
* Increase/decrease quantity
* Update cart quantity
* Remove cart items
* Cart total calculation
* Checkout
* Customer information
* Cash on Delivery
* Place order
* Order confirmation
* My Orders
* Order details
* Order status tracking

### Admin Features

* Django Admin Panel
* Product management
* Category management
* User management
* Customer information
* Stock management
* Order management
* Order details
* Order status management
* Product availability management
* Search and filtering

---

## User Authentication

The application uses **Django's built-in authentication system**.

Users can:

* Create a new account
* Log in securely
* Log out
* Access their profile
* View their orders
* Track order status

Checkout and order-related pages are protected so that users must be authenticated before placing an order.

Each order is connected to the user who placed it, allowing users to access their own order history.

---

## Product System

The store contains a complete product management system.

Each product can contain:

* Product name
* Product image
* Category
* Description
* Price
* Stock
* Availability
* Created date
* Updated date

Products can be managed from the Django Admin Panel.

Administrators can:

* Add products
* Edit products
* Delete products
* Update product prices
* Update stock
* Change availability
* Assign categories

---

## Product Categories

Products are organized into categories for easier browsing and filtering.

Example categories:

```text
Electronics
Fashion
Shoes
Books
Accessories
Home & Living
```

Categories are stored in the database and can be managed through Django Admin.

---

## Search and Category Filter

Users can search products using keywords.

Example:

```text
phone
shoes
watch
headphones
book
```

The application displays matching products.

Users can also filter products by category.

```text
All Products
Electronics
Fashion
Shoes
Books
Accessories
```

If no matching products are found, the application displays a user-friendly message.

---

## Product Details

Every product has a dedicated details page.

The product details page displays:

* Product image
* Product name
* Category
* Price
* Description
* Available stock
* Quantity selector
* Add to Cart button

Users can view complete information before adding a product to their cart.

---

## Shopping Cart

The shopping cart allows users to manage products before checkout.

Users can:

* Add products to cart
* Increase quantity
* Decrease quantity
* Update quantity
* Remove products
* View subtotal
* View total price
* Continue shopping
* Proceed to checkout

The cart is connected to the authenticated user.

Users cannot access another user's cart.

---

## Cart Validation

The application validates cart operations on the server.

It prevents:

* Negative quantities
* Invalid quantities
* Zero quantities
* Ordering more products than available stock
* Invalid product references
* Unauthorized cart access

This helps maintain correct inventory and prevents invalid orders.

---

## Checkout

Authenticated users can proceed to checkout.

The checkout page contains:

### Customer Information

* Full name
* Email
* Phone
* Address
* City

### Order Information

* Product
* Quantity
* Price
* Subtotal
* Total amount

### Payment Method

```text
Cash on Delivery
```

The project does not require a real payment gateway because this is a basic internship e-commerce project.

---

## Order Processing

When a user places an order, the application follows this process:

```text
User Login
     ↓
Browse Products
     ↓
Add Products to Cart
     ↓
Update Cart
     ↓
Checkout
     ↓
Validate Stock
     ↓
Create Order
     ↓
Create Order Items
     ↓
Reduce Product Stock
     ↓
Clear Cart
     ↓
Generate Order Number
     ↓
Show Order Confirmation
```

The order is stored in the database and connected to the authenticated user.

---

## Order Management

Every order contains important information such as:

* Order number
* User
* Customer name
* Email
* Phone
* Address
* City
* Products
* Quantity
* Price
* Total amount
* Payment method
* Order status
* Created date
* Updated date

---

## Order Status

Orders can have the following statuses:

```text
Pending
Processing
Shipped
Delivered
Cancelled
```

The default status is:

```text
Pending
```

Administrators can update the status from Django Admin.

Users can see the latest order status from their **My Orders** page.

---

## My Orders

Logged-in users can access their previous orders through:

```text
My Orders
```

The page displays:

* Order number
* Order date
* Total amount
* Status
* View Details button

Users can open an order to view its complete details.

A user can only access their own orders.

---

## Order Details

The order details page contains:

### Customer Details

* Full name
* Email
* Phone
* Address
* City

### Order Details

* Order number
* Order date
* Products
* Quantity
* Price
* Subtotal
* Total
* Payment method
* Order status

---

## Stock Management

The application includes basic inventory management.

Example:

```text
Initial Stock: 10
Ordered Quantity: 2
Remaining Stock: 8
```

When an order is successfully placed, the product stock is automatically reduced.

If stock reaches zero, the product becomes unavailable.

The administrator can update product stock from Django Admin.

---

## Django Admin Panel

The project uses Django's built-in Admin Panel for store management.

### Product Management

Administrators can:

* Add products
* Edit products
* Delete products
* Update prices
* Update stock
* Manage availability

### Category Management

Administrators can:

* Add categories
* Edit categories
* Delete categories

### User Management

Administrators can:

* View registered users
* Manage user accounts

### Order Management

Administrators can:

* View customer orders
* View customer details
* View ordered products
* View quantities
* View total amount
* Update order status
* Search orders
* Filter orders

---

## Admin Order Workflow

```text
Customer
    ↓
Creates Account
    ↓
Logs In
    ↓
Places Order
    ↓
Order Saved in Database
    ↓
Admin Views Order
    ↓
Admin Checks Customer Details
    ↓
Admin Processes Order
    ↓
Processing
    ↓
Shipped
    ↓
Delivered
```

The updated status is visible to the customer from their account.

---

## Database Design

The project uses **SQLite** as the development database.

Main database entities:

```text
User
Category
Product
Cart
CartItem
Order
OrderItem
```

### Relationship

```text
User
 |
 +------ Cart
 |        |
 |        +------ CartItem ------ Product
 |
 +------ Order
          |
          +------ OrderItem ------ Product

Category
 |
 +------ Product
```

---

## Order Price Snapshot

The order system stores the product price at the time the order is placed.

For example:

```text
Product Current Price: Rs. 5,000
Order Price:           Rs. 4,500
```

Even if the product price later changes to Rs. 5,000, the previous order continues to display:

```text
Rs. 4,500
```

This keeps historical order information accurate.

---

## Frontend

The frontend is developed using:

* HTML5
* CSS3
* JavaScript

The interface is designed to be:

* Modern
* Clean
* Responsive
* User friendly
* Mobile friendly
* Tablet friendly
* Desktop friendly

The UI includes:

* Responsive navbar
* Product cards
* Search bar
* Category filter
* Buttons
* Forms
* Shopping cart
* Checkout page
* Order pages
* User profile
* Footer

---

## JavaScript Features

JavaScript is used to improve frontend interaction.

It can handle:

* Mobile navigation
* Quantity controls
* Cart interactions
* Confirmation dialogs
* Form interactions
* Dynamic UI feedback
* User-friendly messages

Important business logic is validated by Django on the backend.

---

## Responsive Design

The application is designed to work on:

```text
Desktop
   ↓
Tablet
   ↓
Mobile
```

Product cards, navigation, forms, cart, checkout, and other components adapt to different screen sizes.

---

## Security

The project follows important Django security practices.

Implemented security concepts include:

* CSRF protection
* Django authentication
* Password hashing
* Login protection
* Authorization
* Server-side validation
* User ownership validation
* Protected checkout
* Protected order details
* Secure POST requests

Users cannot access another user's orders by simply changing an order ID in the URL.

---

## Project Architecture

```text
                    SIMPLE E-COMMERCE STORE
                              |
             +----------------+----------------+
             |                                 |
          FRONTEND                          BACKEND
             |                                 |
      HTML + CSS + JS                       Django
             |                                 |
             |                    +------------+------------+
             |                    |                         |
             |                Authentication            Database
             |                    |                         |
             |                 Users                     Products
             |                                           Cart
             |                                           Orders
             |                                             |
             +---------------------------------------------+
                                                           |
                                                   Django Admin
                                                           |
                                                   Store Management
```

---

## Project Structure

```text
simple_ecommerce/
│
├── manage.py
│
├── ecommerce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   └── utils.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   │
│   ├── accounts/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   │
│   ├── products/
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   └── category.html
│   │
│   ├── cart/
│   │   └── cart.html
│   │
│   └── orders/
│       ├── checkout.html
│       ├── order_success.html
│       ├── order_list.html
│       └── order_detail.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── media/
│   └── products/
│
├── db.sqlite3
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Important Files

| File               | Purpose                    |
| ------------------ | -------------------------- |
| `manage.py`        | Django project management  |
| `settings.py`      | Project configuration      |
| `urls.py`          | URL routing                |
| `models.py`        | Database models            |
| `views.py`         | Application logic          |
| `forms.py`         | Forms and validation       |
| `admin.py`         | Django Admin configuration |
| `templates/`       | HTML pages                 |
| `static/css/`      | CSS styling                |
| `static/js/`       | JavaScript                 |
| `media/`           | Uploaded product images    |
| `tests.py`         | Application tests          |
| `requirements.txt` | Python dependencies        |
| `README.md`        | Project documentation      |

---

## Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Backend programming  |
| Django       | Web framework        |
| SQLite       | Database             |
| HTML5        | Page structure       |
| CSS3         | Styling              |
| JavaScript   | Frontend interaction |
| Django Admin | Administration       |
| Git          | Version control      |
| GitHub       | Repository hosting   |

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd simple_ecommerce
```

### 2. Create Virtual Environment

Linux/macOS:

```bash
python3 -m venv venv
```

Windows:

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create Migrations

```bash
python manage.py makemigrations
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Create Admin User

```bash
python manage.py createsuperuser
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Open the website:

```text
http://127.0.0.1:8000/
```

Open Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

## Testing

Run the Django test suite:

```bash
python manage.py test
```

Check the project for configuration issues:

```bash
python manage.py check
```

---

## Useful Django Commands

```bash
python manage.py runserver
```

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py check
```

```bash
python manage.py test
```

```bash
python manage.py shell
```

---

## Complete Application Flow

```text
                    USER
                     |
                     ↓
                Register
                     |
                     ↓
                  Login
                     |
                     ↓
              Browse Products
                     |
            +--------+--------+
            |                 |
            ↓                 ↓
         Search          Category Filter
            |                 |
            +--------+--------+
                     |
                     ↓
              Product Details
                     |
                     ↓
                Add to Cart
                     |
                     ↓
              Shopping Cart
                     |
              +------+------+
              |             |
              ↓             ↓
       Update Quantity    Remove Item
              |             |
              +------+------+
                     |
                     ↓
                  Checkout
                     |
                     ↓
              Customer Details
                     |
                     ↓
                Place Order
                     |
                     ↓
             Validate Stock
                     |
                     ↓
              Create Order
                     |
                     ↓
            Reduce Stock
                     |
                     ↓
             Clear Cart
                     |
                     ↓
             Order Success
                     |
                     ↓
                My Orders
                     |
                     ↓
             Track Status
                     |
                     ↓
                  ADMIN
                     |
                     ↓
             Manage Order
                     |
                     ↓
           Update Order Status
```

---

## Learning Outcomes

This project provides practical experience with:

* Python programming
* Django framework
* Django ORM
* Models
* Views
* Templates
* Forms
* Authentication
* Authorization
* CRUD operations
* Database relationships
* Shopping cart development
* Order processing
* Inventory management
* Django Admin
* HTML5
* CSS3
* JavaScript
* Responsive web design
* Form validation
* Security practices
* Testing
* Git
* GitHub

---

## Future Improvements

The current project focuses on the core e-commerce workflow.

Future versions could include:

* Online payment gateway
* Wishlist
* Product reviews
* Product ratings
* Discount coupons
* Email order confirmation
* Password reset
* Product pagination
* Advanced filtering
* Inventory alerts
* Sales analytics
* Revenue dashboard
* Multiple payment methods
* Delivery tracking
* REST API
* React frontend
* PostgreSQL database
* Cloud deployment

---

## Project Highlights

```text
User Authentication
        +
Product Management
        +
Search & Category Filter
        +
Shopping Cart
        +
Checkout
        +
Order Processing
        +
Stock Management
        +
Order Tracking
        +
Django Admin
        =
Complete E-commerce Application
```

---
