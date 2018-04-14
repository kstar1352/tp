import module_manager
module_manager.review()

import pyaudio

import wave

import numpy

import sys

#CHUNK = 1024


def playWav(filename, Chunk = 1024):

    wf = wave.open(filename, 'rb')
    # Instantiate PyAudio.
    p = pyaudio.PyAudio()

    # Open stream.
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(Chunk)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(Chunk)

    # Stop stream.
    stream.stop_stream()
    stream.close()

    # Close PyAudio.
    p.terminate()
    

