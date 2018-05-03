# Updated Animation Starter Code

import pyaudio

import numpy as np

import os

from selectMode import *

from liveMode import *

from homeMode import *

from playMode import *

import aubio

import struct

import copy

from tkinter import *
import globals

####################################
# customize these functions
####################################

def init(data):
    
    globals.dat = data 


    data.Colors = [["brown4", "firebrick4","firebrick3","OrangeRed3","firebrick2",\
                   "red2", "red","firebrick1","coral2", "salmon"],
                   
                   ["#b35900", "#cc6600", "#e67300", "#ff8000", "#ff8c1a", "#ff9933",\
                   "#ffa64d", "#ffb366", "#ffbf80", "#ffcc99"],
                   
                   ["#b3b300","#cccc00", "#e6e600", "#ffff00", "#ffff1a", "#ffff33",\
                    "#ffff4d","#ffff66", "#ffff80", "#ffff99"],
                   
                   ["#009900", "#00b300", "#00cc00", "#00e600", "#00ff00", "#1aff1a",\
                   "#33ff33", "#4dff4d", "#66ff66", "#80ff80"],
                   
                   ["#00997a", "#00b38f", "#00cca3", "#00e6b8", "#00ffcc",\
                   "#1affd1", "#33ffd6","#4dffdb", "#66ffe0", "#80ffe5"],
                
                    ["#4d0099", "#5900b3", "#6600cc", "#7300e6", "#8000ff", "#8c1aff",\
                     "#9933ff", "#a64dff", "#b366ff", "#bf80ff"]]

    
    
    data.mode = "homePage"
    data.modes = ["Try it Live!", "Select"]
    data.rectangles = []
    data.rec = True
    
    data.count = 0
    
    #pitch variables
    data.pitch = 0
    data.highestPitch = 0
    
    data.beatCircles = []
    data.numCircles = 0
    data.circleM = data.width//50
    data.beatCr = 0
    data.beatCx = data.width*3//4
    data.beatCy = data.height//2
    data.beatColor = ""
    data.averageBeat = []
    data.rows =15
    data.cols = 20
        
    #rotating circle stuff    
    data.rotCircles = []
    data.radius = 50
    data.smallR = 10
    points = 8
    data.currAngle = math.pi*8/16
    data.moveAngle = math.pi/points*2
    data.speed = 0
    data.rotColor = ["orange red", "cyan", "purple1", "spring green", "violetRed1",\
                     "lightBlue1", "yellow", "SeaGreen1", "azure", "gold"]
    data.RCI = 0
    for i in range(points):
        data.rotCircles.append([data.width*3//4-data.radius*math.cos(data.currAngle), 
                               data.height//2 - data.radius*math.sin(data.currAngle),data.currAngle])
        
        data.currAngle += data.moveAngle
    
    data.backColor = "black"
    
    data.liveTitleC = "black"
    
    
    #mode variables
    data.MM = data.width//10
    
    
    #playMode variables
    data.audio = 'xc0'
    data.song = ""
    data.songs = []
    data.finalSongs = []
    data.songsLen = 0
    data.songM = data.width//20
    
    
    data.directory = "/Users/kailasshekar/Desktop/cmu 112/TP"
    
        
    #create 8 rectangles for frequency buckets and change height
    data.rectW= (data.width*2//3)//16
    
    
    data.rectColor = ["#004080", "#004d99", "#0059b3", "#0066cc", "#0073e6", "#0080ff",\
                      "#1a8cff", "#3399ff","#4da6ff", "#66b3ff"]

    data.h1 = 5
    data.rect1 = [data.rectW, data.h1]
    data.rectangles.append(data.rect1)
    


    data.h2 = 5
    data.rect2 = [data.rectW*2, data.h2]
    data.rectangles.append(data.rect2)
    

    data.h3 = 5
    data.rect3 = [data.rectW*3, data.h3]
    data.rectangles.append(data.rect3)
    

    data.h4 = 5
    data.rect4 = [data.rectW*4, data.h4]
    data.rectangles.append(data.rect4)
    
    
    data.h5 = 5
    data.rect5 = [data.rectW*5, data.h5]
    data.rectangles.append(data.rect5)

            
    data.h6 = 5
    data.rect6 = [data.rectW*6, data.h6]
    data.rectangles.append(data.rect6)
            


    data.h7 = 5
    data.rect7 = [data.rectW*7, data.h7]
    data.rectangles.append(data.rect7)
    

    data.h8 = 5
    data.rect8 = [data.rectW*8, data.h8]
    data.rectangles.append(data.rect8)
    

    data.h9 = 5
    data.rect9 = [data.rectW*9, data.h9]
    data.rectangles.append(data.rect9)
    

    data.h10 = 5
    data.rect10 = [data.rectW*10, data.h10]
    data.rectangles.append(data.rect10)
    
    #play mode variables
    data.playCount = 0
    
    data.paused = False
    data.stream = None
    data.p = None
    
    
def mousePressed(event, data):
    # use event.x and event.y
    if (data.mode == "homePage"): 
        homePageMousePressed(event, data)
        
    elif (data.mode == "live"):   
        liveMousePressed(event, data)
        
    elif (data.mode == "select"):       
        selectMousePressed(event,data)
    elif (data.mode == "playMode"):       
        playModeMousePressed(event,data)

def keyPressed(event, data):
    # use event.char and event.keysym
    #makeStream()
    pass


# def makeStream():
#     global dat 
#     
#     data = dat
#     data.p = pyaudio.PyAudio()
#     
#     
#     #if not initialized
#     if (data.stream != None):
#         data.stream.stop_stream()
#         
#         
#     data.stream = None
#     data.stream = data.p.open(format=data.p.get_format_from_width(wf.getsampwidth()),
#         channels=wf.getnchannels(),
#         rate=intwf.getframerate(),
#         output=True,
#         stream_callback = callback)
#         
#     data.stream.start_stream()
    
    
def callback(in_data, frame_count, time_info, status):
    global dat
    data = dat
    
    audioD = wf.readframes(frame_count)
    
    #p = data.p
    #stream = data.stream
    
    #diff = copy.copy(aduioD)
    
    #getFourier(audioD, data)
    #beat(audioD, data)
    #getRotSpeed(audioD, data)
    
    return(audioD, pyaudio.paContinue)


def timerFired(data):
    if data.mode == "homePage":
        homePageTimerFired(data)
    elif data.mode == "live":
        liveTimerFired(data)
    elif data.mode == "select":
        selectTimerFired(data)
    elif data.mode == "playMode":
        pass
        #playModeTimerFired(data)
        # global wf
        # wf = wave.open("songs/"+data.song)
        # data.p = pyaudio.PyAudio()
        # 
        # #p = data.p
        # data.stream = data.p.open(format = data.p.get_format_from_width(wf.getsampwidth()),
        #                     channels=wf.getnchannels(),
        #                     rate=wf.getframerate(),
        #                     output=True,
        #                     stream_callback = callback)
    

def redrawAll(canvas, data):
    # draw in canvas
    if data.mode == "homePage":
        homePageRedrawAll(canvas, data)
    elif data.mode == "live":
        liveRedrawAll(canvas, data)
    elif data.mode == "select":
        selectRedrawAll(canvas, data)
    elif data.mode == "playMode":
        playModeRedrawAll(canvas, data)
    
    

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 600)