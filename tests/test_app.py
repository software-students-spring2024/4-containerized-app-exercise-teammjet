from unittest import TestCase

class AppTests(TestCase):#do not need to house test functions inside class, only need to execute command pytest from inside test
    #folder and make sure all test functions and test files are prefixed with test_
    def test_Test(self):
        x = 3
        assert x == 3


