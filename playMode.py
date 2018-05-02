
import os

from liveMode import *

import pyaudio

import numpy as np

import wave 

import scipy as sc 

import threading
from queue import Queue
import time 

import aubio


###################
#SELECT MODE
###################

def playModeMousePressed(event,data):
    x = event.x
    y = event.y
    
    if x > data.width-40 and y < 40:
        data.play = False
        data.mode = "homePage"
    
def play(filename, data):
    
    CHUNK = 512
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    
    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        audioD = wf.readframes(frame_count)
        #data.audio = audioD
        #trying to use threading here but is it the right place?
        # t1 = threading.Thread(target = getFourier, args = (audioD, data))
        # t2 = threading.Thread(target = beat, args = (audioD, data))
        # t3 = threading.Thread(target = getRotSpeed, args = (audioD, data))
        # 
        # t1.daemon = True
        # t2.daemon = True
        # t3.daemon = True
        # 
        # t1.start()
        # t2.start()
        # t3.start()
        # 
        # t1.join()
        # t2.join()
        # t3.join()
        getFourier(audioD, data)
        beat(audioD, data)
        getRotSpeed(audioD, data)
        
        return (audioD, pyaudio.paContinue)


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
        time.sleep(.1)
    
    
    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()
        
    # close PyAudio (7)
    p.terminate()


def playModeKeyPressed(event,data):
    pass
    
def playModeTimerFired(data):
    play("songs/"+data.song, data)
    pass
    
def playModeRedrawAll(canvas, data):
    drawBackground(canvas, data)
    #drawLiveTitle(canvas, data)
    drawBeat(canvas,data)
    drawRotating(canvas, data)
    drawRectangles(canvas, data)
    resetRects(canvas,data)
    pass
    