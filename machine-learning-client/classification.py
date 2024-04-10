#code from learnopencv tutorial 
from torchvision import models 
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
img = Image.open("table_sample.jpg")
img_t = transform(img)
batch_t = torch.unsqueeze(img_t,0)

    #evaluate
    alexnet.eval()
    out = alexnet(batch_t)
    print(out.shape)

#parsing the result
with open('imagenet_classes.txt') as f:
    classes = [line.strip() for line in f.readlines()]

    _, index = torch.max(out, 1)
 
percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
print(classes[index[0]], percentage[index[0]].item())
