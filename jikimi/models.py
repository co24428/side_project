import torch
import torch.nn as nn
import torchvision.models as models

class ResNet18Classifier(nn.Module):
    def __init__(self, num_classes=11):
        super(ResNet18Classifier, self).__init__()
        self.model = models.resnet18(pretrained=True)
        
        # Modify the final layer to output the desired number of classes
        self.model.fc = nn.Linear(self.model.fc.in_features, num_classes)

    def forward(self, x):
        return self.model(x)
    
class MobileNetv2Classifier(nn.Module):
    def __init__(self, num_classes=11):
        super(MobileNetv2Classifier, self).__init__()
        self.model = models.mobilenet_v2(pretrained=True)
        
        # Modify the final layer in MobileNetV2 to output the desired number of classes
        self.model.classifier[1] = nn.Linear(self.model.classifier[1].in_features, num_classes)

    def forward(self, x):
        return self.model(x)
    
class EfficientNetB0Classifier(nn.Module):
    def __init__(self, num_classes=11):
        super(EfficientNetB0Classifier, self).__init__()
        self.model = models.efficientnet_b0(pretrained=True)
        
        # Modify the final layer in EfficientNet B0 to output the desired number of classes
        self.model.classifier[1] = nn.Linear(self.model.classifier[1].in_features, num_classes)

    def forward(self, x):
        return self.model(x)