import os
import pandas as pd

rootpath="./data/"
#生成每个次类别中通路中的基因频次表，行为通路名，列为基因名
listA=os.listdir(rootpath)[0:-2]
print(listA)
for i in listA:
    path=rootpath+i+'/'
    listB=os.listdir(path)
    pathways = []
    genenames = []
    for j in listB:

        pathC=path+j+'/'
        filenames=os.listdir(pathC)
        for k in filenames:
            pathways.append(k[:-4])
        print(pathways)
