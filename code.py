

def fizzBuzz(x):
      string = ""
      for i in range(x):
        if (i%3 == 0): 
          string = string + "Fizz"
        else:
          string = string + i
      return string

x_in = input("Type number from 1 to 100  ")
x_in = int(x_in)
fizzBuzz(x_in)