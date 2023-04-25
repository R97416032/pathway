import os

import numpy as np
import pandas as pd
import re
file=open("./data/pathway.txt",'r')
lines=file.readlines()
file.close()
data=[]
nameA=""
nameB=""
nameC=""

for line in lines:
    data=line.strip('\n').split()
    index=data[0].strip()
    if(re.split('[0-9]',index)[0]=="A"):
        nameA=""
        for i in data[1:]:
            nameA=nameA+" "+i
        nameA=index[1:]+" "+nameA.replace(": "," ")
        if not os.path.exists("./data/"+nameA):
            os.makedirs("./data/"+nameA)
    elif(re.split('[0-9]',index)[0]=="B"):
        nameB = ""
        for i in data[2:]:
            nameB=nameB+" "+i
        nameB = data[1]+nameB.replace(": "," ")
        if not os.path.exists("./data/" + nameA+"/"+nameB):
            os.makedirs("./data/" + nameA+"/"+nameB)
    elif(re.split('[0-9]',index)[0]=="C"):
        nameC = ""
        for i in data[2:]:
            nameC=nameC+" "+i
        nameC="has"+data[1] +nameC.replace("："," ")
        nameC=nameC.replace("/","")
        nameC=nameC.replace("-","")
        if nameC.find('[')>-1:
            nameC=nameC[:nameC.find('[')]
        # file=open("./data/" + nameA+"/"+nameB+"/"+nameC+".txt",'w')
        # file.close()
    elif(re.split('[0-9]',index)[0]=="D"):
        file = open("./data/" + nameA + "/" + nameB + "/" + nameC + ".txt", 'a',encoding='utf-8')
        file.write(data[1]+" "+data[2]+'\n')
        file.close()
