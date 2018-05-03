
import os

from liveMode import *

import pyaudio

import numpy as np

import wave 

#from visuals import *

import scipy as sc 

import threading
from queue import Queue
import time 

import aubio


###################
#PLAY MODE
###################

def playModeMousePressed(event,data):
    x = event.x
    y = event.y
    
    
    if x > data.width*24//28 and y>data.height-40 and data.paused:
        data.paused = not data.paused
        data.stream.start_stream()
        
    elif x> data.width*24//28 and y>data.height-40:
        data.paused = not data.paused
        data.stream.stop_stream()
        
    if x > data.width-40 and y < 40:
        if data.stream != None:
            data.stream.stop_stream()
            data.stream.close()
            data.p.terminate()
        data.mode = "homePage"
        data.paused = False
    
    
def drawPause(canvas, data):
    if data.paused:
        canvas.create_polygon((data.width*25//28, data.height-40), 
                              (data.width*25//28, data.height-10),
                              (data.width*27//28, data.height-25),
                              fill = "gray")
    else:
        canvas.create_rectangle(data.width*36//40, data.height-40, 
                            data.width*37//40, data.height-5, fill = "gray")
        canvas.create_rectangle(data.width*38//40, data.height-40, 
                            data.width*39//40, data.height-5, fill = "gray")
    

def playModeKeyPressed(event,data):
    pass
    
def playModeTimerFired(data):
    pass

        
    
def playModeRedrawAll(canvas, data):
    drawBackground(canvas, data)
    drawPause(canvas, data)
    drawBeat(canvas,data)
    drawRotating(canvas, data)
    drawRectangles(canvas, data)
    resetRects(canvas,data)


    