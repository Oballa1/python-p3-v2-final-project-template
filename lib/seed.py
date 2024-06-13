from models.chefs import Chef
from models.meals import Meal

Chef.drop_table()
Chef.create_table()

Meal.drop_table()
Meal.create_table()

#Creating seed data
Chef.create( "John", "Smith", "Johnny", "10:00-12:00")
Chef.create( "Jane", "Doe", "Jane", "12:00-14:00")
Chef.create( "Jill", "Smith", "Jill", "14:00-16:00")


Meal.create( "Pizza", 30, "Monday", 1)
Meal.create( "Burger", 20, "Tuesday", 2)
