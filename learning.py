# import module_manager
# module_manager.review()

import conda

import pyaudio

import matplotlib.pyplot as plt

import struct 

import numpy as np

import scipy

totalD = np.array(tuple([]))
print(type(totalD))
T = True
i = 0
while T:
    CHUNK = 1024
    FORMAT = pyaudio.paInt32
    CHANNELS = 1
    RATE = 44100
    #RECORD_SECONDS = 5
    #WAVE_OUTPUT_FILENAME = filename
    
    p = pyaudio.PyAudio()
    
    
    #mic open    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
                    
    frames = []
    
    #recording    
    data = stream.read(CHUNK)
    
    mult = len(data)//CHUNK
    readD = np.array(struct.unpack(str(CHUNK*mult) +"b", data))[::2] 
    
        
    i +=1
    if i ==10:
        T = False
    
    print(readD)
    print(type(readD))
    #np.add(totalD, readD)
    
plt.plot(readD)
plt.show()

# 
# a = [1, 0, -1, 0, 1]
# 
# plt.plot(a)
# plt.show()