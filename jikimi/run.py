import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import utils
import argparse


def main(model_path):
    labels = ['1','2','3','4','5','6','7','8','9','n']
    
    for label in labels:
        image_path = './sample_data/' + label + '.png'  
        num_classes = 11
        
        if model_path == 'MobileNetv2Classifier.pth':
            model = utils.load_model(model_path, 'MobileNetV2', num_classes=num_classes)
        elif model_path == 'ResNet18Classifier.pth':
            model = utils.load_model(model_path, 'ResNet18', num_classes=num_classes)
        elif model_path == 'EfficientNetB0Classifier.pth':
            model = utils.load_model(model_path, 'EfficientNetB0', num_classes=num_classes)
        else:
            raise ValueError(f"Unsupported model: {model_path}")

        # 이미지 전처리
        image = utils.preprocess_image(image_path)

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
        utils.imshow(image, title=f'Predicted: {prediction}')

        plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the model with a specified path.")
    parser.add_argument('-m', '--model_path', type=str, required=True, help='Path to the model file')
    args = parser.parse_args()
    
    main(args.model_path)