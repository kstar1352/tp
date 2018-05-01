


####to uncomment mult lines use command t
import os

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
    x = event.x
    y = event.y
    
    if x < data.width//2+40 and y < data.height//2+20 and x > data.width//2-40\
    and y > data.height//2-40:
        data.mode = "playMode"
    
def selectTimerFired(data):
    if data.count == 0:
        getSongs(data.directory, data)
        print(data.songs)
    data.count += 1
    
    

        
def drawSelect(canvas, data):
    canvas.create_text(data.width//2, data.height//6, text = "Select a Song",
                       font = "Helvetica " + str(data.width//15))

def drawSongs(canvas, data):
    #getSongs(data.directory, data)
    for i in range(len(data.songs)):
        if data.songs[i] != "":
            #this is all the songs
            pass
        
        
    #canvas.create_rectangle(data.width//2-40, data.height//2-20, data.width//2+40,
                            #data.height//2 +20, width = 5)
    #canvas.create_text(data.width//2, data.height//2, text = "Try Me")
    
    
def getSongs(path, data):
    if path[-3:] == "wav" and (os.path.isdir(path) == False):
        return [path]
    elif os.path.isdir(path) == False:
        #return [""]
        return [path]
    else:
        # recursive case: it's a folder, return list of all paths
        data.songs = []
        for filename in os.listdir(path):
            data.songs += getSongs(path + "/" + filename, data)
        return data.songs
    
def selectRedrawAll(canvas, data):
    #title
    # drawTitle(canvas, data)
    # drawLive(canvas, data)
    drawSongs(canvas, data)
    drawSelect(canvas, data)
    #drawSongs(canvas, data)