# Exercises
# 1. Create a function that takes two parameters for :  name and age, and outputs a Birthday message “ Happy Birthday ‘name’ I hear you are ‘age’ today!”
def birthday(name, age):
    return f"Happy Birthday {name} I hear you are {age} today!"

print(birthday("John", 25))
print("\n" + "-"*50 + "\n")

#2. Create a function that takes two parameters: size and type of drink, and then outputs the drinks order.

def order(size, drink):
    return f"Order: {size} {drink}"

print(order("Regular", "Mocha"))
print("\n" + "-"*50 + "\n")

#3  Create a cash machine program that takes a pin number and amount. Outputs cash is being dispensed if the pin is correct and there is enough money to withdraw. Finally outputs the new balance.

def withdraw_cash(pin, balance, pin_number, amount):
    if pin == pin_number:
        if balance >= amount:
            balance -= amount
            return f"Cash is being dispensed. New balance: {balance}"
        else:
            return "Insufficient funds"
    else:
        return "Incorrect pin, transaction cancelled"

def main():
    pin_number = 6678
    balance = 2000
    pin = int(input("Enter pin number: "))
    amount = float(input("Enter amount to withdraw: "))
    print(withdraw_cash(pin, balance, pin_number, amount))

if __name__ == "__main__":
    main()
    print("\n" + "-"*50 + "\n")



# 4 Excercise

# *  Create a list of your fav sport game.
# *  Add 'Hockey' to your list
# * Access the first 4 elements
# * Access the only 5th element
# * Replace Hockey with Ice-Hockey
# * Remove the 2nd element of your list
# * Reverse the list
# * Sort the list
# * Pop Ice-Hockey off the list
# * Clear all the elemenst from that list

fav_sport = ["Football", "Basketball", "Tennis", "Cricket"]
fav_sport.append("Hockey")
print(fav_sport)

print(fav_sport[:4])
print(fav_sport[4])
fav_sport[4] = "Ice-Hockey"
print(fav_sport)
fav_sport.pop(1)
print(fav_sport)
fav_sport.reverse()
print(fav_sport)
fav_sport.sort()
print(fav_sport)
fav_sport.remove("Ice-Hockey")
print(fav_sport)
fav_sport.clear()
print(fav_sport)
print("\n" + "-"*50 + "\n")


# More Exercises
# Roll The Dice 

# 1  ​Using the random module, can you write a program that rolls a dice.

#  If the dice rolls a 6, print “Congrats! Move 2 spaces!”. If the dice doesn’t roll a 6, print “Try again!”

from random import randint

def roll_dice():
    return randint(1, 6)


def main():
    dice = roll_dice()
    if dice == 6:
        print("Congrats! Move 2 spaces!")
    else:
        print("Try again!")

if __name__ == "__main__":
    main()
    print("\n" + "-"*50 + "\n")

# 2. Tuple Exercise
# Scenario:
# You are managing inventory for a small grocery store, and you want to use tuples to represent the items in stock. Each tuple will contain information about a specific item, including its name, price, and quantity available.
# Instructions:
# * Create tuples for different items in stock, with each tuple containing information in the format (name, price, quantity).
# * Perform tuple operations to analyze the inventory, such as finding the total value of the inventory or identifying items that need restocking based on their quantity


# Creating tuples for different items in stock
item1 = ("Tomatoes", 0.8, 120)
item2 = ("Potatoes", 0.4, 200)
item3 = ("Onions", 0.6, 90)
item4 = ("Carrots", 0.5, 60)
item5 = ("Cucumbers", 0.7, 40)

# List of all items
inventory = [item1, item2, item3, item4, item5]

# Function to display items in stock
def display_items(inventory):
    print("Items in stock:")
    for item in inventory:
        print(f"Name: {item[0]}, Price: £{item[1]}, Quantity: {item[2]}")

# Function to calculate the total value of the inventory using sum
def calculate_total_value(inventory):
    total_value = sum(price * quantity for _, price, quantity in inventory)
    return total_value

# Function to calculate the total value of the inventory using a loop

def total_inventory_value(inventory):
    total_value = 0
    for item in inventory:
        total_value += item[1] * item[2]  # price * quantity
    return total_value


# Function to identify items that need restocking based on their quantity
def identify_restock_items(inventory, threshold=50):
    restock_items = [item for item in inventory if item[2] < threshold]
    return restock_items
# print(f"Restock items: {identify_restock_items(inventory)}")

# def identify_restocking_items(inventory, threshold=50):
#     restock_items = [name for name, _, quantity in inventory if quantity < threshold]
#     return restock_items
# print(f"Restock items: {identify_restocking_items(inventory)}")

# Example usage
display_items(inventory)  # Display all items in stock

print(f"Total inventory value: £{total_inventory_value(inventory):.2f}")  # Output: Total inventory value: £288.00

restock_items = identify_restock_items(inventory)
print("Items to restock:")
for item in restock_items:
    print(f"{item[0]} needs for restocking")  # Output: Cucumbers 
print("\n" + "-"*50 + "\n")


# 3. Set Exercise
# Scenario:
# You are organizing a conference and need to keep track of attendees who have registered for the event. You want to use sets to manage the attendee data efficiently.
# Instructions:
# * Create sets representing different categories of attendees, such as regular attendees, VIP attendees, and speakers.
# * Add attendees to the respective sets as they register for the event.
# * Perform set operations to analyze the attendee data, such as finding common attendees between different categories or identifying unique attendees in each category

# * Create sets representing different categories of attendees, such as regular attendees, VIP attendees, and speakers.
regular_attendees = {"John", "Mary", "David", "Sarah"}
vip_attendees = {"Alice", "Frank", "David", "Sarah"}
speakers = {"George", "Hannah", "Eva"}

# * Add attendees to the respective sets as they register for the event.
regular_attendees.add("Ivy")
vip_attendees.add("Jack")
speakers.add("Karen")

# Displaying the sets
print("Regular Attendees:", regular_attendees)
print("VIP Attendees:", vip_attendees)
print("Speakers:", speakers)

# Finding common attendees between different categories
common_vip_speakers = vip_attendees.intersection(speakers)
print("Common VIP and Speakers:", common_vip_speakers)

# Identifying unique attendees in each category
unique_regular_attendees = regular_attendees.difference(vip_attendees, speakers)
unique_vip_attendees = vip_attendees.difference(regular_attendees, speakers)
unique_speakers = speakers.difference(regular_attendees, vip_attendees)

print("Unique Regular Attendees:", unique_regular_attendees)
print("Unique VIP Attendees:", unique_vip_attendees)
print("Unique Speakers:", unique_speakers)
print("\n" + "-"*50 + "\n")

# 4. Dictionary Exercise
# Scenario:
# You are the manager of a retail store, and you need to keep track of the inventory of various products available in your store. You want to use dictionaries to efficiently manage the product data..
# Instructions:
# * Create a dictionary where the keys represent the product names, and the values represent the corresponding quantities of each product in stock.
# * Update the inventory as new products arrive or existing products are sold.
# * Perform dictionary operations to analyze the inventory data, such as finding the total quantity of products, identifying low-stock items, or retrieving product information.

# Create a dictionary where the keys represent the product names, and the values represent the corresponding quantities of each product in stock.

inventory = { "Apples": 100, "Bananas": 150, "Oranges": 80, "Grapes": 120, "Pineapples": 50 }

# Update the inventory as new products arrive or existing products are sold.
inventory["Mangoes"] = 70  # New product added
inventory["Bananas"] -= 20  # Existing product sold

# Displaying the inventory
print("Inventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")

# Perform dictionary operations to analyze the inventory datas
total_quantity = sum(inventory.values())
print(f"Total quantity of products: {total_quantity}")

low_stock_items = {product: quantity for product, quantity in inventory.items() if quantity < 100}
print("Low-stock items:")
for product, quantity in low_stock_items.items():
    print(f"{product}: {quantity}")

# Retrieving product information
product_name = "Cherry"
product_quantity = inventory.get(product_name, "Product not found")
print(f"Retrieving product information {product_name}: {product_quantity}")
print("\n" + "-"*50 + "\n")


