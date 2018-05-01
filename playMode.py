
import os

from liveMode import *

import pyaudio

import numpy as np

import aubio

import struct

###################
#SELECT MODE
###################

def playModeMousePressed(event,data):
    pass
    
def playModeKeyPressed(event,data):
    pass
        
        
def play(filename, data):
    
    CHUNK = 1024*4
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    
    def analyze(audio):
        if type(audio) == "int":
            print("end here")
            return None
        wavD= np.fromstring(audio, dtype = np.int16)
        fourier = fftpack.dct(wavD)
        fourier = np.abs(fourier)
        fourier = fourier[:len(fourier)//2]
        print(fourier)


    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        data.playAudio = data
        print(audioD)
        return (data, pyaudio.paContinue)


            
    # open stream using callback (3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)
                    
    # start the stream (4)
    stream.start_stream()
    
    # wait for stream to finish (5)
    while stream.is_active():
        analyze(data.playAudio)
        time.sleep(0.01)
    
    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()
    
    # close PyAudio (7)
    p.terminate()

    
def playModeTimerFired(data):
    #play(data.song, data)
    pass
    
def playModeRedrawAll(canvas, data):
    #title
    # drawTitle(canvas, data)
    # drawLive(canvas, data)
    drawSelect(canvas, data)
    drawSongs(canvas, data)