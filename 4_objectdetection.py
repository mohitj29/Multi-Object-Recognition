
# coding: utf-8

# In[27]:


from __future__ import (
    division,
    print_function,
)

import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch
import os


def main():
    lis = []
    Open_text = open("C:/Users/mohit/Desktop/jaimatadi.txt", "r")
    Read_text = Open_text.read()
    #Remove_lines = Read_text.replace("\n","\t")
    Remove_tabs = Read_text.split("\n")
    Convert = []
    for i in range(len(Remove_tabs)):
        Convert.append(Remove_tabs[i])
    for i in range(len(Convert)):
        # loading astronaut image
        try:
            if os.path.isfile("C:/Users/mohit/Desktop/deepl/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/JPEGImages/%s" %Convert[i]):
                img = skimage.data.load("C:/Users/mohit/Desktop/deepl/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/JPEGImages/%s" %Convert[i])

                # perform selective search
                img_lbl, regions = selectivesearch.selective_search(
                    img, scale=500, sigma=0.9, min_size=10)

                candidates = set()
                p =[]
                for r in regions:
                    # excluding same rectangle (with different segments)
                    if r['rect'] in candidates:
                        continue
                    # excluding regions smaller than 2000 pixels
                    if r['size'] < 2000:
                        continue
                    # distorted rects
                    x, y, w, h = r['rect']
                    if w / h > 1.2 or h / w > 1.2:
                        continue
                    candidates.add(r['rect'])

                    p.append([x,y,w,h])
                lis.append(p)
        except Exception:
            print("Exception Occurred")
    # draw rectangles on the original image
    write_name = "deep.txt"    #naming the file 
    write_file = open(write_name, "w")         
    for i in lis: #creating a loop to write
        for j in i:
            write_file.write(str(j)+ " ")  # writing the numbers so have to convert into string
        write_file.write( "\n")
    write_file.close()  #closing the file           
    Open_text.close() #closing the file
    
   
    

if __name__ == "__main__":
    main()
    


# In[14]:


print(lis)


# In[21]:


from __future__ import (
    division,
    print_function,
)

import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch

Convert = []

def main():
    lis = []
    Open_text = open("C:/Users/mohit/Desktop/jaimatadi.txt", "r")
    Read_text = Open_text.read()
    #Remove_lines = Read_text.replace("\n","\t")
    Remove_tabs = Read_text.split("\n")
    for i in range(len(Remove_tabs)):
        Convert.append(Remove_tabs[i])
        
if __name__ == "__main__":
    main()
    


# In[22]:


Convert

