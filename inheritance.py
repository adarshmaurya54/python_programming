# Question:
# Write a Python program using inheritance, where:
# i. Create a Parent class Employee with attributes name and salary.
# ii. Define a method show_details() in Employee to display the employee's name and salary.
# iii. Create a Child class Manager that inherits from Employee and has an additional attribute department.
# iv. Override the show_details() method in Manager to display all details, including department.
# v. Use super() in the Manager class to call the parent class constructor.
# vi. Create an object of Manager and print the details.

# Single inheritance demonstration

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def show_details(self):
        super().show_details()
        print(f"Department: {self.department}")

manager = Manager("John Doe", 85000, "IT")
manager.show_details() 