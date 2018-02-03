
# coding: utf-8

# In[2]:


from PIL import Image
import os
Open_text = open("C:/Users/mohit/Desktop/deep.txt", "r")
Read_text = Open_text.read()
#Remove_lines = Read_text.replace("\n","\t")
print(Read_text)


# In[54]:


Remove_tabs = Read_text.split("\n")
print(len(Remove_tabs[1]))


# In[3]:


count = 0
top =[]

Remove_tabs = Read_text.split("\n")
for i in range(len(Remove_tabs)):
    blist = []
    count += 1
    #print(count)
    if Remove_tabs[i] == '':
        pass
    else:
        d=Remove_tabs[i][1:-2].split("] [")
        
        for o in d:
            o = o.replace(" ","")
            k=o.split(",")
            lis  = []
            for mj in k:
                
               # print(mj)
                lis.append(int(mj))
            #print(lis)
            blist.append(lis)
    top.append(blist)
    


# In[116]:


jo15sejada = []
for i in range(len(top)):
    #print(len(top[i]))
    
    if len(top[i])>15:
        jo15sejada.append(i)
print(jo15sejada)
write_name = "jo15sejada.txt"    #naming the file 
write_file = open(write_name, "w")         
for i in jo15sejada: #creating a loop to write
    write_file.write(str(i)+ "\n")  # writing the numbers so have to convert into string
    #write_file.write( "\n")
write_file.close()  #closing the file           
#Open_text.close() #closing the file            

       


# In[14]:


from PIL import Image
import numpy as np
import os
Open_text = open("C:/Users/mohit/Desktop/jaimatadi.txt", "r")
Read_text = Open_text.read()
#Remove_lines = Read_text.replace("\n","\t")
Remove_tabs = Read_text.split("\n")
count = 0
pit = 0
jo15_95sejada =[]
Convert1 = []
for i in range(len(Remove_tabs)):
    Convert1.append(Remove_tabs[i])
for i in range(len(Convert1)):
    if len(top[i])>15:
        try:
            img = Image.open("C:/Users/mohit/Desktop/deepl/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/JPEGImages/%s" %Convert1[i])
            #print(Convert1[i])
            for y in range(15):
               # print(i,y)
                x1 = int(top[i][y][0])
                y1 = int(top[i][y][1])
                x2 = int(top[i][y][2])
                y2 = int(top[i][y][3])
                x2 = x1+x2
                y2 = y1+y2
                box = (x1,y1,x2,y2)
                cropped=img.crop(box)
                
                l,k = cropped.size

                if l >95 and k>95:
                    #print("jj")
                    jo15_95sejada.append(i)
                    cropped = cropped.resize((227, 227), Image.NEAREST)
                    #cropped = np.transpose(cropped, (2, 0, 1))
                    
                    name = str(i)+"_"+str(y)
                    cropped.save("C:/Users/mohit/Desktop/learnimagedeep/%s.jpeg" %name)
                    count +=1
        except Exception:
            pit +=1
                
print(count,pit)


# In[25]:


write_name = "C:/Users/mohit/Desktop/jo15_95sejada.txt"    #naming the file 
write_file = open(write_name, "w")         
for i in jo15_95sejada: #creating a loop to write
    print(i)
    write_file.write(str(i)+ "\n")  # writing the numbers so have to convert into string
    #write_file.write( "\n")
write_file.close()  #closing the file           
#Open_text.close() #closing the file   

