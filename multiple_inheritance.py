# Question:
# Write a Python program that demonstrates multiple inheritance, where:
# • A Parent class Person has an attribute name and a method show_name().
# • Another Parent class Job has an attribute designation and a method show_job().
# • A Child class Employee inherits from both Person and Job and has an additional attribute salary.
# • Create an object of Employee and call all the methods.

# Multiple inheritance demonstration

class Person:
    def __init__(self, name):
        self.name = name
    
    def show_name(self):
        print(f"Name: {self.name}")

class Job:
    def __init__(self, designation):
        self.designation = designation
    
    def show_job(self):
        print(f"Designation: {self.designation}")

class Employee(Person, Job):
    def __init__(self, name, designation, salary):
        Person.__init__(self, name)
        Job.__init__(self, designation)
        self.salary = salary

emp = Employee("John Doe", "Software Engineer", 75000)
emp.show_name()
emp.show_job()
print(f"Salary: {emp.salary}") 