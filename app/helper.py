import torchvision.transforms as transforms
from torchvision import torch
from torch.cuda.amp import  autocast
import torch.nn as nn
from PIL import Image
import timm
import io



IMG_PATH =''
W_PATH = '/usr/src/app/app/weights/ayur_model_weights.pth'
EMBEDDING_SIZE = 1280
NUM_CLASSES = 6
CLASS_LABEL =["Ashwagandha", "Cardmon", "Cumin", "Neem","Rama Tulsi","Turmeric"]


# The `EffNet` class is a PyTorch module that implements an EfficientNet model with a custom
# classifier for a specified number of classes and embedding size.

class EffNet(nn.Module):
    def __init__(self, num_classes, embedding_size):
        super(EffNet, self).__init__()
        self.num_classes = num_classes
        self.embedding_size = embedding_size
        self.backbone = timm.create_model(
            'efficientnet_b1',
            pretrained=True,
            num_classes=self.num_classes
        )

        self.backbone.classifier = nn.Sequential(
            nn.Linear(self.embedding_size, 256),
            nn.BatchNorm1d(256),
            nn.PReLU(),
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.PReLU(),
            nn.Linear(128, self.num_classes)
        )

    def forward(self, x):
        return self.backbone(x)
    


def convert_4_channel_to_3_channel(image):
    """
    Convert 4-channel RGBA image to 3-channel RGB image
    """
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    return image

my_transforms = transforms.Compose([
        transforms.Lambda(convert_4_channel_to_3_channel),
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def predict(img):
    """
    The `predict` function takes an image as input, loads a pre-trained model, processes the image, and
    returns the predicted class label for the image.
    
    :param img: The `img` parameter is the input image that you want to make predictions on. It should
    be a byte array representing the image data
    :return: the predicted class label for the input image.
    """
    if torch.cuda.is_available():
        DEVICE = torch.device(type='cuda')
    else:
        DEVICE = torch.device('cpu')


    model= EffNet(num_classes=NUM_CLASSES, embedding_size=EMBEDDING_SIZE)
    model.load_state_dict(torch.load(W_PATH,map_location=torch.device(DEVICE)))
    image = Image.open(io.BytesIO(img))
    image = my_transforms(image)

    model.to(DEVICE)
    model.eval()


    with torch.inference_mode():
        
        image = image.to(DEVICE)
        image = image.unsqueeze(0)
        with autocast():
            logits = model.forward(image)

            y_pred = torch.softmax(logits, dim=1).argmax(dim=1).detach().cpu()

    return CLASS_LABEL[y_pred.item()]