# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 08, 2024 05:41:24
# Database: sqlite:////tmp/tmp.GH3mLnJW3l/lawson/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Represents a customer of the company.
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class Department(SAFRSBaseX, Base):
    """
    description: Represents a department within the company.
    """
    __tablename__ = 'department'
    _s_collection_name = 'Department'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Employee(SAFRSBaseX, Base):
    """
    description: Represents an employee in the organization.
    """
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    hire_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    EmployeeProjectList : Mapped[List["EmployeeProject"]] = relationship(back_populates="employee")



class Position(SAFRSBaseX, Base):
    """
    description: Represents the position or role of an employee.
    """
    __tablename__ = 'position'
    _s_collection_name = 'Position'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    salary = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)



class Product(SAFRSBaseX, Base):
    """
    description: Represents a product available for sale.
    """
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="product")
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="product")



class Project(SAFRSBaseX, Base):
    """
    description: Represents a project handled by the company.
    """
    __tablename__ = 'project'
    _s_collection_name = 'Project'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    project_name = Column(String)
    start_date = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)
    EmployeeProjectList : Mapped[List["EmployeeProject"]] = relationship(back_populates="project")



class Vendor(SAFRSBaseX, Base):
    """
    description: Represents a vendor supplying products.
    """
    __tablename__ = 'vendor'
    _s_collection_name = 'Vendor'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_info = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ShipmentList : Mapped[List["Shipment"]] = relationship(back_populates="vendor")



class EmployeeProject(SAFRSBaseX, Base):
    """
    description: Junction table linking employees to projects.
    """
    __tablename__ = 'employee_project'
    _s_collection_name = 'EmployeeProject'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    employee_id = Column(ForeignKey('employee.id'), nullable=False)
    project_id = Column(ForeignKey('project.id'), nullable=False)

    # parent relationships (access parent)
    employee : Mapped["Employee"] = relationship(back_populates=("EmployeeProjectList"))
    project : Mapped["Project"] = relationship(back_populates=("EmployeeProjectList"))

    # child relationships (access children)



class Inventory(SAFRSBaseX, Base):
    """
    description: Represents inventory details for products.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    quantity_in_stock = Column(Integer)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Represents an order made by a customer.
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'), nullable=False)
    order_date = Column(DateTime)
    total_amount = Column(Float)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class Shipment(SAFRSBaseX, Base):
    """
    description: Represents a shipment sent by a vendor.
    """
    __tablename__ = 'shipment'
    _s_collection_name = 'Shipment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    vendor_id = Column(ForeignKey('vendor.id'), nullable=False)
    shipment_date = Column(DateTime)

    # parent relationships (access parent)
    vendor : Mapped["Vendor"] = relationship(back_populates=("ShipmentList"))

    # child relationships (access children)



class OrderItem(SAFRSBaseX, Base):
    """
    description: Represents the relationship between orders and products.
    """
    __tablename__ = 'order_item'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order.id'), nullable=False)
    product_id = Column(ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)
