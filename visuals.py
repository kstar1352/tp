# Updated Animation Starter Code

import pyaudio

import numpy as np


from selectMode import *

from liveMode import *

from homeMode import *

import aubio

import struct


from tkinter import *

####################################
# customize these functions
####################################

def init(data):

    data.mode = "homePage"
    data.rectangles = []
    data.rec = True
    
    #pitch variables
    data.pitch = 0
    data.highestPitch = 0
    
    data.backColor = "black"
    
    data.liveTitleC = "black"
    
    
    #create 8 rectangles for frequency buckets and change height
    data.rectW= (data.width*2//3)//16
    
    data.r1Color = "red"
    data.h1 = 5
    data.rect1 = [data.rectW, data.h1,data.r1Color]
    data.rectangles.append(data.rect1)
    

    data.r2Color = "orange"
    data.h2 = 5
    data.rect2 = [data.rectW*2, data.h2,data.r2Color]
    data.rectangles.append(data.rect2)
    
    
    data.r3Color = "yellow"
    data.h3 = 5
    data.rect3 = [data.rectW*3, data.h3, data.r3Color]
    data.rectangles.append(data.rect3)
            
    data.r4Color = "brown"
    data.h4 = 5
    data.rect4 = [data.rectW*4, data.h4,data.r4Color]
    data.rectangles.append(data.rect4)

    data.r5Color = "gray"
    data.h5 = 5
    data.rect5 = [data.rectW*5, data.h5,data.r5Color]
    data.rectangles.append(data.rect5)

            
    data.r6Color = "blue"
    data.h6 = 5
    data.rect6 = [data.rectW*6, data.h6, data.r6Color]
    data.rectangles.append(data.rect6)
            
    data.r7Color = "purple"
    data.h7 = 5
    data.rect7 = [data.rectW*7, data.h7, data.r7Color]
    data.rectangles.append(data.rect7)
    
    data.r8Color = "violet"
    data.h8 = 5
    data.rect8 = [data.rectW*8, data.h8,data.r8Color]
    data.rectangles.append(data.rect8)
    
    data.r9Color = "violet"
    data.h9 = 5
    data.rect9 = [data.rectW*9, data.h9,data.r9Color]
    data.rectangles.append(data.rect9)
    
    data.r10Color = "violet"
    data.h10 = 5
    data.rect10 = [data.rectW*10, data.h10,data.r10Color]
    data.rectangles.append(data.rect10)
    
    data.r11Color = "violet"
    data.h11 = 5
    data.rect11 = [data.rectW*11, data.h11,data.r11Color]
    data.rectangles.append(data.rect11)
    
    data.r12Color = "violet"
    data.h12 = 5
    data.rect12 = [data.rectW*12, data.h12,data.r12Color]
    data.rectangles.append(data.rect12)
    
    data.r13Color = "violet"
    data.h13 = 5
    data.rect13 = [data.rectW*13, data.h13,data.r13Color]
    data.rectangles.append(data.rect13)
    
    data.r14Color = "violet"
    data.h14 = 5
    data.rect14 = [data.rectW*14, data.h14,data.r14Color]
    data.rectangles.append(data.rect14)
    
    data.r15Color = "violet"
    data.h15 = 5
    data.rect15 = [data.rectW*15, data.h15,data.r15Color]
    data.rectangles.append(data.rect15)
    
    data.r16Color = "violet"
    data.h16 = 5
    data.rect16 = [data.rectW*16, data.h16, data.r16Color]
    data.rectangles.append(data.rect16)
            
def mousePressed(event, data):
    # use event.x and event.y
    if (data.mode == "homePage"): 
        homePageMousePressed(event, data)
        
    elif (data.mode == "live"):   
        liveMousePressed(event, data)
        
    elif (data.mode == "select"):       
        selectMousePressed(event,data)

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    if data.mode == "homePage":
        homePageTimerFired(data)
    elif data.mode == "live":
        liveTimerFired(data)
    elif data.mode == "select":
        selectTimerFired(data)

def redrawAll(canvas, data):
    # draw in canvas
    if data.mode == "homePage":
        homePageRedrawAll(canvas, data)
        
    elif data.mode == "live":
        liveRedrawAll(canvas, data)
    elif data.mode == "select":
        selectRedrawAll(canvas, data)
    
    
    

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
    data.timerDelay = 1 # milliseconds
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