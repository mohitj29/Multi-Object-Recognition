#                                        Multi-Object Recognition




![image](https://user-images.githubusercontent.com/27119316/35769914-a629b53e-08e0-11e8-9d6e-1cd441f0dbb3.png)

###Abstract

To perfume multi object recognition I used combination of 2 different algorithm. First, the object proposal algorithm and second the convolutional neural network classifier. For Object proposal, I used selective search and for convolutional neural network I used Alex net. To test and to train I used pascal visual object dataset which contain 17,125 Images.

           I. INTRODUCTION
  
In recent time, Alexnet[1] has showed very good result in respect to Image classification task and it still consider one of the good classifier but to perform multi object recognition we need to perform localization but Alex is only capable of Image classification.

![image](https://user-images.githubusercontent.com/27119316/35769925-d30b11ba-08e0-11e8-9ced-777a968d8ead.png)


So, to perform localization there are various algorithm we can use like edge boxes[3], selective search[2] etc. I am using selective search because it has shown good result in past in term of object proposal.

![image](https://user-images.githubusercontent.com/27119316/35769935-fcb10240-08e0-11e8-8150-7b2ba0826b53.png)


I will combine both the algorithm selective search and Alex net, to use it as object recognition system. Through selective search I will generate bounding box and then resize it to feed in the network for classification.

          Methodologies:

####Alex Net:

Alex net has 8 layers. The first 5 are convolutional and the last 3 are fully connected layers. In between we also have some ‘layers’ called pooling and activation.

Layer 1 is a Convolution Layer,

Input Image size is – 3 x 227 x 227, Number of filters – 64, Filter size – 11 x 11, Stride – 4

Layer 2 is a Convolution Layer,

Number of filters – 192, Filter size – 11 x 11, Stride – 4

Layer 3 is a Convolution Layer,

Number of filters – 384, Filter size – 11 x 11, Stride – 4

Layer 4 is a Convolution Layer,

Number of filters – 256, Filter size – 11 x 11, Stride – 4

Layer 5 is a Convolution Layer,

Number of filters – 256, Filter size – 11 x 11, Stride – 4

Layer 6 is a fully connected Layer with 4096 hidden units

Layer 7 is a fully connected Layer with 4096 hidden units

Layer 8 is a fully connected Layer with 20 hidden units


           Data preparation:

To train my network I used the VOC dataset which gives me dimensions and labels of the object. I cropped all the object using those dimensions and prepare it to feed to network, for that I only used those cropped images whose size is greater than 95x95 because I must resize all the images in 3x227x277 to feed in the network. So, if cropped Images are greater than 95x95 I will reshape them and feed it to network otherwise I will ignore them. After applying such a filter, I had 3800 Images to train my network. I had 20 classes which were:

• Person: person

• Animal: bird, cat, cow, dog, horse, sheep

• Vehicle: aero plane, bicycle, boat, bus, car, motorbike, train

• Indoor: bottle, chair, dining table, potted plant, sofa, tv/monitor


           Training process:

I used 3800 images of 3x277x277 size to feed in network I randomly initialized the weights to train addition to that I randomly feed the images from the dataset and run 15 epochs to reduce the loss. Loss started from 2.786 and after 10 epochs it reduced to 0.437.


           Testing Process:

Now, once the model is trained. It’s time to prepare data for test. So, for that I used selective search algorithm to generate bounding boxes After having all the boxes, I cropped all the boxes from images and saved it.

Now I again prepared data to feed in the network so I applied same filter (cropped Images >95x95) on all the images and then reshape it in 3x227x227 to feed in network for the prediction.


           Results:


I have run the model over 5000 images and in which it got 1545 correctly recognized which gave me 30.9% of accuracy.

These are the few examples of correctly recognized Images.

![image](https://user-images.githubusercontent.com/27119316/35769944-1da7837a-08e1-11e8-80af-e1d949c42ba8.png)

Correct prediction: Cycle

![image](https://user-images.githubusercontent.com/27119316/35769949-24df3656-08e1-11e8-8c15-845abf63cc55.png)

Correct prediction: person


![image](https://user-images.githubusercontent.com/27119316/35769951-2871e3d6-08e1-11e8-9116-b821f7e25cf8.png)

Correct prediction: Chair

But as the accuracy is 30.9% there are many incorrectly classified Images also.


![image](https://user-images.githubusercontent.com/27119316/35769955-363f3928-08e1-11e8-887e-60d9369f712f.png)

Incorrect prediction: Cat


![image](https://user-images.githubusercontent.com/27119316/35769962-3aece2fe-08e1-11e8-8ef3-c6c7db83841d.png)

Incorrect prediction: Tv monitor


           Conclusion:


Apart from this due to the use of selective search there were many unnecessary boxes got generated which had no objects that could affected the performance. To improve the performance, we can do various things like:

1) Currently we are using 2 different algorithms, we can make one trainable end to end neural network to improve the performance.

2) We need a strategy to reduce the False positive.

3) Since I was training the model on CPU to generate the result I stopped the training on 10 epochs so with more computational power and by increase the training dataset we can improve the performance of the network.
References.

[1] Vedaldi, Andrea, and Karel Lenc. "Matconvnet: Convolutional neural networks for matlab." Proceedings of the 23rd ACM international conference on Multimedia. ACM, 2015.
[2] Uijlings, Jasper RR, et al. "Selective search for object recognition." International journal of computer vision 104.2 (2013): 154-171.
[3] Paszke, Adam, et al. "Pytorch: Tensors and dynamic neural networks in python with strong gpu acceleration, may 2017."
[4] Zitnick, C. Lawrence, and Piotr Dollár. "Edge boxes: Locating object proposals from edges." European Conference on Computer Vision. Springer, Cham, 2014.
