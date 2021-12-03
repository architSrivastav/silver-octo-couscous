from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Create
# newEntry = ClassName(property = "value",...)
# session.add(newEntry)
# session.commit()

# cheesepizza = menuItem(name="Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
# session.add(cheesepizza)
# session.commit()

# Read
session.query(Restaurant).all()
# items = session.query(MenuItem).all()
# for item in items:
#     print item.name    

# update
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print (veggieBurger.id)
    print (veggieBurger.price)
    print (veggieBurger.restaurant.name)
    print ("\n")

UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 8).one()
print (UrbanVeggieBurger.price)

UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()

for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '$2.99'
        sessiom.add(veggieBurger)
        session.commit()

#delete
spinach =  session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print (spinach.restaurant.name)
session.delete(spinach)
session.commit()