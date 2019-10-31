# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:15:41 2019

@author: Mak Chaudhary
"""

import cv2
import face_recognition
import pickle
import imutils
import os

def Gdataset():
    os.chdir('C:\\Users\\Mak Chaudhary\\Desktop\\sdp_dataset')
    
    print('Enter the full name:- ',end='')
    name = input().split()
    
    full_name = ''
    for word in name:
        full_name = full_name + '_' + word
    
    if not os.path.isdir(full_name):
        os.mkdir(full_name)
        os.chdir(full_name)
        cwd = os.getcwd()
    else:
        print('The directory already exists. want to delete ? [y / n]')
        choice = input()
        if choice == 'y':
            for filename in os.listdir(full_name):
                os.remove(full_name + '\\' +filename)
            os.rmdir(full_name)
            os.mkdir(full_name)
            os.chdir(full_name)
            cwd = os.getcwd()
        else:
            print('closing program...')
            exit()
    
    data = []
    inputFile = open('C:\\Users\\Mak Chaudhary\\Desktop\\sdp_dataset\\face_encodings.pickle','rb')
    while True:
        try:
            data.append(pickle.load(inputFile))
        except:
            break
    
    video = cv2.VideoCapture(0)
    
    cnt = 0
    encodings = []
    while True:
        
        ret, frame = video.read()
        
    
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
        location = face_recognition.face_locations(rgb)
    
        cropped_image = None
        
        if len(location) == 1:
            cnt = cnt + 1
            (top, right, bottom, left) = location[0]        
            cropped_image = frame[top:bottom,left:right]
            cropped_image = cv2.resize(cropped_image, (128, 128))
            encodings.append(face_recognition.face_encodings(cropped_image))
            cv2.imwrite( cwd + '\\' + full_name + '_' + str(cnt) + '.jpg',cropped_image)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            
        if cnt == 100:
            break
        
        cv2.imshow('xyz',frame)
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release handle to the webcam
    video.release()
    cv2.destroyAllWindows()
    
    data[0][full_name] = encodings
    
    outputFile = open('C:\\Users\\Mak Chaudhary\\Desktop\\sdp_dataset\\face_encodings.pickle','wb')
    pickle.dump(data,outputFile)
    outputFile.close()
#Gdataset()
