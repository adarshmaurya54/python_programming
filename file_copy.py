# Question:
# Write a program to copy the contents of one file into a new file.
# i. The operations should be performed only if the file exists and user permits to overwrite the content of the destination file.
# ii. Delete the source file once the contents are copied to destination file

import os

source = "source.txt"
destination = "destination.txt"

if not os.path.exists(source):
    print("Source file does not exist")
    exit()

if os.path.exists(destination):
    permission = input("Destination file exists. Overwrite? (y/n): ")
    if permission.lower() != 'y':
        print("Operation cancelled")
        exit()

with open(source, "r") as src:
    content = src.read()
    with open(destination, "w") as dest:
        dest.write(content)

os.remove(source)
print("File copied and source file deleted") 