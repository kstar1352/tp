


####to uncomment mult lines use command t
import os

import pyaudio

import numpy as np

import aubio

import wave

from liveMode import *

import struct
import globals
###################
#SELECT MODE
###################



def callback(in_data, frame_count, time_info, status):
    data = globals.dat
    
    audioD = wf.readframes(frame_count)
    
    #p = data.p
    #stream = data.stream
    
    
    getFourier(audioD, data)
    beat(audioD, data)
    getRotSpeed(audioD, data)
    
    return(audioD, pyaudio.paContinue)


def selectMousePressed(event,data):
    x = event.x
    y = event.y
    
    if x > data.width-40 and y < 40:
        data.mode = "homePage"
        
    rows = data.songsLen//4
    colF = data.songsLen%4
    index = 0 
    for i in range(rows+1):
        for j in range(4):
            
            if i == rows and j >=colF:
                return None
            
            if (x > data.width*j//4 + data.songM and \
            x < data.width*(j+1)//4 - data.songM)\
            and (y > data.height*(i+2)//8 and y < data.height*(i+3)//8):
                print("clicked in index: ", index)
                data.song = data.finalSongs[index]
                print(data.finalSongs, data.song)
                
                global wf
                wf = wave.open("songs/"+data.song)
                data.p = pyaudio.PyAudio()
        
                #p = data.p
                data.stream = data.p.open(format = data.p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True,
                            stream_callback = callback)
                            
                data.mode = "playMode"
            
            index +=1 

    
    # if x < data.width//2+40 and y < data.height//2+20 and x > data.width//2-40\
    # and y > data.height//2-40:
    #     data.mode = "playMode"
    
    
def selectKeyPressed(event,data):
    pass
    
def selectTimerFired(data):
    if data.count == 0:
        getSongs(data.directory, data)
        
        for i in range(len(data.songs)):
            if data.songs[i] != "":
                data.songsLen +=1
                flag = True
                while flag:
                    found = data.songs[i].find("/")
                    if found == -1:
                        flag = False
                    else:
                        data.songs[i] = data.songs[i][found+1:]
                    
                song = data.songs[i]
                data.finalSongs.append(song)
        print(data.finalSongs)
    data.count += 1
    
    

        
def drawSelect(canvas, data):
    canvas.create_text(data.width//2, data.height//6, text = "Select a Song",
                       font = "Helvetica " + str(data.width//15))

def drawSongs(canvas, data):
    #getSongs(data.directory, data)
    rows = data.songsLen//4
    colF = data.songsLen%4
    index = 0
    for i in range(rows+1):
        for j in range(4):
            
            #for last row when to stop
            if i == rows and j >=colF:
                return None
                
            #draw the boxes
            canvas.create_rectangle(data.width*j//4 + data.songM,
                                    data.height*(i+2)//8, 
                                    data.width*(j+1)//4 - data.songM,
                                    data.height*(i+3)//8, width = 2)

            
            #write the text
            canvas.create_text(data.width*(j*2+1)//8, data.height*(i*2+5)//16,
                               text = data.finalSongs[index][:-4])
                               
            index+=1
        
    #canvas.create_rectangle(data.width//2-40, data.height//2-20, data.width//2+40,
                            #data.height//2 +20, width = 5)
    #canvas.create_text(data.width//2, data.height//2, text = "Try Me")
    
    
def getSongs(path, data):
    if path[-3:] == "wav" and (os.path.isdir(path) == False):
        return [path]
    elif os.path.isdir(path) == False:
        return [""]
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