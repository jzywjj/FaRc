# -*- coding:utf-8 -*-
import pika
import base64
import os
import json
import cv2
import numpy as np
import demjson

def MQConnection():
    credentials=pika.PlainCredentials('admin', 'x', False)
    connectionParameters =pika.ConnectionParameters('115.29.173.89', 5672, '/', credentials=credentials)
    
    connection=pika.BlockingConnection(connectionParameters)
    return connection
def callback(ch, method, properties, body):
    data=json.loads(body)
    ad=json.loads(data)
    sd=ad["img"]
    print("=====")
    print(sd)
    m_data=base64.b64decode(sd)
    nparr =np.fromstring(m_data,np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite('/home/apple/Desktop/aa/1.jpg',img_np)
    
    
#     print(data['a'])
#     print(data['b'])
    
def setup():
    connection=MQConnection()
    channel=connection.channel()
    channel.queue_declare(queue="test",durable=False)
    
    channel.basic_consume(callback, queue="test", no_ack=True)
    channel.start_consuming()
    
if __name__ == '__main__':
    setup()