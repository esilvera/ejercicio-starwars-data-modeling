import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    user_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    films = Column(String(150))
    starships = Column(String(50), ForeignKey("ships.id"))
    homeworld = Column(String(50), ForeignKey("planets.id"))
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    planets = relationship(Characters)

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    ships = relationship(Characters)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("user.id"))
    id_planet = Column(Integer, ForeignKey("planets.id"))
    id_ship = Column(Integer, ForeignKey("ships.id"))
    id_character = Column(Integer, ForeignKey("characters.id"))
    favorites = relationship(User)
    

""" 
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

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
        return {} """
        
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')