import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    pass_user = Column(String(250), nullable=False)
    email_user = Column(String(250), nullable=False, unique=True)
    url_user = Column(String(250), nullable=False)
    presentacion = Column(String(250), nullable=False)
    foto_user = Column(String(250))
    

class Follower(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer,ForeignKey('user.id'))  
    id_user_follower = Column(Integer,ForeignKey('user.id'))



class Following(Base):
    __tablename__ = 'followings'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer,ForeignKey('user.id'))  
    id_user_following = Column(Integer,ForeignKey('user.id'))



class Post(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_user_post = Column(Integer,ForeignKey('user.id'))
    id_tipo_post = Column(Integer,ForeignKey('tipo_post.id'))
    descripcion = Column(String(250), nullable=False)
    like = Column(Integer, nullable=False)


class Tipo_Post(Base):
    __tablename__ = 'potipo_posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    tipo_post = Column(String(250), nullable=False)



class Comment(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_post = Column(Integer,ForeignKey('post.id'))
    descripcion = Column(String(250), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e