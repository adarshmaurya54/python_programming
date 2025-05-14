# Question:
# Create three tuples namely: empName, designation, salary. Insert atleast 5 records and perform the following operations:
# i) Zip the tuples
# ii) Extract the names of employees who are Designer and Create a new tuple containing these names.
# iii) Sort the tuple based on salary
# iv) Rename the position "Developer" with "Quality Engineer"
# v) Add a new position of "Quality Analyst with salary 75000"

emp_name = ("John", "Alice", "Bob", "Eve", "Charlie")
designation = ("Designer", "Developer", "Designer", "Developer", "Manager")
salary = (65000, 72000, 68000, 70000, 85000)

zipped_data = list(zip(emp_name, designation, salary))
print("Zipped data:", zipped_data)

designers = tuple(name for name, pos, _ in zipped_data if pos == "Designer")
print("Designers:", designers)

sorted_data = tuple(sorted(zipped_data, key=lambda x: x[2]))
print("Sorted by salary:", sorted_data)

updated_designation = tuple("Quality Engineer" if pos == "Developer" else pos for pos in designation)
print("Updated positions:", updated_designation)

emp_name = emp_name + ("David",)
designation = designation + ("Quality Analyst",)
salary = salary + (75000,)
print("Updated tuples:", list(zip(emp_name, designation, salary))) 