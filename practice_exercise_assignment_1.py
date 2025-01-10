# Exercise 1: Check if the number is even.
def even(n):
  if n % 2 == 0: # if the number is divisible by 2, it is even
    return True # return True if the number is even
  return False # return False if the number is odd

print(even(8))

# Exercise 2: Display a message if a list is empty.
def is_empty(lst):
    if len(lst) == 0: # if the length of the list is 0, it is empty
        return 'List is empty' # return 'List is empty' if the list is empty
    return 'List is not empty' # return 'List is not empty' if the list is not empty

print(is_empty([7,9]))

# Exercise 1: Write a script to check if a number as odd or even.
def is_odd_or_even(number):
    if number % 2 == 0: # if the number is divisible by 2, it is even
        return "even" # return 'even' if the number is even
    else:
        return "odd"    # return 'odd' if the number is odd
print(is_odd_or_even(7))

# Exercise 1: Write a script for Temp categories.
def temp_category(temp):
    if temp <= 0: # If the temperature is less than or equal to 0
        print('Its Freezing Colddd!')
    elif temp <= 10:
        print('Its Cold')
    elif temp <= 20:
        print('Its Moderate')
    elif temp <= 25:
        print('Its Warm')
    else:
        print('Its Hotttt!')

# Example usage
temp = 16
print(temp_category(temp))  # Output: Its Moderate

# Exercise 1: Print each character in a string.
def print_characters(string):
    for char in string: # Iterate through each character in the string
        print(char)

# Example usage
string = 'Hello'
print_characters(string)  # Output: H e l l o

# Exercise 2: Create a list of squares of the first 10 natural numbers.
def squares_of_natural_numbers():
    squares = [i**2 for i in range(1, 11)] # List comprehension to generate squares of numbers from 1 to 10
    return squares

# Example usage
print(squares_of_natural_numbers())  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Exercise 1: Add numbers until sum reaches 100 using while loop.
def sum_until_100():
    total = 0  # Initialize the total sum to 0
    i = 1  # Start with the number 1
    while total < 100:  # Continue the loop until the total sum is less than 100
        total += i  # Add the current number to the total sum
        i += 1  # Increment the number by 1 for the next iteration
    return total  # Return the total sum when it reaches or exceeds 100

# Example usage
print(f"The sum is : {sum_until_100()}")  # Output: The sum is: 105


# Exercise : Guessing game with break on correct guess.
from random import randint

def guess():
    lower,higher = 1,10 # Set the lower and higher limits for the random number
    number = randint(lower,higher) # Generate a random number between the lower and higher limits
    guess_limit = 3 # Set the number of attempts allowed 
    attempts = 0 # Initialize the number of attempts made by the user
    while attempts < guess_limit: # Continue the loop until the user reaches the guess limit
        try:
            user_input = int(input(f"Enter a number between {lower} to {higher}: ")) # Get the user's input
            attempts += 1 # Increment the number of attempts made by the user
            if user_input < number: # If the user's guess is lower than the random number
                print("The number is higher.") # Print a message indicating that the number is higher
            elif user_input > number: # If the user's guess is higher than the random number
                print("The number is lower.") # Print a message indicating that the number is lower
            else:
                return f"Your guess is right! The number is: {number}" # Return a message indicating that the user's guess is correct
        except ValueError:
            print("Please enter a valid integer.") # Print a message if the user enters a non-integer value
    return f"Sorry, you've reached the guess limit. The correct number was: {number}" # Return a message if the user reaches the guess limit

print(guess())
