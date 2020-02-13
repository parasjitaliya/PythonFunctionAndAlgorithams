import Utility
# take user input
year = int(input("Enter the year for check is leap year or not:"))

#condition for leapyear or not leapyear
if (Utility.checkyear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")
