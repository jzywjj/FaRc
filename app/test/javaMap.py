# -*- coding:utf-8 -*-
import pika
from dev.configUtil import getPropertyVal
import base64
import os
import json

def MQConnection():
    credentials=pika.PlainCredentials(getPropertyVal('rabbitmq','rabbitmq_user'), getPropertyVal('rabbitmq','rabbitmq_password'), False)
    connectionParameters =pika.ConnectionParameters(host=getPropertyVal('rabbitmq','rabbitmq_host'), port=getPropertyVal('rabbitmq','rabbitmq_port'), virtual_host=getPropertyVal('rabbitmq','rabbitmq_vhot'), credentials=credentials)
    
    connection=pika.BlockingConnection(connectionParameters)
    return connection
def callback(ch, method, properties, body):
    print("=======")
    print(body)
    data=json.loads(body)
    print(data['a'])
    print(data['b'])
    
def setup():
    connection=MQConnection()
    channel=connection.channel()
    channel.queue_declare(queue="myqueue",durable=True)
    
    channel.basic_consume(callback, queue="myqueue", no_ack=True)
    channel.start_consuming()
    
if __name__ == '__main__':
    setup()