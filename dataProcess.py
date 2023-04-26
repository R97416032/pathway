import os
import pandas as pd
import csv
rootpath="./data/"
#生成每个B类别中通路中的基因频次表，行为通路名，列为基因名
listA=os.listdir(rootpath)[0:-2]
for i in listA:
    path=rootpath+i+'/'
    listB=os.listdir(path)
    pathways = []

    for j in listB:
        genenames = ['pathway']
        pathC=path+j+'/'
        filenames=os.listdir(pathC)
        dictB={}
        for k in filenames:
            pathways.append(k[:-4])
            genefile=open(pathC+k,'r')
            temp=[]
            for g in genefile.readlines():
                genenames.append(g.strip('\n'))
                temp.append(g.strip('\n'))
            dictB[k[:-4]]=temp
        genenames=sorted(set(genenames),key=genenames.index)
        if not os.path.exists("./csv/"+i+'/'+j ):
            os.makedirs("./csv/"+i+'/'+j)
        with open("./csv/"+i+'/'+j+"/"+j+".csv", "w",newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(genenames)
            for key in dictB.keys():
                temp=[key]
                for g in genenames[1:]:
                    if g in dictB[key]:
                        temp.append(1)
                    else:
                        temp.append((0))
                writer.writerow(temp)
#生成每个A类别中通路中的基因频次表，行为通路名，列为基因名
for i in listA:
    path=rootpath+i+'/'
    listB=os.listdir(path)
    pathways = []
    genenames = ['pathway']
    dictB = {}
    for j in listB:
        pathC=path+j+'/'
        filenames=os.listdir(pathC)
        for k in filenames:
            pathways.append(k[:-4])
            genefile=open(pathC+k,'r')
            temp=[]
            for g in genefile.readlines():
                genenames.append(g.strip('\n'))
                temp.append(g.strip('\n'))
            dictB[k[:-4]]=temp
    genenames=sorted(set(genenames),key=genenames.index)
    if not os.path.exists("./csv/"+i ):
        os.makedirs("./csv/"+i)
    with open("./csv/"+i+'/'+i+".csv", "w",newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(genenames)
        for key in dictB.keys():
            temp=[key]
            for g in genenames[1:]:
                if g in dictB[key]:
                    temp.append(1)
                else:
                    temp.append((0))
            writer.writerow(temp)