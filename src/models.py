import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(16), nullable=False)
    password = Column(String(30), nullable=False)
    firstname = Column(String(30))
    lastname = Column(String(30))
    email = Column(String(120), nullable=False)

class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True)

class Vehicles(Base):
    __tablename__ = "Vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.id'))

class Character(Base):
    __tablename__ = "Character"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_year = Column(Integer)
    eye_color = Column(String)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.id'))

class Planet(Base):
    __tablename__ = "Planet"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    population = Column(Integer)
    terrain = Column(String)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.id'))
    

class Favorites(Base):
    __tablename__ = "Fav"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'))
    user_id = Column(Integer, ForeignKey('User.id'))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')