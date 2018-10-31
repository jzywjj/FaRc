# -*- coding:utf-8 -*-
import pika
from dev.configUtil import getPropertyVal
import base64
# 接受来自截图的图片信息
def MQConnection():
    credentials=pika.PlainCredentials(getPropertyVal('rabbitmq','rabbitmq_user'), getPropertyVal('rabbitmq','rabbitmq_password'), False)
    connectionParameters =pika.ConnectionParameters(host=getPropertyVal('rabbitmq','rabbitmq_host'), port=getPropertyVal('rabbitmq','rabbitmq_port'), virtual_host=getPropertyVal('rabbitmq','rabbitmq_vhot'), credentials=credentials)
    
    connection=pika.BlockingConnection(connectionParameters)
    return connection
    
def Recv(callback):
    connection=MQConnection()
    channel=connection.channel()
    channel.queue_declare(queue='COMPARE_IMAGE')
    channel.basic_consume(callback,
                      queue='COMPARE_IMAGE',
                      no_ack=True)
    channel.start_consuming()
    
    
def RecvCamelImage(callback):
    connection=MQConnection()
    channel=connection.channel()
    channel.queue_declare(queue='SAVE_IMAGE')
    channel.basic_consume(callback,
                      queue='SAVE_IMAGE',
                      no_ack=True)
    channel.start_consuming()

def SendMsg(msg):
    connection=MQConnection()
    channel=connection.channel()
    channel.queue_declare(queue='RE_RESULT')

    channel.basic_publish(exchange='',
    routing_key='RE_RESULT',
    body=msg)

    connection.close()

