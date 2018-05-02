import pyaudio

import numpy as np

import aubio

import struct

import scipy as sc 

from scipy import fftpack

import threading
from queue import Queue
import time 

import random

import math


######################
#live Mode

######################

def liveMousePressed(event, data):
    x = event.x
    y = event.y
    
    if x > data.width-40 and y < 40:
        data.mode = "homePage"
    
    pass
    pass
    
def liveKeyPressed(event, data):
    pass
    
    
def getFourier(audio, data):
    audioD = audio
    #FFT STUFF
    wavD = np.fromstring(audioD, dtype = np.int16)
    
    #change to frequency
    #fourier = fftpack.rfft(wavD)
    fourier = fftpack.dct(wavD)
    fourier = np.abs(fourier)
    fourier = fourier[:len(fourier)//2]

    
    #create freq buckets
    buckets = []
    for i in range(10):
        buckets.append(0)
    
    #divisor for dct and int16 = 100000, increase for int 32
    divisor = 100000
    
    #divide by number of buckets
    modVal = (len(fourier)//10) +1
    #start at -1 since at 0 j will increase by 1
    j = -1
    for i in range(len(fourier)):
        if i % modVal == 0:
            j+=1
        # print(j)
        buckets[j] += fourier[i]//divisor
        data.rectangles[j][1] += fourier[i]//divisor
        
    
    



  
def getRotSpeed(audio, data):
    audioD = audio
    wavD = np.fromstring(audioD, dtype = np.int16)
    
    speed = np.abs(wavD)
    speed = np.sum(speed)
    data.speed = speed//100000
    data.radius = speed//9000 
    
    if data.radius > 150:
        data.radius = 150
        data.RCI +=1   
 
  
def beat(audio, data):
    audioD = audio
    wavD = np.fromstring(audioD, dtype = np.int16)

    #beat detection
    currentBeat = np.abs(wavD)
    currentBeat = np.sum(currentBeat)
    #print(currentBeat)
    
    data.averageBeat.append(currentBeat)
    
    #keep recent history of the song
    if len(data.averageBeat) > 20:
        data.averageBeat.pop(0)

    
    maxR = min(data.width//40, data.height//30)
    
    
    data.beatCr = np.abs(currentBeat//300000)
    
    if data.beatCr +3 > maxR:
        data.rows = 15
        data.cols = 20
        data.beatCr = maxR -3
    elif data.beatCr < 2:
        data.beatCr = 0
    else:
        data.rows = 15
        data.cols = 20
        
        
      
      #beat through just a single monetary value  
#     wav = np.fromstring(audio, dtype = np.int16)
#     averageBeat = 100000
#     currentBeat = np.abs(wav)
#     currentBeat = np.sum(wav)
#     if currentBeat > averageBeat:
#         print("Beat: ", currentBeat)
#         data.beatCr = currentBeat//1000
    
    
def record(data):
    #instantiate variables

    if data.rec == True:

        CHUNK = 512 
        #need it to be float for pitch, but int for frequencies
        #FORMAT = pyaudio.paFloat32
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        
        
        p = pyaudio.PyAudio()
        
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        
        frames = []
        
        audioData = stream.read(CHUNK)
        
        wavD = np.fromstring(audioData, dtype = np.int16)
        
        #analyze functions

        
        
        t1 = threading.Thread(target = getFourier, args = (audioData, data))
        t2 = threading.Thread(target = beat, args = (audioData, data))
        t3 = threading.Thread(target = getRotSpeed, args = (audioData, data))
        
        t1.daemon = True
        t2.daemon = True
        t3.daemon = True
        
        t1.start()
        t2.start()
        t3.start()
        
        t1.join()
        t2.join()
        t3.join()
        
    


        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        

    ## uncomment below to include laggy pitch detection

   #       CHUNK = 1024 
    #     #need it to be float for pitch, but int for frequencies
    #     #FORMAT = pyaudio.paFloat32
    #     pFORMAT = pyaudio.paFloat32
    #     CHANNELS = 1
    #     RATE = 44100
    #     
    #     
    #     p = pyaudio.PyAudio()
    #     
    #     stream = p.open(format=pFORMAT,
    #                     channels=CHANNELS,
    #                     rate=RATE,
    #                     input=True,
    #                     frames_per_buffer=CHUNK)
    #     
    #     
    #     pitchData = stream.read(CHUNK)
    #     
    #     #PITCH DETECTION
    #     pDetection = aubio.pitch("default", CHUNK,
    #          CHUNK, RATE)
    #     #     
    #     # # Set unit.
    #     pDetection.set_unit("midi")
    #     pDetection.set_silence(-40)
    #     pDetection.set_tolerance(.4)
    #     #         
             
    #     pitchSamples = np.fromstring(pitchData, dtype = aubio.float_type)
    #     # 
    #     pitch = pDetection(pitchSamples)[0]
    #     # 
    #     data.pitch = pitch
    #     # 
    #     if data.pitch>110:
    #         data.backColor = "cyan"
    #     # 
    #     if data.pitch >105:
    #         data.backColor = "azure"
    #     elif data.pitch > 95:
    #         data.backColor = "deep sky blue"
    #     elif data.pitch > 88:
    #         data.backColor = "medium spring green"
    #     elif data.pitch > 81:
    #         data.backColor = "purple2"
    #     elif data.pitch > 75:
    #         data.backColor = "goldenrod1"
    #     elif data.pitch > 68:
    #         data.backColor = "firebrick4"
    #     else:
    #         data.backColor = "gray1"
    #         
    #     
    # stream.stop_stream()
    # stream.close()
    # p.terminate()
    #print("done recording")
    
    
def resetRects(canavs, data):
    i = 0
    for rect in data.rectangles:
        rect[1] = 5
        canavs.create_rectangle(rect[0]-data.rectW, data.height-5, 
                                rect[0], data.height, fill = data.rectColor[i], width = 0)
        i+=1
        # rect[1] = 5
        
def liveTimerFired(data):
    #this opens the stream everytime timerFired called
    #is this what I want it to do?
    
    #do I also need to do threading here?
    #record for a second then display graphics # repeat for threading
    record(data)
    
    if data.rec == False:
        data.mode = "select"
        
def drawRotating(canvas, data):
    
    
    if data.radius < 30:
        canvas.create_oval(data.width*3//4-data.smallR, data.height//2-data.smallR,
                           data.width*3//4+data.smallR, data.height//2+data.smallR,
                           fill = data.rotColor[data.RCI%10])
                        
    else:
        data.smallR = data.radius//5
        for i in range(len(data.rotCircles)):
            canvas.create_oval((data.width*3//4-data.radius*math.cos(data.rotCircles[i][2]))-data.smallR,
                            (data.height//2 - data.radius*math.sin(data.rotCircles[i][2]))-data.smallR,
                            (data.width*3//4-data.radius*math.cos(data.rotCircles[i][2]))+data.smallR,
                            (data.height//2 - data.radius*math.sin(data.rotCircles[i][2]))+data.smallR,
                            fill = data.rotColor[data.RCI%10])
                            
        for circ in data.rotCircles:
            circ[2] += data.speed


def drawRectangles(canvas, data):
    pass
    i = 0
    for rect in data.rectangles:
        canvas.create_rectangle(rect[0] -data.rectW, data.height-rect[1],
                                rect[0], data.height, fill = data.rectColor[i])
        i+= 1
def drawBackground(canvas, data):
    canvas.create_rectangle(0,0, data.width, data.height, fill = data.backColor)
    
def drawBeat(canvas, data):
    for i in range(data.rows-3):
        for j in range(data.cols//2):
            canvas.create_oval(j*data.width//20 + data.width//40 -  data.beatCr,
                               i*data.height//15+ data.height//30 - data.beatCr,
                               j*data.width//20 + data.width//40 +  data.beatCr,
                               i*data.height//15+ data.height//30 + data.beatCr,
                               fill = data.Colors[i%6][j])
                    
            
            # canvas.create_oval(data.width *j//cols + data.circleM, 
            #                    data.height*i//10+data.circleM, 
            #                    data.width*(j+1)//cols+data.circleM,
            #                    data.height*(i+1)//10, 
            #                    fill = data.Colors[random.randint(0, 381)])
                               
    
    
#create title
# def drawLiveTitle(canvas, data):
#     canvas.create_text(data.width//2, data.height//6, text = "Live Mode!",
#                     font = "Helvetica " + str(data.width//15), 
#                     fill = data.liveTitleC)

                      
def liveRedrawAll(canvas, data):
    drawBackground(canvas, data)
    #drawLiveTitle(canvas, data)
    drawBeat(canvas,data)
    drawRotating(canvas, data)
    drawRectangles(canvas, data)
    resetRects(canvas,data)
    