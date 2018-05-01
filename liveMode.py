

import pyaudio

import numpy as np

import aubio

import struct

import scipy as sc 

from scipy import fftpack

import threading
from queue import Queue
import time 



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

    
    # #beat detection
    # currentBeat = np.abs(wavD)
    # currentBeat = np.sum(wavD)
    # 
    # data.averageBeat.append(currentBeat)
    # 
    # #keep recent history of the song
    # if len(data.averageBeat) > 15:
    #     data.averageBeat.pop(0)
    #     
    # #print(np.average(data.averageBeat))
    # if currentBeat > np.average(data.averageBeat):
    #     data.beatCr = currentBeat//1000
    
    #create freq buckets
    buckets = []
    for i in range(8):
        buckets.append(0)
    
    #divisor for dct and int16 = 100000, increase for int 32
    divisor = 100000
    
    #divide by number of buckets
    modVal = len(fourier)//8
    #start at -1 since at 0 j will increase by 1
    j = -1
    for i in range(len(fourier)):
        if i % modVal == 0:
            j+=1
        buckets[j] += fourier[i]//divisor
        data.rectangles[j][1] += fourier[i]//divisor
        
    
    
    #to find volume possibly
    #volume = num.sum(samples**2)/len(samples)
    # Format the volume output so that at most
    # it has six decimal numbers.
    #volume = "{:.6f}".format(volume)




    #for now instead of threading
    # for i in range(len(fourier)):
    #     if i < len(fourier)//16:
    #         data.rectangles[0][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*2//16:
    #         data.rectangles[1][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*3//16:
    #         data.rectangles[2][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*4//16:
    #         data.rectangles[3][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*5//16:
    #         data.rectangles[4][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*6//16:
    #         data.rectangles[5][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*7//16:
    #         data.rectangles[6][1] += 2*abs(fourier[i]//max2)
    #         
    #     elif i < len(fourier)*8//16:
    #         data.rectangles[7][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*9//16:
    #         data.rectangles[8][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*10//16:
    #         data.rectangles[9][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*11//16:
    #         data.rectangles[10][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*12//16:
    #         data.rectangles[11][1] += 2*abs(fourier[i]//max2)
    #     elif i < len(fourier)*13//16:
    #         data.rectangles[12][1] += 2*abs(fourier[i]//max2)
    #         
    #     elif i < len(fourier)*14//16:
    #         data.rectangles[13][1] +=  2*abs(fourier[i]//max1)
    #     elif i < len(fourier)*15//16:
    #         data.rectangles[14][1] += 2*abs(fourier[i]//max1)
    #     else:
    #         data.rectangles[15][1] += 2*abs(fourier[i]//max1)
  
def beat(audio, data):
    audioD = audio
    wavD = np.fromstring(audioD, dtype = np.int16)

    #beat detection
    currentBeat = np.abs(wavD)
    currentBeat = np.sum(wavD)
    
    data.averageBeat.append(currentBeat)
    
    #keep recent history of the song
    if len(data.averageBeat) > 15:
        data.averageBeat.pop(0)
        
    #print(np.average(data.averageBeat))
    if currentBeat > np.average(data.averageBeat):
        data.beatCr = currentBeat//1000
        
      
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

        CHUNK = 1024 
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
        
        #analyze functions
        getFourier(audioData, data)
        beat(audioData, data)

        
        
        #to find volume possibly
        #volume = num.sum(samples**2)/len(samples)
        # Format the volume output so that at most
        # it has six decimal numbers.
        #volume = "{:.6f}".format(volume)

        
        #for now instead of threading
        # for i in range(len(fourier)):
        #     if i < len(fourier)//16:
        #         data.rectangles[0][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*2//16:
        #         data.rectangles[1][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*3//16:
        #         data.rectangles[2][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*4//16:
        #         data.rectangles[3][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*5//16:
        #         data.rectangles[4][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*6//16:
        #         data.rectangles[5][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*7//16:
        #         data.rectangles[6][1] += 2*abs(fourier[i]//max2)
        #         
        #     elif i < len(fourier)*8//16:
        #         data.rectangles[7][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*9//16:
        #         data.rectangles[8][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*10//16:
        #         data.rectangles[9][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*11//16:
        #         data.rectangles[10][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*12//16:
        #         data.rectangles[11][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*13//16:
        #         data.rectangles[12][1] += 2*abs(fourier[i]//max2)
        #         
        #     elif i < len(fourier)*14//16:
        #         data.rectangles[13][1] +=  2*abs(fourier[i]//max1)
        #     elif i < len(fourier)*15//16:
        #         data.rectangles[14][1] += 2*abs(fourier[i]//max1)
        #     else:
        #         data.rectangles[15][1] += 2*abs(fourier[i]//max1)
        
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
    #  
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
    for rect in data.rectangles:
        canavs.create_rectangle(rect[0]-data.rectW, data.height-5, 
                                rect[0], data.height, fill = rect[2], width = 0)
        rect[1] = 5
        
def liveTimerFired(data):
    #this opens the stream everytime timerFired called
    #is this what I want it to do?
    
    #do I also need to do threading here?
    #record for a second then display graphics # repeat for threading
    record(data)
    
    if data.rec == False:
        data.mode = "select"
    

def drawRectangles(canvas, data):
    pass
    for rect in data.rectangles:
        canvas.create_rectangle(rect[0] -data.rectW, data.height-rect[1],
                                rect[0], data.height, fill = rect[2])
        # if rect[1] <= 40:
        #     canvas.create_rectangle(rect[0] -data.rectW, data.height-5,
        #                         rect[0], data.height, fill = rect[2])
        # else:
        #     canvas.create_rectangle(rect[0] -data.rectW, data.height-rect[1],
        #                         rect[0], data.height, fill = rect[2])
        
def drawBackground(canvas, data):
    canvas.create_rectangle(0,0, data.width, data.height, fill = data.backColor)
    
def drawBeat(canvas, data):
    canvas.create_oval(data.beatCx-data.beatCr, data.beatCy-data.beatCr, 
                       data.beatCx+data.beatCr, data.beatCy+data.beatCr,
                       fill = "Red")
    
    
#create title
def drawLiveTitle(canvas, data):
    canvas.create_text(data.width//2, data.height//6, text = "Live Mode!",
                    font = "Helvetica " + str(data.width//15), 
                    fill = data.liveTitleC)

                      
def liveRedrawAll(canvas, data):
    drawBackground(canvas, data)
    drawLiveTitle(canvas, data)
    drawRectangles(canvas, data)
    drawBeat(canvas,data)
    resetRects(canvas,data)
    