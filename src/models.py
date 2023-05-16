import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(1024), nullable=False)
    precio = Column(Integer, primary_key=True) # Debe ser Numeric en vez de Integer, fix it
    categorias = relationship("Categoria", backref="productos")
    categoria_id = Column(String(50), ForeignKey('categories.id'))
    
class Categoria(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

class ShoppingCart(Base):
    _tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    user = relationship("Person", backref="carrito")
    productos = relationship("Productos", backref="likes")







## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
