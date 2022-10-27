def checkForLeapYear(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

year = int(input("Enter a year : "))

if(checkForLeapYear(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")