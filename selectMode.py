

import pyaudio

import numpy as np

import aubio

import struct

###################
#SELECT MODE
###################

def selectMousePressed(event,data):
    pass
    
def selectKeyPressed(event,data):
    pass
    
def selectTimerFired(data):
    pass

#creates title
# def drawTitle(canvas, data):
#     canvas.create_text(data.width//2, data.height//4, text = "AudioLizer", 
#                        font = "Helevetica " + str(data.width//15))
# 
# #create the live box
# def drawLive(canvas, data):
#     canvas.create_rectangle(data.width//8, data.height//2, data.width*3//8,
#                             data.height*3//4, width = 5)
#     canvas.create_text(data.width*2//8, data.height*5//8, text = "Try it Live",
#                        font = "Helevetica " + str(data.width//20))
    
    
def drawSelect(canvas, data):
    canvas.create_text(data.width//2, data.height//6, text = "Select a Song",
                       font = "Helvetica " + str(data.width//15))
    
def selectRedrawAll(canvas, data):
    #title
    # drawTitle(canvas, data)
    # drawLive(canvas, data)
    drawSelect(canvas, data)