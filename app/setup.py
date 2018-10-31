# -*- coding: utf-8 -*-

# pip install opencv-python
#pip install numpy
# pip install pika
# pip install mysql-connector

from dev.faceMQSrv import Recv,RecvCamelImage,SendMsg
from dev.faceBase64 import faceDecoding
from dev.Face_RC import Face_Coding,Face_Distance,Face_Coding_ORIG
from dev.RedisUtil import getHashVal,setHashVal
import numpy as np
import threading
import json
#MQ的回调 在此函数中收到了前端传递消息
def callback(ch, method, properties, body):
    data=json.loads(body)
    ad=json.loads(data)
    m_data=ad["img"]
    id=ad["id"]
    img=faceDecoding(m_data)
    cd=Face_Coding(img)
    if (len(cd)>0):
        faceCompare(cd,id)
    else:
        res="{'userid':'-1','id':'"+str(id)+"'}" 
        SendMsg(res)

#启动监听
def faceMQ():
    Recv(callback)


#-----------------------
# insert mysql  knownCoding
def workCallback(ch, method, properties, body):
    data=json.loads(body)
    ad=json.loads(data)
    maxid=ad["id"]
    sd=ad["img"]
    T=  Face_Coding_ORIG(faceDecoding(sd))
    if(len(T)>0):
        
        setHashVal("face", maxid, T.tostring()) 
    
    
def RecvCamImage():
    RecvCamelImage(workCallback)

kCondings=[]
kids=[] 
def faceCompare(unconding,id):
    x=getHashVal("face")
    for a,b in x.items():
        kids.append(a)  
        kCondings.append(np.fromstring(b,dtype=float))
      
    userid=Face_Distance(kCondings,unconding,kids)
    kCondings.clear()
    kids.clear()
    index=str(userid).find('b')
    if index !=-1:
        res="{'userid':'"+str(userid).replace('b', '',1)+"','id':'"+str(id)+"'}"
        SendMsg(res)
    else:
        res="{'userid':'"+str(userid)+"','id':'"+str(id)+"'}" 
        SendMsg(res)
       
       
if __name__ == '__main__':
    t1=threading.Thread(target=faceMQ)
    t2=threading.Thread(target=RecvCamImage)
    t1.start()
    t2.start()
    
    
    
    
    
    