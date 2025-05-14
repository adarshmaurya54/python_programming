# Question:
# Create a package named utilities that contains two modules:
# • math_utils.py: Should contain functions for multiplication and division.
# • string_utils.py: Should contain functions to count vowels and check if a string is a palindrome.
# • Write a main script that:
# • Imports the necessary modules from utilities.
# • Takes two numbers as user input and performs multiplication and division.
# • Takes a string as user input and:
#   o Counts the number of vowels.
#   o Checks if the string is a palindrome.

from math_utils import multiply, divide
from string_utils import count_vowels, is_palindrome

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
print("Is palindrome:", is_palindrome(text)) 