import module_manager
module_manager.review()

import pyaudio

import struct

import wave

import string

import numpy as np

import sys

import matplotlib.pyplot as plt

import time


#CHUNK = 1024


def playWav(filename):
    
    #insipired from online code
    #got main parts from online code at: https://stackoverflow.com/questions/6951046/pyaudio-help-play-a-file?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    
    wf = wave.open(filename, 'rb')
    Chunk = 1024
    
    # Instantiate PyAudio.
    p = pyaudio.PyAudio()
    
    print("start playing")
    # Open stream.
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
                    output=True)
    
    data = wf.readframes(Chunk)
    dataLen = len(data)
    mult = dataLen//Chunk

    
    structData = np.array(struct.unpack(str(mult * Chunk) + 'b', data))[::2]

    #structData = np.array(struct.unpack(str(mult * Chunk) + 'B', data))[::2] + 127 #bytes from 0-255
    
    print(structData)
    
    #finalData = np.array(structData, dtype = 'b')[::2] + 127 #add half since not signed
    print(len(structData))
    


    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(Chunk)
        print("DATA STUFF OVER HERE!!!!!!!!!")
        #print(data, end = "\n")
    
    print("end playing")
    

    
    #print(numData)
    
    
    # count = 0
    # for num in numData:
    #     if num > 100 or num < -100:
    #         print(num)
    #         count+=1
    # print("num greater than 100: ", count)
    # for i in structData:
    #     if i > 100 or i < -100:
    #         print(i)
    #     else:
    #         pass
    
    while stream.is_active():
        time.sleep(.1)
            
    # Stop stream.
    stream.stop_stream()
    stream.close()

    # Close PyAudio.
    p.terminate()
    


    def analyze(audio):
        if type(audio) == "int":
            print("end here")
            return None
        wavD= np.fromstring(audio, dtype = np.int16)
        fourier = fftpack.dct(wavD)
        fourier = np.abs(fourier)
        fourier = fourier[:len(fourier)//2]
        print(fourier)

def callPlay(filename):
    playWav(filename)
   
i = 0
while i < 1000:
    callPlay("songs/TryMe.wav")
    i+=1
    print("WILL THIS STOP HEREE??????????????????????")