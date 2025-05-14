# Question:
# Write a program to perform the following operations:
# i) create, concatenate and print a string 
# ii) Make a list of first 10 letters of the alphabet, then use the slicing to do the following operations: 
#     a. Print the first 3 letters of the list 
#     b. Print any 3 letters from the middle 
#     c. Print the letter from any particular index to the end of the list

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(letters[:3])
print(letters[3:6])
print(letters[4:]) 