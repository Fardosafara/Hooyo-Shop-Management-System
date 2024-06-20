from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from models import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    customer_name = Column(String, nullable=False)
    customer_phone = Column(String, nullable=False)
    customer_address = Column(String, nullable=False)
    total_cost = Column(Float, nullable=False)
    order_number = Column(Integer, unique=True, nullable=False)
    order_items = relationship('OrderItem', back_populates='order')
