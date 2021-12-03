import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(80))
    description = Column(String(80))
    price = Column(String(80))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    # ^variable is reln b/w    ^class Restaurant


# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):
# this serializable fxn will help define what data we want to 
# send across
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }
############insert at the end of file#################

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)