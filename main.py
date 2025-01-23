


# Create a Function: Turn this logic into a function called suggest_destination(budget) that:

# Accepts budget as an argument.
# Returns the suggestion as a string.

from budgetFunction import budgetFunction
from calculator import add
from weather_advice import weather_device
from password import validate_password


print(budgetFunction(300))
print(add(10,5))
print(weather_device("sunny"))
print(validate_password("Pass1234!"))

####################################################################################################
# Instructions for Students:

# Create a function that takes weather as an argument and returns the appropriate advice.
# Optionally, create a class WeatherAssistant with a method for weather advice.
#Move the weather advice logic into a file named weather_advice.py.





# Instructions for Students:

# Refactor this code by creating functions to:
# Add an item to the shopping list.
# Remove an item from the shopping list.
# Print all items in the shopping list.
# Optionally, create a ShoppingList class that manages the list with the above methods.
#Move the shopping list logic into a file named shopping_list.py.





# Instructions for Students:

# Refactor this code by creating two functions:
# celsius_to_fahrenheit(celsius)
# fahrenheit_to_celsius(fahrenheit)
# Consider creating a TemperatureConverter class with these methods.

# celsius = 25
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C is {fahrenheit}°F")

# fahrenheit = 77
# celsius = (fahrenheit - 32) * 5/9
# print(f"{fahrenheit}°F is {celsius}°C")






# Instructions for Students:

# Create functions for:
# Adding an item to the inventory.
# Removing an item from the inventory.
# Printing the inventory.
# Optionally, organize these into an Inventory class.


# inventory = {}
# inventory["apples"] = 10
# inventory["bananas"] = 5
# inventory["apples"] -= 3
# if inventory["apples"] <= 0:
#     del inventory["apples"]
# print(inventory)







# Instructions for Students:

# Refactor this code by creating a validate_password(password) function.
# Extend it to check for additional rules like special characters.
