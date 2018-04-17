import module_manager
module_manager.review()

import pyaudio

import wave

import numpy
import struct
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
        
        print("START RECORDING")
        #read the file
        for i in range(0, int(Rate / Chunk * recordSeconds)):
            data = stream.read(Chunk)
            frames.append(data)
            
        print("DONE RECORDING")
            
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
        
        wf = wave.open(file, 'rb')
        Chunk = 1024
        # Instantiate PyAudio.
        p = pyaudio.PyAudio()
        
        print("start playing")
        
        #p.get_format_from_width(wf.getsampwidth())
        # Open stream.
        stream = p.open(format=pyaudio.paInt32,
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
                        output=True)
        
        data = wf.readframes(Chunk)
        dataLen = len(data)
        mult = dataLen//Chunk
        
    
        print("chunk type: ", type(Chunk))
        structData = struct.unpack(str(mult * Chunk) + 'B', data)
        
        numData = numpy.fromstring(data)
        
        
        # for i in range(len(structData)):
        #     if abs(structData[i]) > 100:
        #         print(structData)
            
        #print(numData)
        
        #print(intData)
        
        for num in numData:
            if num > 100 or num < 100:
                stream.write(data)
                data = wf.readframes(Chunk)
    
        # while len(data) > 0:
        #     stream.write(data)
        #     data = wf.readframes(Chunk)
        
        print("end playing")
        
        
        #print(numData)
        
        print("numData len:",len(numData))
        print("structData len:", len(structData))
        
        count = 0
        for num in numData:
            if num > 100 or num < -100:
                print(num)
                count+=1
        print("num greater than 100: ", count)
        
        # for i in structData:
        #     if i > 100 or i < -100:
        #         print(i)
        #     else:
        #         pass
                
        # Stop stream.
        stream.stop_stream()
        stream.close()
    
        # Close PyAudio.
        p.terminate()
        
        
A1 = Audio()
A1.record("voice.wav")
A1.play("voice.wav")

        