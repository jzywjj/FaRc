# -*- coding:utf-8 -*-
import base64
import cv2
import numpy as np

# base64解码返回图像信息
def faceDecoding(base64_data):
    data=base64.b64decode(base64_data)
    nparr =np.fromstring(data,np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    return img_np

def BASE64_Decoding(data):
    d=base64.b64decode(data)
    return d