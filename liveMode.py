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
        data.stream.stop_stream()
        data.stream.close()
        data.p.terminate()
        data.mode = "homePage"
    
    pass
    pass
    
def liveKeyPressed(event, data):
    pass
    
    
def getLiveFourier(audio, data):
    audioD = audio
    #FFT STUFF
    wavD = np.fromstring(audioD, dtype = np.int16)
    if len(wavD)==0:
        return None
    
    #change to frequency
    fourier = fftpack.rfft(wavD)
    #fourier = fftpack.dct(wavD)
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
        
    
def getFourier(audio, data):
    audioD = audio
    #FFT STUFF
    wavD = np.fromstring(audioD, dtype = np.int16)
    if len(wavD)==0:
        return None
    
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
    divisor1 =3000000
    divisor = 1000000
    
    #divide by number of buckets
    modVal = (len(fourier)//10) +1
    #start at -1 since at 0 j will increase by 1
    j = -1
    for i in range(len(fourier)):
        if i % modVal == 0:
            j+=1
        # print(j)
        if j == 0:
            buckets[j] += fourier[i]//divisor1
            data.rectangles[j][1] += fourier[i]//divisor1 
            
        else:
            buckets[j] += fourier[i]//divisor
            data.rectangles[j][1] += fourier[i]//divisor    



  
def getLiveRotSpeed(audio, data):
    audioD = audio
    wavD = np.fromstring(audioD, dtype = np.int16)
    
    speed = np.abs(wavD)
    speed = np.sum(speed)
    
    data.radius = speed//60000 
    data.speed = data.radius/130
    #data.speed = speed//100000
    
    if data.radius > 150:
        data.radius = 150
        data.RCI +=1   
 
 
def getRotSpeed(audio, data):
    audioD = audio
    wavD = np.fromstring(audioD, dtype = np.int16)
    
    speed = np.abs(wavD)
    speed = np.sum(speed)
    
    data.radius = speed//350000
    data.speed = data.radius/100
    #data.speed = speed//30000000
    
    if data.radius > 150:
        data.radius = 150
        data.RCI +=1   
  
def liveBeat(audio, data):
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
    
    
    data.beatCr = np.abs(currentBeat//400000)
    
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
    
    
    data.beatCr = np.abs(currentBeat//3000000)
    
    if data.beatCr +3 > maxR:
        data.rows = 15
        data.cols = 20
        data.beatCr = maxR -3
    elif data.beatCr < 2:
        data.beatCr = 0
    else:
        data.rows = 15
        data.cols = 20
    
    

    
def record(data):
    #instantiate variables

    if data.rec == True:

        CHUNK = 512 
        #need it to be float for pitch, but int for frequencies
        #FORMAT = pyaudio.paFloat32
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        
        
        data.p = pyaudio.PyAudio()
        
    
        
        data.stream = data.p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        
        frames = []
        
        audioData = data.stream.read(CHUNK)
        
        wavD = np.fromstring(audioData, dtype = np.int16)
        
        #analyze functions

        
        
        t1 = threading.Thread(target = getLiveFourier, args = (audioData, data))
        t2 = threading.Thread(target = liveBeat, args = (audioData, data))
        t3 = threading.Thread(target = getLiveRotSpeed, args = (audioData, data))
        
        t1.daemon = True
        t2.daemon = True
        t3.daemon = True
        
        t1.start()
        t2.start()
        t3.start()
        
        t1.join()
        t2.join()
        t3.join()
        
    


        
        data.stream.stop_stream()
        data.stream.close()
        data.p.terminate()
        
    
    
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
    
    
    #record(data)
    
    if data.rec == False:
        data.mode = "select"
        
def drawRotating(canvas, data):
    
    min = 15
    
        
    if data.radius <= 30:
        canvas.create_oval(data.width*3//4-min, data.height//2-min,
                           data.width*3//4+min, data.height//2+min,
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
    
    if data.radius >= 120:
        smallerCirc = data.radius/2
        smallerR = smallerCirc//5
        for times in range(2):
            for i in range(len(data.rotCircles)):
                canvas.create_oval((data.width*3//4-smallerCirc*math.cos(data.rotCircles[i][2]))-smallerR,
                                (data.height//2 - smallerCirc*math.sin(data.rotCircles[i][2]))-smallerR,
                                (data.width*3//4-smallerCirc*math.cos(data.rotCircles[i][2]))+smallerR,
                                (data.height//2 - smallerCirc*math.sin(data.rotCircles[i][2]))+smallerR,
                                fill = data.rotColor[data.RCI%10])
            smallerCirc -= 40
            smallerR -= smallerCirc//5
                            
    elif data.radius >= 80:
        smallerCirc = data.radius/2
        smallerR = smallerCirc//5
        for i in range(len(data.rotCircles)):
            canvas.create_oval((data.width*3//4-smallerCirc*math.cos(data.rotCircles[i][2]))-smallerR,
                            (data.height//2 - smallerCirc*math.sin(data.rotCircles[i][2]))-smallerR,
                            (data.width*3//4-smallerCirc*math.cos(data.rotCircles[i][2]))+smallerR,
                            (data.height//2 - smallerCirc*math.sin(data.rotCircles[i][2]))+smallerR,
                            fill = data.rotColor[data.RCI%10])

def drawRectangles(canvas, data):
    pass
    i = 0
    for rect in data.rectangles:
        if rect[1] > 60:
            rect[1] = 60
        canvas.create_rectangle(rect[0] -data.rectW, data.height-rect[1],
                                rect[0], data.height, fill = data.rectColor[i])
        i+= 1
        
        
def drawBackground(canvas, data):
    if data.radius ==150:
        canvas.create_rectangle(0,0, data.width+5, data.height+5, fill = data.rotColor[data.RCI%10])
    else:
        canvas.create_rectangle(0,0, data.width+5, data.height+5, fill = data.backColor)
    
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
                               
    
    

                      
def liveRedrawAll(canvas, data):
    drawBackground(canvas, data)
    drawBeat(canvas,data)
    drawRotating(canvas, data)
    drawRectangles(canvas, data)
    resetRects(canvas,data)
    