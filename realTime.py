import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import fftpack


CHUNK = 1024*4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
i= 0

while i<2:

    stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE,
                    input = True, frames_per_buffer = CHUNK)
                    
    
    data = stream.read(CHUNK)
    #print(data)
    
    intD = np.fromstring(data, dtype = np.int16) #[::2]
    
    
    for i in range(len(intD)):
        print(intD[i])
    #print(intD)
    
    #fourier = np.fft.fft(intD)
    #fourier = fftpack.dct(intD)
    fourier = fftpack.rfft(intD)
    fourier = fourier.real
    fourier = np.abs(fourier)
    fourier = fourier[:len(fourier)//2]
    #print(fourier)
    
    buckets = []
    for i in range(8):
        buckets.append(1)
    
    
    modVal = len(fourier)//8
    j = -1
    for i in range(len(fourier)):
        if i % modVal == 0:
            j += 1
        buckets[j] += fourier[i]//1000
    
    for i in range(len(buckets)):
        print("bucket " +str(i) + ":", buckets[i]) 
    
    i+=1
#plt.plot(intD)
plt.ylim(-100,1000)
plt.plot(fourier)
plt.show()