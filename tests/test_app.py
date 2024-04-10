from unittest import TestCase
from PIL import Image

class AppTests(TestCase):#do not need to house test functions inside class, only need to execute command pytest from inside test
    #folder and make sure all test functions and test files are prefixed with test_
    def test_Test(self):
        x = 3
        assert x == 3

    def test_chair_fancy(self):
        pass 

    def test_char(self):
        pass

    def clock_soendrum(self):
        pass
    
    def guitar(self):
        pass

    def table_sample(self):
        img = Image.open("table_sample.jpg")
        
        pass

