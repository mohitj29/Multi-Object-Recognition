
# coding: utf-8

# In[35]:


Open_text = open("C:/Users/mohit/Desktop/ann.txt", "r")
Read_text = Open_text.read()
Remove_lines = Read_text.replace("'","")
Remove_tabs = Read_text.split("\n")
Convert = []
for i in range(len(Remove_tabs)):
    Convert.append(Remove_tabs[i])
top  = []
import xml.etree.ElementTree as ET
for i in range(len(Convert)):
    if i in jo15_95sejada:
        tree = ET.parse('C:/Users/mohit/Desktop/deepl/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/Annotations/%s'%Convert[i])
        root = tree.getroot()

        allobject = []
        for child in root:  
            oneobj =[]

            if child.tag == 'object':                    
                    for p in child:
                        if p.tag == 'name':
                            #print(p.text)
                            oneobj.append(p.text)


                    allobject.append(oneobj)
        top.append(allobject)
print(top)


# In[53]:


print(top[0][0][0])


# In[57]:


alltestlabel = []
for i in range(len(top)):
    classes = []
    for y in range(len(top[i])):
        if top[i][y][0] == 'person':
            classes.append(1)
        if top[i][y][0] == 'aeroplane':
            classes.append(2)
        if top[i][y][0] == 'bicycle':
            classes.append(3)
        if top[i][y][0] == 'bird':
            classes.append(4)
        if top[i][y][0] == 'boat':
            classes.append(5)
        if top[i][y][0] == 'bottle':
            classes.append(6)
        if top[i][y][0] == 'bus':
            classes.append(7)
        if top[i][y][0] == 'car':
            classes.append(8)
        if top[i][y][0] == 'cat':
            classes.append(9)
        if top[i][y][0] == 'chair':
            classes.append(10)
        if top[i][y][0] == 'cow':
            classes.append(11)
        if top[i][y][0] == 'diningtable':
            classes.append(12)
        if top[i][y][0] == 'dog':
            classes.append(13)
        if top[i][y][0] == 'horse':
            classes.append(14)
        if top[i][y][0] == 'motorbike':
            classes.append(15)
        if top[i][y][0] == 'pottedplant':
            classes.append(16)
        if top[i][y][0] == 'sheep':
            classes.append(17)
        if top[i][y][0] == 'sofa':
            classes.append(18)
        if top[i][y][0] == 'train':
            classes.append(19)
        if top[i][y][0] == 'tvmonitor':
            classes.append(20)
        alltestlabel.append(classes)


# In[58]:


print(alltestlabel)


# In[59]:


write_name = "C:/Users/mohit/Desktop/jo15_95sejadalabel.txt"    #naming the file 
write_file = open(write_name, "w")         
for i in alltestlabel: #creating a loop to write
    for j in i:
        write_file.write(str(j)+ " ")  # writing the numbers so have to convert into string
    write_file.write( "\n")
write_file.close()  #closing the file           
Open_text.close() #closing the file            



# In[16]:


Open_text = open("C:/Users/mohit/Desktop/jo15_95sejada.txt", "r")
Read_text = Open_text.read()
#Remove_lines = Read_text.replace("\n","\t")
Remove_tabs = Read_text.split("\n")
jo15_95sejada = []
for i in range(len(Remove_tabs)):
    #print(i)
    jo15_95sejada.append(int(Remove_tabs[i]))


# In[17]:


print(jo15_95sejada)

