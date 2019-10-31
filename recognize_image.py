# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 23:37:00 2019

@author: Mak Chaudhary
"""

import face_recognition
import numpy as np
import pickle
import time
import os

def process(frame, name, index):
    
    start = time.time()
    
    os.chdir('C:\\Users\\Mak Chaudhary\\Desktop\\sdp_dataset')
    cropped = frame
    encode = face_recognition.face_encodings(cropped)
    if len(encode):
        encode = encode[0]
        with open('face_encodings.pickle','rb') as inputFile:
            while True:
                try:
                    temp = pickle.load(inputFile)
                except EOFError:
                    break
        temp = temp[0]
        
        allZeros = np.zeros((128,1), dtype = np.int32)
        allEncodings = []
        Names = list(temp.keys())
        for i in Names:
            encodings = temp[i]
            for j in encodings:
                allEncodings.append(j if len(j)>0 else allZeros)
        #allEncodings.remove(allEncodings[0])
        
        tempDistances = [face_recognition.face_distance(np.asarray(allEncodings[x]),np.asarray(encode)) for x in range(len(allEncodings))]

        whoIsThat = [ True if x[0] < 0.5 else False for x in tempDistances]

        if True in whoIsThat:
            #code_here
            freqs= [ whoIsThat[(i-1)*100:i*100].count(True) for i in range(1, 1 + len(whoIsThat)) ]
            name[index] = Names[np.argmax(freqs)]
        else:
            name[index] = 'Unknown'
        
        end = time.time()
        print('time: ',end - start)