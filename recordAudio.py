import module_manager
module_manager.review()

import pyaudio

import wave

import numpy

import struct


import sys



def recordWav(filename, seconds = 5):
    
    #insipired from online code from: https://gist.github.com/mabdrabo/8678538
    CHUNK = 1024
    FORMAT = pyaudio.paInt32
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = seconds
    WAVE_OUTPUT_FILENAME = filename
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("* recording")
    
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
        
    mult = len(data)//CHUNK
    
    #data= data[0:2] + data[4:]
    print(len(data))
    print(data)
    
        

    print(mult)
    structD = struct.unpack(str(CHUNK*mult) +'b', data)
    #readD = numpy.fromstring(data, "Int32") 
    
    print(structD)
    # for num in structD:
    #     print(num)
    print("* done recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

