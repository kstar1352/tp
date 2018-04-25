# import module_manager
# module_manager.review()

import conda

import math

import pyaudio

import matplotlib.pyplot as plt

import aubio

import struct 

import numpy as np

import scipy as sp

from scipy.fftpack import fft

from scipy import signal

totalD = np.array(tuple([]))
print(type(totalD))
i = 0
while i<1:
    
    #insipired from online code
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
                    output = True,
                    frames_per_buffer=CHUNK)
                    
    frames = []
    
    #recording    
    data = stream.read(CHUNK)
    
    mult = len(data)//CHUNK
    
    intD = np.fromstring(data, dtype = np.int16)[::2]
    
    #intD = struct.unpack(str(CHUNK*mult) +"b", data)[::2]
    
    #readD = np.array(struct.unpack(str(CHUNK*mult) +"b", data))[::2] 
    
    #readD = np.array(struct.unpack(str(CHUNK*mult) +"b", data))
    
    #pitch = aubio.pitch(CHUNK)
    
    #signal = readD
    
    #n = signal.size
    
    #Fourier = np.fft.fft(readD)
    
    #Fourier = np.fft.fft(intD)
    
    #realFourier = np.abs(Fourier[:len(Fourier)//2])
    
    #freq = np.fft.fftfreq(n, d = 1/44100)
    
    #finalFreq = freq[:len(freq)//2]
    
    # for i in range(len(realFourier)):
    #     print(realFourier[i])
    
    for i in range(len(intD)):
        print(intD[i])
    
    
    
    bucket1 = 0
    bucket2 = 0
    bucket3 = 0
    bucket4 = 0
    bucket5 = 0
    bucket6 = 0
    bucket7 = 0
    bucket8 = 0
    
    
    # to get finalFreq use fftfreq, and make signal equal to readD which is 
    # an np array, then set n = the signal size of that. Ater that apply Fourier 
    # transfrom to readD. Then get the frequencies by doing using the fftfreq 
    # by doing n and d = 1/44100. Finally cut down both the lists to first half. 
    # Then create buckets to make sure they are working properly. 
    
    # print("number of frequencies: ", len(finalFreq))
    # print("Fourier frequencies:", realFourier)
    # for i in range(len(finalFreq)):
    #     
    #     if i < len(finalFreq)//8:
    #         bucket1 += realFourier[i]
    #         
    #     elif i < len(finalFreq)*2//8:
    #         bucket2+= realFourier[i]
    #         
    #     elif i < len(finalFreq)*3//8:
    #         bucket3+= realFourier[i]
    #         
    #     elif i < len(finalFreq)*4//8:
    #         bucket4+= realFourier[i]
    #         
    #     elif i < len(finalFreq)*5//8:
    #         bucket5+= realFourier[i]
    #         
    #     elif i < len(finalFreq)*6//8:
    #         bucket6+= realFourier[i]
    #         
    #     elif i < len(finalFreq)*7//8:
    #         bucket7 += realFourier[i]
    #     else:
    #         bucket8 += realFourier[i]
            
        #print("freq: ", realFourier[i])
        #print("amount: ", realFourier[i]) 
        
        
    #print("frequency buckets: ", freq[:len(freq)//2])
    
    #Fourier = (np.fft.fft(intD))
    #print("Fourier Transform:",Fourier)
    
    
    #psd = np.fft.fftfreq(CHUNK, 44100)
    #print("Spectrum: ", len(psd[1:CHUNK//2]))
    
    
    
    
    #pS, fsd  = sp.signal.welch(readD, 44100)
    #print("Spectral analysis: ",fsd)
    
    
        
    i +=1
    
    #print(readD)
    #print(type(readD))

    
#plt.plot(readD)
plt.plot(intD)
#plt.psd(readD,1024, 44100)
#plt.plot(Fourier)
#plt.semilogx(pS, fsd)
#plt.semilogx(pS, fsd)
#plt.plot(psd)
#plt.show()
#plt.tight_layout()

#print(len(intD), len(readD), len(finalFreq))

print("bucket1: ", bucket1)
print("bucket2: ", bucket2)
print("bucket3: ", bucket3)
print("bucket4: ", bucket4)
print("bucket5: ", bucket5)
print("bucket6: ", bucket6)
print("bucket7: ", bucket7)
print("bucket8: ", bucket8)

# 
# a = [1, 0, -1, 0, 1]
# 
# plt.plot(a)
plt.show()