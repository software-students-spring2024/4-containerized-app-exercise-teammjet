# code from learnopencv tutorial
import io
import base64
import torch
import io
dir(models)
#establish alexnet model
alexnet = models.alexnet(pretrained = True)

#create transform
from torchvision import transforms
transform = transforms.Compose([            #[1]
 transforms.Resize(256),                    #[2]
 transforms.CenterCrop(224),                #[3]
 transforms.ToTensor(),                     #[4]
 transforms.Normalize(                      #[5]
 mean=[0.485, 0.456, 0.406],                #[6]
 std=[0.229, 0.224, 0.225]                  #[7]
 )])

#get image and batch(not sure what batch is)
from PIL import Image
from flask_cors import CORS
from flask import Flask, request, jsonify
from torchvision import models, transforms

dir(models)
app = Flask(__name__)
CORS(app)
# establish alexnet model
alexnet = models.alexnet(pretrained=True)

# create transform
transform = transforms.Compose(
    [  # [1]
        transforms.Resize(256),  # [2]
        transforms.CenterCrop(224),  # [3]
        transforms.ToTensor(),  # [4]
        transforms.Normalize(  # [5]
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]  # [6]  # [7]
        ),
    ]
)


def convert_img(image: io.BytesIO):
    """
    Convert a given image in BytesIO format to a format suitable for evaluation.
    """
    image_binary = image.getvalue()
    image = Image.open(io.BytesIO(image_binary))
    return evaluate(image)


def evaluate(img):
    """
    Evaluate the given image using a pre-trained model.
    """
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)

    # evaluate
    alexnet.eval()
    out = alexnet(batch_t)
    print(out.shape)

    # parsing the result
    with open("imagenet_classes.txt", encoding="utf-8") as f:
        classes = [line.strip() for line in f.readlines()]

    _, indices = torch.sort(out, descending=True)

    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    print([(classes[idx], percentage[idx].item()) for idx in indices[0][:5]])
    arr = [(classes[idx], percentage[idx].item()) for idx in indices[0][:5]]
    return arr


@app.route("/classify", methods=["POST"])
def handle_req():
    """
    Route for handling the classification request.
    """
    # retrieve JSON data and extract the base64 encoded image
    data = request.get_json()
    image_base64 = data.get("image")
    image_binary = base64.b64decode(image_base64)

    # open the image using PIL and evaluate it
    image = Image.open(io.BytesIO(image_binary))
    result = evaluate(image)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)


