## **Q1: Tuple Operations with Indian Names**
```
# Create tuples
empName = ("Adarsh", "Ravi", "Priya", "Meena", "Amit")
designation = ("Developer", "Designer", "Tester", "Designer", "Manager")
salary = (70000, 60000, 50000, 65000, 90000)

# i) Zip the tuples
employees = list(zip(empName, designation, salary))
print("Zipped Tuple:")
print(employees)

# ii) Extract names of employees who are Designer and create a new tuple
designers = tuple(emp[0] for emp in employees if emp[1] == "Designer")
print("\nNames of Designers:")
print(designers)

# iii) Sort the tuple based on salary
sorted_by_salary = sorted(employees, key=lambda x: x[2])
print("\nSorted by Salary:")
print(sorted_by_salary)

# iv) Add a new position of “Quality Analyst with salary 75000”
updated_employees = employees + [("Neha", "Quality Analyst", 75000)]
print("\nAfter Adding Quality Analyst:")
print(updated_employees)
```

## **Q2: File Copy Using Only ```os``` Module**
```
import os

def copy_file(source, destination):
    # i) Check if source file exists
    if not os.path.exists(source):
        print("Source file does not exist.")
        return

    # Check if destination file exists
    if os.path.exists(destination):
        user_input = input("Destination file exists. Overwrite? (yes/no): ").strip().lower()
        if user_input != 'yes':
            print("Operation cancelled.")
            return

    # Read from source and write to destination
    with open(source, 'r') as src_file:
        data = src_file.read()

    with open(destination, 'w') as dest_file:
        dest_file.write(data)

    print("File copied successfully.")

    # ii) Delete the source file
    os.remove(source)
    print("Source file deleted.")

# Example usage (uncomment and provide actual filenames to run)
# copy_file("source.txt", "destination.txt")
```
