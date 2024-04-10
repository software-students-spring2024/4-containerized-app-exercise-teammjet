from unittest import TestCase
from PIL import Image
import os
import sys
import pytest
#read a file from another folder
sys.path.append('../4-containerized-app-exercise-teammjet/machine-learning-client/')
import classification
buffer = classification.io.BytesIO()

class AppTests(TestCase):#do not need to house test functions inside class, only need to execute command pytest from inside test
    #folder and make sure all test functions and test files are prefixed with test_

    def test_chair_fancy(self):
        image = Image.open("tests/chair_fancy.jpg")
        image.save(buffer, format="jpeg")
        result = classification.convert_img(buffer)
        assert result == 'chair'

    def test_chair(self):
        image = Image.open("tests/chair.jpg")
        image.save(buffer, format="jpeg")
        result = classification.convert_img(buffer)
        assert result == 'chair'

    def clock_soendrum(self):
        image = Image.open("tests/clock_soendrum.jpg")
        image.save(buffer, format="jpeg")
        result = classification.convert_img(buffer)
        assert result == 'clock'
    
    def guitar(self):
        image = Image.open("tests/guitar.jpg")
        image.save(buffer, format="jpeg")
        result = classification.convert_img(buffer)
        assert result == 'guitar'

    def table_sample(self):
        image = Image.open("tests/table_sample.jpg")
        image.save(buffer, format="jpeg")
        result = classification.convert_img(buffer)
        assert result == 'desk'


#pytest.main()