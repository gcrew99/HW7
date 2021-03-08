# Written by Gabriel Crew
# Function to determine whether a given year is a leap  year

leapStr = input("Enter a Year and I'll tell you if it's a leap year or not:" )

def leapYear(leapStr):
  leapNum = int(leapStr)
  if (leapNum % 4) == 0:
    string = "Leap year"
  else:
    string ="Not a Leap Year"
  return string