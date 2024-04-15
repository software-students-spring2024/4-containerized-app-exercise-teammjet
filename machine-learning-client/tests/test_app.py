from unittest import TestCase
from PIL import Image
import os
import pytest
import sys
#read a file from another folder
#sys.path.append('../4-containerized-app-exercise-teammjet/machine-learning-client/')
import classification #if you run pytest from test class, there will be a module import error
#run instead from project folder
buffer = classification.io.BytesIO()

class AppTests(TestCase):#do not need to house test functions inside class, only need to execute command pytest from inside test
    #folder and make sure all test functions and test files are prefixed with test_

    def test_chair_fancy(self):
        image = Image.open("machine-learning-client/tests/chair_fancy.jpg")
        image.save(buffer, format="jpeg")
        result = classification.convert_img(buffer)
        assert result[0][0] == 'folding chair'

    def test_chair(self):
        image = Image.open("machine-learning-client/tests/chair.jpg")
        image.save(buffer, format="jpeg")
        result = classification.convert_img(buffer)
        assert result[0][0] == 'folding chair'

    def test_clock_soendrum(self):
        image = Image.open("machine-learning-client/tests/clock_soendrum.jpg")
        image.save(buffer, format="jpeg")
        result = classification.convert_img(buffer)
        assert result[0][0] == 'clock'
    
    def test_guitar(self):
        image = Image.open("machine-learning-client/tests/guitar.jpg")
        image.save(buffer, format="jpeg")
        result = classification.convert_img(buffer)
        assert result[0][0] == 'guitar'

    def test_table_sample(self):
        image = Image.open("machine-learning-client/tests/table_sample.jpg")
        image.save(buffer, format="jpeg")
        result = classification.convert_img(buffer)
        assert result[0][0] == 'desk'

pytest.main()