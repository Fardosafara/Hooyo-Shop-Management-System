from sqlalchemy import Column, Integer, String, Float
from models import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    uom = Column(String, nullable=False)
    price = Column(Float, nullable=False)
