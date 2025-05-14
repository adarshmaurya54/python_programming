# Question:
# Create a dictionary whose keys are month names and whose values are the number of days in the corresponding months.
# i) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
# ii) Print out all keys in the alphabetically order
# iii) Print out all the months with 31 days
# iv) Print out the key value pairs sorted by number of days in each month

months = {
    "January": 31, "February": 28, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31,
    "September": 30, "October": 31, "November": 30, "December": 31
}

month = input("Enter month name: ")
if month in months:
    print(f"{month} has {months[month]} days")

sorted_keys = sorted(months.keys())
print("Months in alphabetical order:", sorted_keys)

months_31 = [month for month, days in months.items() if days == 31]
print("Months with 31 days:", months_31)

sorted_by_days = sorted(months.items(), key=lambda x: x[1])
print("Months sorted by number of days:", sorted_by_days) 