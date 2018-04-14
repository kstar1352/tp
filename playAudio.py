import module_manager
module_manager.review()

import pyaudio

import struct

import wave

import string

import numpy

import sys

#CHUNK = 1024


def playWav(filename, Chunk = 1024):

    wf = wave.open(filename, 'rb')
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
    
    print(mult)
    intData = struct.unpack(str(mult * Chunk) + 'B', data)
    
    
    print(intData)

    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(Chunk)
    
    print("end playing")
    # Stop stream.
    stream.stop_stream()
    stream.close()

    # Close PyAudio.
    p.terminate()
    

