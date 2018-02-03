from PIL import Image
import os
Open_text = open("C:/Users/mohit/Desktop/jaimatadi.txt", "r")
Read_text = Open_text.read()
#Remove_lines = Read_text.replace("\n","\t")
Remove_tabs = Read_text.split("\n")
count = 0
pit = 0
Convert1 = []
for i in range(len(Remove_tabs)):
    Convert1.append(Remove_tabs[i])
for i in range(len(Convert1)):
    try:
        img = Image.open("C:/Users/mohit/Desktop/deepl/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/JPEGImages/%s" %Convert1[i])
        #print(Convert1[i])
        for y in range(len(top[i])):
            x1 = int(top[i][y][1][0])
            y1 = int(top[i][y][1][1])
            x2 = int(top[i][y][1][2])
            y2 = int(top[i][y][1][3])
            box = (x1,y1,x2,y2)
            cropped=img.crop(box)
            directory = "C:/Users/mohit/Desktop/imagedeep/%s"%top[i][y][0]
            if not os.path.exists(directory):
                os.makedirs(directory)
            count +=1

            cropped.save("C:/Users/mohit/Desktop/imagedeep/%s/%s.jpeg" %(top[i][y][0],count))
    except Exception:
            pit +=1
