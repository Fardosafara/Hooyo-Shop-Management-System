from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from models.product import Product
from models.order import Order
from models.order_item import OrderItem
from db_connect import connect_db, engine

app = Flask(__name__)

# Ensure the database and tables are created
connect_db()

# Set up SQLAlchemy session
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/add_product', methods=['GET', 'POST'])
def add_product_route():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        uom = request.form['uom']
        price = float(request.form['price'])
        session = Session()
        product = Product(name=name, quantity=quantity, uom=uom, price=price)
        session.add(product)
        session.commit()
        return redirect(url_for('view_products_route'))
    return render_template('add_product.html')

@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product_route(product_id):
    session = Session()
    product = session.query(Product).get(product_id)
    if product:
        session.delete(product)
        session.commit()
    return redirect(url_for('delete_product_list'))

@app.route('/delete_product_list')
def delete_product_list():
    session = Session()
    products = session.query(Product).all()
    return render_template('delete_product.html', products=products)

@app.route('/view_products')
def view_products_route():
    session = Session()
    products = session.query(Product).all()
    return render_template('view_products.html', products=products)

@app.route('/orders')
def view_orders_route():
    session = Session()
    orders = session.query(Order).all()
    return render_template('orders.html', orders=orders)

@app.route('/new_order', methods=['GET', 'POST'])
def new_order_route():
    if request.method == 'POST':
        date_str = request.form['date']
        customer_name = request.form['customer_name']
        customer_phone = request.form['customer_phone']
        customer_address = request.form['customer_address']
        total_cost = float(request.form['total_cost'])

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            session = Session()
            order_number = session.query(Order).count() + 1
            order = Order(
                date=date, 
                customer_name=customer_name, 
                customer_phone=customer_phone, 
                customer_address=customer_address, 
                total_cost=total_cost, 
                order_number=order_number
            )
            session.add(order)
            session.commit()
            return redirect(url_for('view_orders_route'))
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")
            return redirect(url_for('new_order_route'))
    
    return render_template('new_order.html')

if __name__ == '__main__':
    app.run(debug=True)
