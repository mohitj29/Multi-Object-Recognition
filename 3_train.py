import numpy as np
import torch
traindata =np.load("C:/Users/mohit/Desktop/20nump.npy")
trainlabel =np.load("C:/Users/mohit/Desktop/20classes.npy")

traindata = torch.from_numpy(traindata)
trainlabel = torch.from_numpy(trainlabel)


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



net = AlexNet()


import time
import random

import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=1e-3, momentum=0.1)


for epoch in range(15):  # loop over the dataset multiple times

    running_loss = 0.0
    for i in range(3800):
        #print(time.clock())
#         b=myrand()
#         b = torch.LongTensor(b)
#        b=torch.randperm(32)
        #print(i)
        j=random.randint(1,3800)
        inputs = traindata[j:(j+2),:,:,:] 
        
        # get the inputs
        labels = trainlabel[j:(j+2)]
#         print (labels)
        # wrap them in Variable
#         labels =np.asarray(labels)
        labels = Variable(labels.long()-1)
        inputs = inputs.float()
        inputs = Variable(torch.FloatTensor(inputs))
        #print(inputs)
#         inputs, labels = Variable(inputs.long()), Variable(labels)

        # zero the parameter gradients
        optimizer.zero_grad()
#         print(inputs)
        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
       # break
        #print("pp")
        # print statistics
        running_loss += loss.data[0]
        if i % 200 == 199:    
            
            print('hhh[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 200))
            running_loss = 0.0
            torch.save(net,"C:/Users/mohit/Desktop/jmdjmd.pth")
        #break
        #print(time.clock())
    #break
torch.save(net,"C:/Users/mohit/Desktop/jmdjmd.pth")

print('Finished Training')
