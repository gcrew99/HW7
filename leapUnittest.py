#Gabriel Crew
import unittest 
import leapYear

class TestCase(unittest.TestCase):
  def test1(self): self.assertEqual(leapYear(4),"Leap Year")


if __name__ == '__main__':
  unittest.main()