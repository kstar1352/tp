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


from tkinter import *

####################################
# customize these functions
####################################

def init(data):

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




    
    
    
    # data.Colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    # 'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    # 'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    # 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    # 'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    # 'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    # 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    # 'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    # 'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    # 'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    # 'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    # 'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    # 'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    # 'indian red', 'saddle brown', 'sandy brown',
    # 'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    # 'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    # 'pale violet red', 'maroon', 'medium violet red', 'violet red',
    # 'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    # 'thistle', 'snow2', 'snow3',
    # 'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    # 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    # 'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    # 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    # 'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    # 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    # 'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    # 'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    # 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    # 'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    # 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    # 'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    # 'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    # 'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    # 'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    # 'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    # 'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    # 'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    # 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    # 'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    # 'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    # 'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    # 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    # 'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    # 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    # 'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    # 'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    # 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    # 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    # 'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    # 'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    # 'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    # 'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    # 'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    # 'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    # 'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    # 'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    # 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    # 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    # 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    # 'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    # 'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    # 'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    # 'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    # 'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    # 'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',]
    

    
    
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
    pass

def timerFired(data):
    if data.mode == "homePage":
        homePageTimerFired(data)
    elif data.mode == "live":
        liveTimerFired(data)
    elif data.mode == "select":
        selectTimerFired(data)
    elif data.mode == "playMode":
        playModeTimerFired(data)

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