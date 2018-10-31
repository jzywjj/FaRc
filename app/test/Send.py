# -*- coding:utf-8 -*-
import pika
from dev.configUtil import getPropertyVal
import base64
import os

def MQConnection():
    credentials=pika.PlainCredentials(getPropertyVal('rabbitmq','rabbitmq_user'), getPropertyVal('rabbitmq','rabbitmq_password'), False)
    connectionParameters =pika.ConnectionParameters(host=getPropertyVal('rabbitmq','rabbitmq_host'), port=getPropertyVal('rabbitmq','rabbitmq_port'), virtual_host=getPropertyVal('rabbitmq','rabbitmq_vhot'), credentials=credentials)
    
    connection=pika.BlockingConnection(connectionParameters)
    return connection

def send(exchangeName):
    connection=MQConnection()
    channel=connection.channel()
    channel.exchange_declare(exchange=exchangeName,exchange_type='fanout')
    f=open('/home/apple/Desktop/1.jpg', 'rb')
    base64_data=base64.b64encode(f.read())
    channel.basic_publish(exchange=exchangeName,routing_key='',body=base64_data)

    connection.close() 
    
def imageSend(filepath):
    with open(filepath,"rb") as f:  
        # b64encode是编码，b64decode是解码  
        base64_data = base64.b64encode(f.read())
        
    connection=MQConnection()
    channel=connection.channel()
    channel.queue_declare(queue='RE_IMAGE')
    channel.basic_publish(exchange='',
                          routing_key='RE_IMAGE',
                          body=base64_data)

    connection.close() 
    

    
if __name__ =="__main__":
#     for root, dirs, files in os.walk("/home/apple/Desktop/images/"):
#       
#         for x in files:
#             imageSend("/home/apple/Desktop/images/"+str(x))
   #imageSend('/home/apple/Desktop/2.jpg')
    send('logs')



      