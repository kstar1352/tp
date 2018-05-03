

# def play(filename, data):
#     
#     CHUNK = 512
#     wf = wave.open(filename, 'rb')
#     p = pyaudio.PyAudio()
#     
#     # define callback (2)
#     def callback(in_data, frame_count, time_info, status):
#         audioD = wf.readframes(frame_count)
#         #trying to use threading here but is it the right place?
#         # t1 = threading.Thread(target = getFourier, args = (audioD, data))
#         # t2 = threading.Thread(target = beat, args = (audioD, data))
#         # t3 = threading.Thread(target = getRotSpeed, args = (audioD, data))
#         # 
#         # t1.daemon = True
#         # t2.daemon = True
#         # t3.daemon = True
#         # 
#         # t1.start()
#         # t2.start()
#         # t3.start()
#         # 
#         # t1.join()
#         # t2.join()
#         # t3.join()
#         getFourier(audioD, data)
#         beat(audioD, data)
#         getRotSpeed(audioD, data)
#         
#         return (audioD, pyaudio.paContinue)
# 
# 
#     # open stream using callback (3)
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                     channels=wf.getnchannels(),
#                     rate=wf.getframerate(),
#                     output=True,
#                     stream_callback=callback)
#                     
#     # start the stream (4)
#     stream.start_stream()
#     
#     # wait for stream to finish (5)
#     while stream.is_active():
#         time.sleep(.1)
#     
#     
#     # stop stream (6)
#     stream.stop_stream()
#     stream.close()
#     wf.close()
#         
#     # close PyAudio (7)
#     p.terminate()


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


# def callback(in_data, frame_count, time_info, status):
#     global dat
#     
#     data = dat
#     
#     
#     audioD = wf.readframes(frame_count)
#     
#     
#     p = data.p
#     stream = data.stream
#     
#     getFourier(audioD, data)
#     beat(audioD, data)
#     getRotSpeed(audioD, data)


# def play(filename, data):
#     pass
    
    
    # global wf
    # wf = wave.open("songs/"+data.song)
    # data.p = pyaudio.PyAudio()
    # 
    # p = data.p
    # data.stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
    #                      channels=wf.getnchannels(),
    #                      rate=wf.getframerate(),
    #                      output=True,
    #                      stream_callback = callback)
                         
                         
       
    #("songs/"+data.song, data)