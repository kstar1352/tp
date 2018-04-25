import pyaudio

import numpy as np

import aubio

import struct

##########################
#homePage
##########################
def homePageMousePressed(event,data):
    x = event.x
    y = event.y
    if (x > data.width//8 and x < data.width*3//8) and \
        (y > data.height//2 and y < data.height*3//4):
            print("pressed inside live box")
            data.mode = "live"
    
def homePageKeyPressed(event,data):
    pass
    
def homePageTimerFired(data):
    pass

#creates title
def drawTitle(canvas, data):
    canvas.create_text(data.width//2, data.height//4, text = "AudioLizer", 
                       font = "Helevetica " + str(data.width//15))

#create the live box
def drawLive(canvas, data):
    canvas.create_rectangle(data.width//8, data.height//2, data.width*3//8,
                            data.height*3//4, width = 5)
    canvas.create_text(data.width*2//8, data.height*5//8, text = "Try it Live",
                       font = "Helevetica " + str(data.width//20))
    
def homePageRedrawAll(canvas, data):
    #title
    drawTitle(canvas, data)
    drawLive(canvas, data)