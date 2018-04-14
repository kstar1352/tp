import module_manager
module_manager.review()

import pyaudio

import wave

import numpy

import sys


class Audio(object):
    Chunk = 1024
    #p = pyaudio.PyAudio()
    
    
    def __init__(self):
        pass
        
    def record(self, file, seconds = 5):
        
        #initial variables
        Chunk = 1024
        Channels = 2
        Format = pyaudio.paInt32
        Rate = 44100
        recordSeconds= seconds
        outputFile = file
        p = pyaudio.PyAudio()
        
        #open stream
        stream = p.open(format=Format,
                    channels=Channels,
                    rate=Rate,
                    input=True,
                    frames_per_buffer = Chunk)
    
        frames = []
        
        #read the file
        for i in range(0, int(Rate / Chunk * recordSeconds)):
            data = stream.read(Chunk)
            frames.append(data)
            
        #close the stream
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        wf = wave.open(outputFile, 'wb')
        wf.setnchannels(Channels)
        wf.setsampwidth(p.get_sample_size(Format))
        wf.setframerate(Rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        
    def play(self, file):
        pass
        
        
A1 = Audio()
A1.record("voice.wav")

        