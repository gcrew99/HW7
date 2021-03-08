#Gabriel Crew
import unittest 
import leapYear

class TestCase(unittest.TestCase):
  def test1(self): self.assertEqual(leapYear(4),"Leap Year")
  def test2(self): self.assertEqual(leapYear(200),"Not Leap Year")
  def test3(self): self.assertEqual(leapYear(400),"Not Leap Year")

if __name__ == '__main__':
  unittest.main()