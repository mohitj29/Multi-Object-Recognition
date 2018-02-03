import numpy as np
testdata =np.load("C:/Users/mohit/Desktop/testimagenumpy.npy")
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
class AlexNet(nn.Module):

    def __init__(self, num_classes=20):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), 256 * 6 * 6)
        x = self.classifier(x)
        return x
import torch
net = torch.load("C:/Users/mohit/Desktop/jmdjmd.pth")
allprediction = []
for i in range(0,5000,100):
    p=torch.FloatTensor(testdata[i:i+100,:,:,:])
    print(p.size())
    outputs = net(Variable(p))
    _, predicted = torch.max(outputs.data, 1)
    allprediction.extend(predicted)
	
predlis = []
for i in range(len(allprediction)):
    predlis.append(allprediction[i][0])

Open_text = open("C:/Users/mohit/Desktop/jo15_95sejadalabel.txt", "r")
Read_text = Open_text.read()
#Remove_lines = Read_text.replace("\n","\t")
Remove_tabs = Read_text.split("\n")
x= [ list(map(int,line.split(' ')[:-1])) for line in Remove_tabs]
cpt =0
success = 0
loss = 0
for i in range(0,5000,15):
    for j in range(15):
        if i+j <5000:
            testclass =predlis[i+j]+1
            if testclass in x[cpt]:
                success +=1
            else:
                loss +=1
    cpt+=1
