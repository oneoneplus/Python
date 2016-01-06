#coding=utf-8
import re
qqDic={}
qqNumDic={}
qqNameList=[]
qqNumList=[]
myNumList=[]
numNamedic={}
myfile=open(u"d://python，消息记录.txt","r")
Content=myfile.readlines()
myfile.close()

for i in Content: 
    i=i.decode("utf-8").encode("gbk","ignore")
    #print i+"****"
    if i.find("201")==0 and i.find("-")>0 and i.find(":")>0 and (i.find("(")>0 and i.find(")")>0) or (i.find("<")>0 and i.find("@qq.com>")>0) :  
        qqName=i[20:].split("\n")[0]
        
        qqNameList.append(qqName)
        try:
            if(i.find("<")>0 and i.find("qq.com>")>0):
                #print qqName
            
                qqNumList.append(qqName.split("<")[1].split(">")[0])
                if numNamedic.has_key(qqName.split("<")[1].split(">")[0])==False:
                    numNamedic[qqName.split("<")[1].split(">")[0]]=qqName.split("<")[0]

            else:
                qqNumList.append(qqName.split("(")[1].split(")")[0])
                if numNamedic.has_key(qqName.split("(")[1].split(")")[0])==False:
                    numNamedic[qqName.split("(")[1].split(")")[0]]=qqName.split("(")[0]
                
        except Exception,e:
            pass        
myNumList=list(set(qqNumList))#只有qq号

mylist=list(set(qqNameList))  #qq号加昵称
#print numNamedic
for i in myNumList:
    m=numNamedic[str(i)]
    #print m
    qqNumDic[m+"("+i+")"]=qqNumList.count(i)    
myqqNumDic=sorted(qqNumDic.iteritems(),key=lambda d:d[1],reverse=True)

for i in myqqNumDic:
    print i[0]+":"+str(i[1])






#for i in mylist:
   # qqDic[i]=qqNameList.count(i)    
#myqqDic=sorted(qqDic.iteritems(),key=lambda d:d[1],reverse=True)

#for i in myqqDic:
   # print i[0]+":"+str(i[1])
   
