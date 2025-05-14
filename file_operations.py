# Question:
# Create a text file and Perform the following operations on the file:
# a) Open the file and Read the contents from the file.
# b) Check if the file exists or not
# c) Write the content and display
# d) Append the content to the existing file and display it
# e) Remove the file

# File operations

import os

filename = "sample.txt"

with open(filename, "w") as f:
    f.write("Initial content\n")

if os.path.exists(filename):
    with open(filename, "r") as f:
        print("File contents:", f.read())

with open(filename, "w") as f:
    f.write("New content\n")
with open(filename, "r") as f:
    print("After writing:", f.read())

with open(filename, "a") as f:
    f.write("Appended content\n")
with open(filename, "r") as f:
    print("After appending:", f.read())

os.remove(filename) 