import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from torchvision import transforms
from model import ResNet18Classifier

def load_model(model_path, num_classes=10):
    model = ResNet18Classifier(num_classes=num_classes)
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0)  # Add batch dimension
    return image

def imshow(inp, title=None):
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)

def main():
    model_path = 'resnet18_classifier.pth'
    image_path = 'data/split_dataset/test/6/4digits_62_0.png'  # 테스트할 이미지 파일 경로
    num_classes = 10

    # 모델 로드
    model = load_model(model_path, num_classes=num_classes)

    # 이미지 전처리
    image = preprocess_image(image_path)

    # 디바이스 설정
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    image = image.to(device)

    # 예측 수행
    with torch.no_grad():
        outputs = model(image)
        _, preds = torch.max(outputs, 1)
        prediction = preds.item()

    # 이미지 시각화
    image = image.cpu().squeeze(0)  # Remove batch dimension
    imshow(image, title=f'Predicted: {prediction}')

    plt.show()

if __name__ == '__main__':
    main()