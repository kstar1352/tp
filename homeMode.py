import module_manager
module_manager.review()

import pyaudio

import numpy as np

import aubio


import struct

from liveMode import *

import globals


##########################
#homePage
##########################

def liveCallback(in_data, frame_count, time_info, status):
    data = globals.dat
    
    audioD = in_data
    
    getLiveFourier(audioD, data)
    liveBeat(audioD, data)
    getLiveRotSpeed(audioD, data)
    
    return (audioD, pyaudio.paContinue)
    
    

def homePageMousePressed(event,data):
    x = event.x
    y = event.y
    
    #for the live selection
    if (x > data.MM and x < data.width//2 - data.MM) and \
        (y > data.height//2 and y < data.height*3//4):
            data.mode = "live"
            
            data = globals.dat
            
            data.p = pyaudio.PyAudio()
            
            data.stream = data.p.open(format = pyaudio.paInt16,
                            channels=1,
                            rate=44100,
                            input=True,
                            stream_callback = liveCallback)
            
    #for the song selection
    elif (x > data.MM+data.width//2 and x < data.width - data.MM) and \
        (y > data.height//2 and y < data.height*3//4):
            data.mode = "select"
    

def homePageKeyPressed(event,data):
    pass
    
def homePageTimerFired(data):
    pass

#creates title
def drawTitle(canvas, data):
    canvas.create_text(data.width//2, data.height//4, text = "AudioLizer", 
                       font = "Helevetica " + str(data.width//15))
                       
                       
                       
def drawModes(canvas, data):
    for box in range(2):
        canvas.create_rectangle(data.width*(box)//2 + data.MM,
                                data.height*4//8, 
                                data.width*(box+1)//2-data.MM,
                                data.height*6//8, width = 5)
        if box == 0:
            
            canvas.create_text(data.width*(box+1)//4, data.height*5//8, 
                           text = data.modes[box], 
                           font = "Helevetica " + str(data.width//20))
        else:
            canvas.create_text(data.width*(box+2)//4, data.height*5//8, 
                           text = data.modes[box], 
                           font = "Helevetica " + str(data.width//20))
#create the live box
def drawLive(canvas, data):
    canvas.create_rectangle(data.width//8, data.height//2, data.width*3//8,
                            data.height*3//4, width = 5)
    canvas.create_text(data.width*2//8, data.height*5//8, text = "Try it Live",
                       font = "Helevetica " + str(data.width//20))
                       
                       
def drawHomeBack(canvas, data):
    rows = 5
    for i in range(rows):
        canvas.create_rectangle(0,data.height*i//5, data.width, \
                                data.height*(i+1)//5, fill = data.homeColors2[i],
                                width = 0)

    
def homePageRedrawAll(canvas, data):
    #title
    drawHomeBack(canvas, data)
    drawTitle(canvas, data)
    drawModes(canvas, data)
    #drawLive(canvas, data)