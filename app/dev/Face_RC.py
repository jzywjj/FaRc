# -*- coding:utf-8 -*-
import face_recognition as face
import cv2

def Face_Coding(img_path):
    #small_frame = cv2.resize(img_path, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = img_path[:, :, ::-1]
    #img_path = img_path[:, :, ::-1]
    face_locations = face.face_locations(rgb_small_frame)
    face_encodings = face.face_encodings(rgb_small_frame, face_locations)
    
    if(len(face_encodings)>0):
        return face_encodings[0]
    
    else:
        return []
    
    
def Face_Coding_ORIG(img_path):
    img_path = img_path[:, :, ::-1]
    locations=face.face_locations(img_path)
    face_encoding=face.face_encodings(img_path,locations)
    
    if(len(face_encoding)>0):
        return face_encoding[0]
    
    else:
        return []

def Face_Distance(known_encodings,image_to_test_encoding,Lid):
    
    res=face.compare_faces(known_encodings,image_to_test_encoding,0.45)
    print(res)
    try:
        pos=res.index(True)
    except:
        return -1
    else:
        return Lid[pos]
    