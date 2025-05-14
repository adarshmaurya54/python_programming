# Question:
# Write a program that takes two numbers as input and divides them. Handle:
# i) Division by zero
# ii) Invalid input (like a string)
#
# Create a BankAccount class. Raise InsufficientFunds (custom exception) if someone tries to withdraw more than the balance.
# • Use try-except to handle errors
# • Use finally to print a "Transaction completed" message

def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: Please enter valid numbers")

class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientFunds("Not enough balance")
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        except InsufficientFunds as e:
            print(f"Error: {e}")
        finally:
            print("Transaction completed")

divide_numbers()

account = BankAccount(1000)
account.withdraw(500)
account.withdraw(1000) 