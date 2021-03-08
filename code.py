def fizzBuzz(x):
      string = ""
      for i in range(x):
        i = i +1
        if (i%3 == 0): 
          string = string + "Fizz,"
        else:
            i_str = str(i)
            string = string + i_str + ","
      return string

x_in = input("Type number from 1 to 100  ")
x_in = int(x_in)
fizzBuzz(x_in)
