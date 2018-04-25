import pyaudio

import numpy as np

import aubio

import struct

import scipy as sc 

from scipy import fftpack

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
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
                        
    if data.rec == True:


        
        frames = []
        
        audioData = stream.read(CHUNK)
        
    
        wavD = np.fromstring(audioData, dtype = np.int16)
        print(wavD[:10],wavD[-10:])
        
        #change to frequency
        # fourier = np.fft.fft(wavD)
        # fourier = fourier.real
        # fourier = np.abs(fourier)
        # fourier = fourier[:len(fourier)//2]
        # print(len(fourier))
        
        #fourier = fftpack.dct(wavD)
        fourier = fftpack.rfft(wavD)
        fourier = fourier.real
        fourier = np.abs(fourier)
        fourier = fourier[:len(fourier)//2]
        print(len(fourier))

        
        print("sum of first bucket: ", sum(fourier[0:128]))
        print("sum of second bucket: ", sum(fourier[128:256]))
        print("sum of third bucket: ", sum(fourier[256:384]))
        print("sum of fourth bucket: ", sum(fourier[384:512]))
        print("sum of fifth bucket: ", sum(fourier[512:640]))
        print("sum of sixth bucket: ", sum(fourier[640:768]))
        print("sum of 7th bucket: ", sum(fourier[768:896]))
        print("sum of last bucket: ", sum(fourier[896:1024]))

        
        #print(fourier[:10], fourier[-128:])
        
        #create freq buckets
        #create freq buckets
        buckets = []
        bucket6 = []
        for i in range(8):
            buckets.append(0)
        
        divisor = 10000
        modVal = len(fourier)//8
        j = -1
        for i in range(len(fourier)):
            if i % modVal == 0:
                j+=1
            # if j == 6:
            #     bucket6.append(fourier[i]//divisor)
            #     print("7th bucket: ", fourier[i]//divisor)
            buckets[j] += fourier[i]//divisor
            data.rectangles[j][1] += fourier[i]//divisor
            
        for i in range(len(buckets)):
            print("bucket "+ str(i+1)+ " : ", buckets[i])
        
        
            
        
                
        
    
    
            
 
        
        
        ###change something for the pitch
        
        
        #to find volume possibly
        #volume = num.sum(samples**2)/len(samples)
        # Format the volume output so that at most
        # it has six decimal numbers.
        #volume = "{:.6f}".format(volume)

        
        # #change to frequency
        # fourier = np.fft.fft(intD[::3])
        # #fourier = np.fft.fft(readD[::3])
        # fourier = fourier.real
        
        #print(intD)
        #print("len of fourier:", len(fourier))
        # 
        # max1 = 10000
        # max2 = 1000000


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
        
        # for i in range(len(fourier)):
        #     if i < len(fourier)//8:
        #         data.rectangles[0][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*2//8:
        #         data.rectangles[1][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*3//8:
        #         data.rectangles[2][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*4//8:
        #         data.rectangles[3][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*5//8:
        #         data.rectangles[4][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*6//8:
        #         data.rectangles[5][1] += 2*abs(fourier[i]//max2)
        #     elif i < len(fourier)*7//8:
        #         data.rectangles[6][1] += 2*abs(fourier[i]//max2)
                
        
        #PITCH DETECTION
        pDetection = aubio.pitch("default", CHUNK,
            CHUNK, RATE)
            
        # Set unit.
        pDetection.set_unit("midi")
        pDetection.set_silence(-40)
        pDetection.set_tolerance(.6)
                
        pitchSamples = np.fromstring(audioData, dtype = aubio.float_type)
        pitch = pDetection(pitchSamples)[0]
        
        data.pitch = pitch
        
        if data.pitch>110:
            data.backColor = "cyan"
        
        if data.pitch >105:
            data.backColor = "azure"
        elif data.pitch > 95:
            data.backColor = "deep sky blue"
        elif data.pitch > 88:
            data.backColor = "medium spring green"
        elif data.pitch > 81:
            data.backColor = "purple2"
        elif data.pitch > 75:
            data.backColor = "goldenrod1"
        elif data.pitch > 68:
            data.backColor = "firebrick4"
        else:
            data.backColor = "gray1"
            
        print(pitch)
        
    stream.stop_stream()
    stream.close()
    p.terminate()
    #print("done recording")
    
    
def resetRects(canavs, data):
    for rect in data.rectangles:
        canavs.create_rectangle(rect[0]-data.rectW, data.height-5, 
                                rect[0], data.height, fill = rect[2])
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
    
    
#create title
def drawLiveTitle(canvas, data):
    canvas.create_text(data.width//2, data.height//6, text = "Live Mode!",
                    font = "Helvetica " + str(data.width//15), 
                    fill = data.liveTitleC)

                      
def liveRedrawAll(canvas, data):
    drawBackground(canvas, data)
    drawLiveTitle(canvas, data)
    drawRectangles(canvas, data)
    resetRects(canvas,data)