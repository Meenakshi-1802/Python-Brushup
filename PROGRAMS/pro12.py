## Leap Year
year = int(input("Enter the year:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It is a Leap year")
else:
    print("It is not a leap year")
