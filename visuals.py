# Updated Animation Starter Code

import pyaudio

import numpy as np

import struct


from tkinter import *

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.mode = "homePage"
    data.rectangles = []
    data.rec = True
    
    
    #create 8 rectangles for frequency buckets and change height
    data.rectW= (data.width//2)//8
    
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
    data.rect7 = [data.rectW*7, data.h7,data.r7Color]
    data.rectangles.append(data.rect7)
    
    data.r8Color = "violet"
    data.h8 = 5
    data.rect8 = [data.rectW*8, data.h8,data.r8Color]
    data.rectangles.append(data.rect8)
            
def mousePressed(event, data):
    # use event.x and event.y
    if (data.mode == "homePage"): 
        homePageMousePressed(event, data)
        
    elif (data.mode == "live"):   
        liveMousePressed(event, data)
        
    elif (data.mode == "select"):       
        selectMousePressed(event, data)

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
    
    
######################
#live Mode

######################
def liveMousePressed(event, data):
    x = event.x
    y = event.y
    
    if x > data.width//2:
        data.rec = False
        print("clicked")
        #data.mode = "select"
    pass
    pass
    
def liveKeyPressed(event, data):
    pass
    
    
    
def record(data):
    #instantiate variables
    

    CHUNK = 1024
    FORMAT = pyaudio.paInt32
    CHANNELS = 2
    RATE = 44100
    
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
                        
    if data.rec == True:
        # CHUNK = 1024
        # FORMAT = pyaudio.paInt32
        # CHANNELS = 2
        # RATE = 44100
        # 
        # 
        # p = pyaudio.PyAudio()
        # 
        # stream = p.open(format=FORMAT,
        #                 channels=CHANNELS,
        #                 rate=RATE,
        #                 input=True,
        #                 frames_per_buffer=CHUNK)
                        
        print("* recording")
        
        frames = []
        
        audioData = stream.read(CHUNK)
        
        mult = len(audioData)//CHUNK
        readD = np.array(struct.unpack(str(CHUNK*mult) +"b", audioData))[::2] 
        
        #change to frequency
        freq = np.fft.fft(readD)
        freq = freq[1:len(freq)//2]
        #print("len of freq:", freq)
        # for i in range(len(freq)):
        #     if i < len(freq) //8:
        #         data.rectangles[0][1] += abs(freq[i]//1000)
        #     elif i < len(freq)*2//8:
        #         data.rectangles[1][1] += abs(freq[i]//1000)
        #     elif i < len(freq)*3//8:
        #         data.rectangles[2][1] += abs(freq[i]//1000)
        #     elif i < len(freq)*4//8:
        #         data.rectangles[3][1] += abs(freq[i]//1000)
        #     elif i < len(freq)*5//8:
        #         data.rectangles[4][1] += abs(freq[i]//1000)
        #     elif i < len(freq)*6//8:
        #         data.rectangles[5][1] += abs(freq[i]//1000)
        #     elif i < len(freq)*7//8:
        #         data.rectangles[6][1] += abs(freq[i]//1000)
        #     else:
        #         data.rectangles[7][1] += abs(freq[i]//1000)

        for i in range(len(freq)):
            if i < len(freq) //8:
                data.rectangles[0][1] = 5 + abs(freq[i]//50)
            elif i < len(freq)*2//8:
                data.rectangles[1][1] = 5 + abs(freq[i]//50)
            elif i < len(freq)*3//8:
                data.rectangles[2][1] = 5 + abs(freq[i]//50)
            elif i < len(freq)*4//8:
                data.rectangles[3][1] = 5 + abs(freq[i]//50)
            elif i < len(freq)*5//8:
                data.rectangles[4][1] = 5 + abs(freq[i]//50)
            elif i < len(freq)*6//8:
                data.rectangles[5][1] = 5 + abs(freq[i]//50)
            elif i < len(freq)*7//8:
                data.rectangles[6][1] = 5 + abs(freq[i]//50)
            else:
                data.rectangles[7][1] = 5 + abs(freq[i]//50)
        
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("done recording")
    
def resetRects(data):
    for rect in data.rectangles:
        rect[1] = 5
        
def liveTimerFired(data):
    #this opens the stream everytime timerFired called
    #is this what I want it to do?
    
    #do I also need to do threading here?
    #record for a second then display graphics # repeat for threading
    record(data)
    #resetRects(data)
    if data.rec == False:
        data.mode = "select"
    

def drawRectangles(canvas, data):
    pass
    for rect in data.rectangles:
        canvas.create_rectangle(rect[0] -data.rectW, data.height-rect[1],
                                rect[0], data.height, fill = rect[2])
        
    
    
#create title
def drawLiveTitle(canvas, data):
    canvas.create_text(data.width//2, data.height//6, text = "Live Mode!",
                    font = "Helvetica " + str(data.width//15))

                      
def liveRedrawAll(canvas, data):
    drawLiveTitle(canvas, data)
    drawRectangles(canvas, data)
    

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
    data.timerDelay = 100 # milliseconds
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