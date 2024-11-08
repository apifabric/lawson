# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define base class
Base = declarative_base()

# Example Table Definitions

class Employee(Base):
    """description: Represents an employee in the organization."""
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    hire_date = Column(DateTime, default=datetime.utcnow)

class Department(Base):
    """description: Represents a department within the company."""
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    location = Column(String, nullable=True)

class Position(Base):
    """description: Represents the position or role of an employee."""
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    salary = Column(Float, nullable=True)

class Project(Base):
    """description: Represents a project handled by the company."""
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String, nullable=True)
    start_date = Column(DateTime, default=datetime.utcnow)

class EmployeeProject(Base):
    """description: Junction table linking employees to projects."""
    __tablename__ = 'employee_project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=False)

class Customer(Base):
    """description: Represents a customer of the company."""
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=True)

class Order(Base):
    """description: Represents an order made by a customer."""
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Float, nullable=True)

class Product(Base):
    """description: Represents a product available for sale."""
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    price = Column(Float, nullable=True)

class OrderItem(Base):
    """description: Represents the relationship between orders and products."""
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=True)

class Vendor(Base):
    """description: Represents a vendor supplying products."""
    __tablename__ = 'vendor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    contact_info = Column(String, nullable=True)

class Inventory(Base):
    """description: Represents inventory details for products."""
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity_in_stock = Column(Integer, nullable=True)

class Shipment(Base):
    """description: Represents a shipment sent by a vendor."""
    __tablename__ = 'shipment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_id = Column(Integer, ForeignKey('vendor.id'), nullable=False)
    shipment_date = Column(DateTime, default=datetime.utcnow)

# Create a SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Sample data insertions

# Employees and positions
employee1 = Employee(first_name='John', last_name='Doe', hire_date=datetime(2022, 5, 1))
employee2 = Employee(first_name='Jane', last_name='Smith', hire_date=datetime(2021, 8, 15))
position1 = Position(title='Developer', salary=75000.0)
position2 = Position(title='Manager', salary=90000.0)

# Departments
department1 = Department(name='Engineering', location='Building A')
department2 = Department(name='Sales', location='Building B')

# Projects and Employee Projects
project1 = Project(project_name='Project Alpha', start_date=datetime(2023, 1, 5))
employee_project1 = EmployeeProject(employee_id=1, project_id=1)

# Customers and Orders
customer1 = Customer(first_name='Alice', last_name='Johnson', email='alice@example.com')
order1 = Order(customer_id=1, order_date=datetime(2023, 7, 10), total_amount=150.00)

# Products and Order Items
product1 = Product(name='Widget', price=20.00)
order_item1 = OrderItem(order_id=1, product_id=1, quantity=5)

# Vendors, Inventory, and Shipments
vendor1 = Vendor(name='Global Supplies', contact_info='info@globalsupplies.com')
inventory1 = Inventory(product_id=1, quantity_in_stock=100)
shipment1 = Shipment(vendor_id=1, shipment_date=datetime(2023, 6, 1))

# Add all to session
session.add_all([
    employee1, employee2, position1, position2,
    department1, department2, project1, employee_project1,
    customer1, order1, product1, order_item1,
    vendor1, inventory1, shipment1
])

# Commit the session
session.commit()
