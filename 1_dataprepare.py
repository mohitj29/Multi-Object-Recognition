Open_text = open("C:/Users/mohit/Desktop/ann.txt", "r")
Read_text = Open_text.read()
#Remove_lines = Read_text.replace("\n","\t")
Remove_tabs = Read_text.split("\n")
Convert = []
for i in range(len(Remove_tabs)):
    Convert.append(Remove_tabs[i])
top  = []
import xml.etree.ElementTree as ET
for i in range(len(Convert)):
    tree = ET.parse('C:/Users/mohit/Desktop/deepl/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/Annotations/%s'%Convert[i])
    root = tree.getroot()
    
    allobject = []
    for child in root:  
        oneobj =[]
        
        if child.tag == 'object':                    
                for p in child:
                    if p.tag == 'bndbox':
                        bnd =[]
                        for sz in p:
                            bnd.append(sz.text)
                        bnd[2]=float(bnd[2])-float(bnd[0])
                        bnd[3]=float(bnd[3])-float(bnd[1])
                        
                        oneobj.append(bnd)
                    if p.tag == 'name':
                        oneobj.append(p.text)

            
                allobject.append(oneobj)
    top.append(allobject)
write_name = "anndeep.txt"    #naming the file 
write_file = open(write_name, "w")         
for i in top: #creating a loop to write
    for j in i:
        write_file.write(str(j)+ " ")  # writing the numbers so have to convert into string
    write_file.write( "\n")
write_file.close()  #closing the file           
Open_text.close() #closing the file            

