from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

if __package__ is None or __package__ == '':
    from database import Base
else:
    from .database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    sku = Column(String(80), unique=True, nullable=False, index=True)
    stock = Column(Integer, default=0, nullable=False)
    description = Column(String(400), nullable=True)
    price = Column(Integer, default=0, nullable=False)
    orders = relationship('Order', back_populates='product')

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    email = Column(String(200), unique=True, nullable=False, index=True)
    phone = Column(String(40), nullable=True)
    orders = relationship('Order', back_populates='customer')

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    product = relationship('Product', back_populates='orders')
    customer = relationship('Customer', back_populates='orders')
