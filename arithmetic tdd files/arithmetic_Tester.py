import unittest
from arithm import solution

class TestSolution(unittest.TestCase):
    def test_addition(self):
        self.assertTrue(solution(10,20,"+"),30)
    def test_subtraction(self):
        self.assertTrue(solution(35,15,"-"),20)
    def test_multiplication(self):
        self.assertTrue(solution(45,10,"*"),450)
    def test_division(self):
    	self.assertTrue(solution(36,6,"/"),6)
    def test_remainder(self):
    	self.assertTrue(solution(23,2,"%"),1)

if __name__ == '__main__':
	unittest.main()