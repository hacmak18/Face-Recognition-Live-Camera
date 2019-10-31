# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 23:00:17 2019

@author: Mak Chaudhary
"""

import cv2
import threading
import os
os.chdir('C:\\Users\\Mak Chaudhary\\Desktop\\sdp_dataset')
import face_recognition
from recognize_image import process


font = cv2.FONT_HERSHEY_SIMPLEX
#names = []

def captureFrame():

    #firstFrame = True
    count = 0
    
    video_capture = cv2.VideoCapture(0)
    names = [None]
    while True:
        #names = [None]
        ret, frame = video_capture.read()
        #print('2')
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        locations = face_recognition.face_locations(rgb)
        

        
        if count%20 == 0:
            
            print('frame: ',count)
            
            if len(locations):
                names = ['Unknown'] * len(locations)
                print('total Names:',len(names))
                for i in range(len(locations)):
                    
                    (top,right,bottom,left) = locations[i]
                    rgbFace = rgb[top:bottom,left:right]
                    
                    
                    try:
                        Tprocess = threading.Thread(target = process,args = (rgbFace, names, i))
                        Tprocess.start()
                        Tprocess.join()
                    except:
                        print("here")
                     #print(names)
        
        try:
            global font
            for i in range(len(names)):
                    (t,r,b,l) = locations[i]
                    cv2.putText(frame, names[i], (l,t-5), font, 0.6, (0, 0, 255), 2, cv2.LINE_AA)
        except:
            print(names)
        count += 1
        
        for i in range(len(locations)):
            (t,r,b,l) = locations[i]
            cv2.rectangle(frame,(l,t),(r,b),(0,0,255),3)                
        #if name is None:
        #    print('none')
        #else:            
        #    recognized = True
        
        # Display the resulting image
        
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()

#captureFrame()