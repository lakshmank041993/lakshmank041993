import unittest
from p1_roman_to_interger import Roman_to_interger

class TestRomeToInterger(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Roman_to_interger.convert(self,"III"),3,"value doesnot match expected is 3")
    
    def test_2(self):
        self.assertEqual(Roman_to_interger.convert(self,"X"),10,"value doesnot match expected is 10") 
    
    def test_3(self):
        self.assertEqual(Roman_to_interger.convert(self,"LVIII"),58,"value doesnot match expected is 10")
    
    def test_4(self):
        self.assertEqual(Roman_to_interger.convert(self,"MCMXCIII"),1993,"value doesnot match expected is 10")

    def test_5(self):
        self.assertEqual(Roman_to_interger.convert(self,"MCMXCIII"),1993,"value doesnot match expected is 10")

if __name__=='__main__':
	unittest.main()