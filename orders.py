from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db_connect import Base

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String, nullable=False)
    order_number = Column(Integer, nullable=False, unique=True)
    customer_name = Column(String, nullable=False)
    total_cost = Column(Float, nullable=False)

    @classmethod
    def get_all_orders(cls):
        session = Session()
        return session.query(cls).all()

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

Order.order_items = relationship("OrderItem", order_by=OrderItem.id, back_populates="order")
