# Hooyo's Shop Management System CLI
Welcome to Hooyo's Shop Management System CLI, a command-line interface for managing products, orders, and users in a shop setting. This CLI tool allows users to perform various tasks such as adding and deleting products, managing orders, and handling user accounts.
Hooyo is a Somali word meaning "mom." This project is dedicated to my mom and to all the hardworking moms out there.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Commands](#commands)
   - [Main Menu](#main-menu)
   - [Product Management](#product-management)
   - [Order Management](#order-management)
   - [User Management](#user-management)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)

## Features

- **Product Management**: Add, delete, view, and find products.
- **Order Management**: Create new orders and view existing orders.
- **User Management**: Create and view users.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fardosafara/hooyo-shop-management-system.git
   cd hooyo-shop-management-cli
   ```

2. Set up the database:
   ```bash
   python db_connect.py
   ```

## Usage

Run the CLI:
```bash
python main.py
```

Follow the on-screen prompts to navigate through the menu and perform various tasks.

## Commands

### Main Menu

- **1. Manage Products**: Navigate to product management.
- **2. Manage Orders**: Navigate to order management.
- **3. User Management**: Navigate to user management.
- **4. Exit**: Exit the application.

### Product Management

- **1. Add Product**: Add a new product to the inventory.
- **2. Delete Product**: Delete an existing product by ID.
- **3. View All Products**: View all products in the inventory.
- **4. Find Product by ID**: Find a specific product by its ID.
- **5. Back to Main Menu**: Return to the main menu.

### Order Management

- **1. View Orders**: View all existing orders.
- **2. New Order**: Create a new order.
- **3. Back to Main Menu**: Return to the main menu.

### User Management

- **1. Create User**: Create a new user account.
- **2. View Users**: View all user accounts.
- **3. Back to Main Menu**: Return to the main menu.

## Dependencies

- `sqlalchemy`
- `datetime`
- `db_connect`
- `models` (Product, Order, OrderItem)
- `helper` (authenticate_user, create_user, view_users, get_user_input, get_secure_input, validate_password)

Make sure to install these dependencies using `pip` as mentioned in the installation section.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.



