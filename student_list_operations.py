# Question:
# Create two lists- name and marks of 5 students and perform the following operations:
# i) Display both the lists
# ii) Append the list two with list one
# iii) Display the name and marks of student at index=2
# iv) Add the name and marks of two students
# v) Insert a student record at location 3
# vi) Copy the both the list to a new list
# vii) Copy the items of student list from index 1:4 into a newlist
# viii) Remove the student record of a particular student
# ix) Remove the student record at index =4
# x) Remove the first item of marks list
# xi) Delete all the records of list-marks
# xii) Delete the list student

names = ["John", "Alice", "Bob", "Eve", "Charlie"]
marks = [85, 92, 78, 95, 88]

print("Original lists:")
print(names)
print(marks)

names.extend(marks)
print("After appending:", names)

print(f"Student at index 2: {names[2]}, Marks: {marks[2]}")

names.append("David")
marks.append(91)
names.append("Emma")
marks.append(89)

names.insert(3, "Frank")
marks.insert(3, 82)

new_names = names.copy()
new_marks = marks.copy()

new_list = names[1:4]

names.remove("Alice")
marks.pop(4)
marks.pop(0)

marks.clear()
del names 