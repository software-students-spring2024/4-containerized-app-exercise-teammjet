import pytest
from pytest_mock import MockFixture
from app import app as web_app
from PIL import Image
from io import BytesIO
@pytest.fixture
def client():
    web_app.config.update({"TESTING": True})

    with web_app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200

def test_upload(client):
    # Open the stored image
    with open("test-images/guitar.jpg", "rb") as img:
        image = Image.open(img)
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        
        # Save the converted image to a buffer
        buffer = BytesIO()
        image.save(buffer, format='JPEG')
        buffer.seek(0)
        
        data = {
            'image': (buffer, 'guitar.jpg')
        }
        # Send POST request with the image
        response = client.post('/upload', data=data, content_type='multipart/form-data')

        # Check the status code
        assert response.status_code == 200

        # Optionally check the response content if specific outputs are expected
        response_data = response.json
        assert 'image_data' in response_data  # Add further checks based on expected response

