"""
This module contains routes for handling image data, including uploading images for classification.
"""

import io
import os
import base64
import bson
import requests
import pymongo.errors
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from PIL import Image, UnidentifiedImageError
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
user = os.environ["MONGO_INITDB_ROOT_USERNAME"]
passw = os.environ["MONGO_INITDB_ROOT_PASSWORD"]
uri = f"mongodb://{user}:{passw}@db:27017/db?authSource=admin"

# instantiate the app
app = Flask(__name__)

# connect to the database
client = MongoClient(uri, server_api=ServerApi("1"))
db = client["project4"]
images = db["images"]

# the following try/except block is a way to verify that the database connection is alive (or not)
try:
    # verify the connection works by pinging the database
    client.admin.command("ping")  # The ping command is cheap and does not require auth.
    print(" *", "Connected to MongoDB!")  # if we get here, the connection worked!
except pymongo.errors.ConnectionFailure as e:
    # the ping command failed, so the connection is not available.
    print(" * MongoDB connection error:", e)  # debug


@app.route("/")
def home():
    """
    Route for the home page
    """
    return render_template("index.html")  # render the home template


@app.route("/upload", methods=["POST"])
def upload():
    """
    Route for classifying an uploaded image.
    """
    # Check if the request contains an image
    if "image" not in request.files:
        return jsonify({"error": "No image provided in the request."}), 400

    try:
        # open the uploaded image file
        file = request.files["image"]
        image = Image.open(file)
    except UnidentifiedImageError:
        return jsonify({"error": "Invalid image format."}), 400

    # convert RGBA image to RGB
    if image.mode == "RGBA":
        image = image.convert("RGB")

    # determine the image format from the file extension
    image_format = file.content_type.split("/")[-1].upper()

    # convert PIL Image to binary format for classification
    buffer = io.BytesIO()
    image.save(buffer, format=image_format)
    image_binary = buffer.getvalue()
    image_base64 = base64.b64encode(image_binary).decode("utf-8")

    response = requests.post(
        "http://machine-learning-client:5002/classify",
        json={"image": image_base64},
        timeout=10,
    )

    if response.status_code != 200:
        return jsonify({"error": "Failed to process the image."}), 500
    result = response.json()

    # save image and classification to MongoDB
    doc = {"image_data": bson.binary.Binary(image_binary), "classification": result}
    images.insert_one(doc)

    # return JSON response with image data and classification
    return jsonify(result)


# run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
