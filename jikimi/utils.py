import os
import shutil
from sklearn.model_selection import train_test_split
from torchvision import datasets, transforms
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np
import torch
import models

def load_model(model_path, model_type='MobileNetV2', num_classes=11):
    if model_type == 'MobileNetV2':
        model = models.MobileNetV2Classifier(num_classes=num_classes)
    elif model_type == 'ResNet18':
        model = models.ResNet18Classifier(num_classes=num_classes)
    elif model_type == 'EfficientNetB0':
        model = models.EfficientNetB0Classifier(num_classes=num_classes)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")
    
    # 모델의 가중치를 로드
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

def split_data(data_dir, output_dir, val_size=0.2, test_size=0.1):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for class_name in os.listdir(data_dir):
        class_dir = os.path.join(data_dir, class_name)
        if os.path.isdir(class_dir):
            images = os.listdir(class_dir)
            train_val_images, test_images = train_test_split(images, test_size=test_size, random_state=42)
            train_images, val_images = train_test_split(train_val_images, test_size=val_size, random_state=42)
            
            train_class_dir = os.path.join(output_dir, 'train', class_name)
            val_class_dir = os.path.join(output_dir, 'val', class_name)
            test_class_dir = os.path.join(output_dir, 'test', class_name)
            os.makedirs(train_class_dir, exist_ok=True)
            os.makedirs(val_class_dir, exist_ok=True)
            os.makedirs(test_class_dir, exist_ok=True)
            
            for img in train_images:
                shutil.copy(os.path.join(class_dir, img), os.path.join(train_class_dir, img))
            for img in val_images:
                shutil.copy(os.path.join(class_dir, img), os.path.join(val_class_dir, img))
            for img in test_images:
                shutil.copy(os.path.join(class_dir, img), os.path.join(test_class_dir, img))

def get_dataloaders(data_dir, batch_size=32):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    train_dataset = datasets.ImageFolder(root=os.path.join(data_dir, 'train'), transform=transform)
    val_dataset = datasets.ImageFolder(root=os.path.join(data_dir, 'val'), transform=transform)
    test_dataset = datasets.ImageFolder(root=os.path.join(data_dir, 'test'), transform=transform)

    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    return train_loader, val_loader, test_loader