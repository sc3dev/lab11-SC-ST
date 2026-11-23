import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertAlmostEqual(add(3.1, 2.1), 5.2)
        self.assertAlmostEqual(add(49, -10.1), 38.9)
        self.assertAlmostEqual(add(-15, -0.3), -15.3)

    # def test_subtract(self): # 3 assertions
    def test_subtract(self):
        self.assertAlmostEqual(subtract(4, 4), 0)
        self.assertAlmostEqual(subtract(3.5, 7.6), -4.1)
        self.assertAlmostEqual(subtract(-10.1, -10.7), 0.6)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(5, 25), 2)
        self.assertAlmostEqual(logarithm(25, 5), 0.5)
        self.assertAlmostEqual(logarithm(10, 0.01), -2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 14348907.3)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
