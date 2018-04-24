# import module_manager
# module_manager.review()

import conda

import math

import pyaudio

import matplotlib.pyplot as plt

import struct 

import numpy as np

import scipy as sp

from scipy.fftpack import fft

from scipy import signal

totalD = np.array(tuple([]))
print(type(totalD))
T = True
i = 0
while T:
    
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
                    frames_per_buffer=CHUNK)
                    
    frames = []
    
    #recording    
    data = stream.read(CHUNK)
    
    mult = len(data)//CHUNK
    readD = np.array(struct.unpack(str(CHUNK*mult) +"b", data))[::2] 
    
    Fourier = np.abs(np.fft.fft(readD))
    #print("Fourier Transform:",Fourier)
    
    
    psd = np.fft.fftfreq(CHUNK, 44100)
    print("Spectrum: ", len(psd[1:CHUNK//2]))
    
    
    
    
    #pS, fsd  = sp.signal.welch(readD, 44100)
    #print("Spectral analysis: ",fsd)
    
    
        
    i +=1
    if i ==30:
        T = False
    
    #print(readD)
    #print(type(readD))

    
#plt.plot(readD)
#plt.psd(readD,1024, 44100)
plt.plot(Fourier)
#plt.semilogx(pS, fsd)
#plt.semilogx(pS, fsd)
#plt.plot(psd)
plt.show()
#plt.tight_layout()


# 
# a = [1, 0, -1, 0, 1]
# 
# plt.plot(a)
# plt.show()