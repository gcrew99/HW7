#Gabriel Crew
import unittest 
import code

class TestCase(unittest.TestCase):
  def test1(self): self.assertEqual(fizzBuzz(3),"1,2,Fizz")
  def test2(self): self.assertEqual(fizzBuzz(5),"1,2,Fizz,4,Buzz")
  def test3(self): self.assertEqual(fizzBuzz(15),"1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,")


if __name__ == '__main__':
  unittest.main()