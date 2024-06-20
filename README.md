# Hooyo-Shop-Management-System
Hooyo Shop Management System
Hooyo is a Somali word meaning "mom." This project is dedicated to my mom and to all the hardworking moms out there. The Hooyo Shop Management System is a web-based application designed to manage products, orders, and users for small shops and businesses.

Table of Contents
Introduction
Features
Installation
Usage
Project Structure
Contributing
Acknowledgements
Introduction
The Hooyo Shop Management System allows users to manage their products, orders, It provides an easy-to-use interface for adding, viewing, and deleting products and orders, as well as creating and managing user accounts in the CLI.

Features
Product Management: Add, view, and delete products.
Order Management: Create and view orders with customer details and total cost.
User Management: Create user accounts with authentication.
CLI Integration: Manage products and orders through a command-line interface.
Installation
Prerequisites
Python 3.6 or higher
SQLite
Setup
Clone the repository:

sh
Copy code
git clone https://github.com/Fardosafara/hooyo-shop-management-system
cd hooyo-shop-management-system
Create a virtual environment:

sh
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

sh
Copy code
pip install -r requirements.txt
Set up the database:

sh
Copy code
python db_connect.py
Run the Flask application:

sh
Copy code
python app.py
Run the CLI:

sh
Copy code
python cli.py
Usage
Web Interface
Home Page: Navigate to http://127.0.0.1:5000/ to access the home page.
Add Product: Navigate to http://127.0.0.1:5000/add_product to add new products.
View Products: Navigate to http://127.0.0.1:5000/view_products to view all products.
Delete Product: Navigate to http://127.0.0.1:5000/delete_product_list to delete products.
Create Order: Navigate to http://127.0.0.1:5000/new_order to create a new order.
View Orders: Navigate to http://127.0.0.1:5000/orders to view all orders.
CLI Interface
Main Menu: Run python cli.py to start the CLI and navigate through the options to manage products, orders, and users.
Project Structure
plaintext
Copy code
hooyo-shop-management/
│
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── order.py
│   ├── order_item.py
│   └── user.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_product.html
│   ├── view_products.html
│   ├── delete_product.html
│   ├── orders.html
│   ├── new_order.html
│   └── profile.html
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── db_connect.py
├── app.py
├── cli.py
├── helper.py
└── README.md
Contributing
Fork the repository
Create a new branch
Make your changes
Submit a pull request

Acknowledgements
This project is dedicated to my mom and all hardworking moms.

