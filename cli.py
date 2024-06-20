from sqlalchemy.orm import Session
from db_connect import engine
from models.product import Product
from models.order import Order
from models.order_item import OrderItem
from helper import authenticate_user, create_user, view_users, get_user_input, get_secure_input, validate_password
from datetime import datetime

class CLI:
    def __init__(self):
        self.session = Session(bind=engine)
        self.current_user = None

    def main_menu(self):
        while True:
            print("\nHooyo's Shop Management System")
            print("1. Manage Products")
            print("2. Manage Orders")
            print("3. User Management")
            print("4. Exit")
            choice = get_user_input("Enter choice: ")

            if choice == '1':
                self.manage_products()
            elif choice == '2':
                self.manage_orders()
            elif choice == '3':
                self.user_management()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_products(self):
        while True:
            print("\nManage Products")
            print("1. Add Product")
            print("2. Delete Product")
            print("3. View All Products")
            print("4. Find Product by ID")
            print("5. Back to Main Menu")
            choice = get_user_input("Enter choice: ")

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.delete_product()
            elif choice == '3':
                self.view_all_products()
            elif choice == '4':
                self.find_product_by_id()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_product(self):
        name = get_user_input("Enter product name: ")
        quantity = int(get_user_input("Enter product quantity: "))
        uom = get_user_input("Enter unit of measurement: ")
        try:
            price = float(get_user_input("Enter product price: "))
            product = Product(name=name, quantity=quantity, uom=uom, price=price)
            self.session.add(product)
            self.session.commit()
            print("Product added successfully.")
        except ValueError:
            print("Invalid price. Please enter a valid number.")

    def delete_product(self):
        products = self.session.query(Product).all()
        if products:
            print("\nProducts List:")
            for product in products:
                print(f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, UOM: {product.uom}, Price: {product.price}")

            try:
                product_id = int(get_user_input("Enter product ID to delete: "))
                product = self.session.query(Product).get(product_id)
                if product:
                    self.session.delete(product)
                    self.session.commit()
                    print("Product deleted successfully.")
                else:
                    print("Product not found.")
            except ValueError:
                print("Invalid product ID. Please enter a valid number.")
        else:
            print("No products available to delete.")

    def view_all_products(self):
        products = self.session.query(Product).all()
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, UOM: {product.uom}, Price: {product.price}")

    def find_product_by_id(self):
        try:
            product_id = int(get_user_input("Enter product ID: "))
            product = self.session.query(Product).get(product_id)
            if product:
                print(f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, UOM: {product.uom}, Price: {product.price}")
            else:
                print("Product not found.")
        except ValueError:
            print("Invalid product ID. Please enter a valid number.")

    def manage_orders(self):
        while True:
            print("\nManage Orders")
            print("1. View Orders")
            print("2. New Order")
            print("3. Back to Main Menu")
            choice = get_user_input("Enter choice: ")

            if choice == '1':
                self.view_orders()
            elif choice == '2':
                self.new_order()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def view_orders(self):
        orders = self.session.query(Order).all()
        for order in orders:
            print(f"ID: {order.id}, Date: {order.date}, Order Number: {order.order_number}, Customer: {order.customer_name}, Phone: {order.customer_phone}, Address: {order.customer_address}, Total Cost: {order.total_cost}")
            for item in order.order_items:
                product = self.session.query(Product).get(item.product_id)
                print(f"    Product: {product.name}, Quantity: {item.quantity}, Description: {item.description}")

    def new_order(self):
        date_str = get_user_input("Enter order date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")
            return

        customer_name = get_user_input("Enter customer name: ")
        customer_phone = get_user_input("Enter customer phone number: ")
        customer_address = get_user_input("Enter customer address: ")
        total_cost_input = get_user_input("Enter total cost: ")
        try:
            total_cost = float(total_cost_input)
            order_number = self.session.query(Order).count() + 1
            order = Order(date=date, customer_name=customer_name, customer_phone=customer_phone, customer_address=customer_address, total_cost=total_cost, order_number=order_number)
            self.session.add(order)
            self.session.commit()
            self.add_order_items(order.id)
            print("Order added successfully.")
        except ValueError:
            print("Invalid cost format. Please enter a valid number.")

    def add_order_items(self, order_id):
        while True:
            try:
                product_id = int(get_user_input("Enter product ID: "))
                product = self.session.query(Product).get(product_id)
                if product:
                    description = get_user_input("Enter item description: ")
                    quantity = int(get_user_input("Enter quantity: "))
                    if product.quantity >= quantity:
                        order_item = OrderItem(order_id=order_id, product_id=product_id, description=description, quantity=quantity)
                        product.quantity -= quantity
                        self.session.add(order_item)
                        self.session.commit()
                        print(f"Added {quantity} of {product.name} to the order with description: {description}.")
                    else:
                        print(f"Insufficient quantity of {product.name}. Available: {product.quantity}")
                else:
                    print("Invalid product ID.")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

            another = get_user_input("Add another item? (yes/no): ").strip().lower()
            if another != 'yes':
                break

    def user_management(self):
        while True:
            print("\nUser Management")
            print("1. Create User")
            print("2. View Users")
            print("3. Back to Main Menu")
            choice = get_user_input("Enter choice: ")

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.view_users()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def create_user(self):
        username = get_user_input("Enter username: ")
        password = get_secure_input("Enter password: ")
        if not validate_password(password):
            print("Password must be at least 8 characters long and contain at least one number.")
            return
        name = get_user_input("Enter your name: ")
        phone_number = get_user_input("Enter your phone number: ")
        try:
            create_user(self.session, username, password, name, phone_number)
            print("User created successfully.")
        except ValueError as e:
            print(e)

    def view_users(self):
        view_users(self.session)

if __name__ == '__main__':
    cli = CLI()
    cli.main_menu()
