#!/usr/local/bin/python3
"""
visualize audio from alsa default device and output on raspberry gpio pins
used "Realtime Audio Visualization In Python" as basis from
https://www.swharden.com/wp/2016-07-19-realtime-audio-visualization-in-python/
"""
import pyaudio
import numpy as np

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges. \
         You can achieve this by using 'sudo' to run your script")

def main():
    """ do all the audio processing and set the GPIO pins"""
    initGPIO()

    maxValue = 2**16
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=22050,
                input=True, frames_per_buffer=1048)

    buffersize = 20
    lastPeaks = [0] * buffersize
    i = buffersize #overflow in first run, so achtually start with 0

    try:
        while True:
            data = np.fromstring(stream.read(1048),dtype=np.int16)
            tmp_peak = np.abs(np.max(data)-np.min(data))/maxValue
            i+=1
            if i >= buffersize:
                i=0
            lastPeaks[i] = tmp_peak
          
            fourth = (sum(lastPeaks)/len(lastPeaks))/4
            level = int((tmp_peak) / fourth)-1

            #different reaction setting
            #fourth = max(lastPeaks) /4
            #level = int((tmp_peak*1.25) / fourth)-1

            setLED(level)
    except KeyboardInterrupt:
        pass


def initGPIO():
    """initalize and setup rpi gpio-pins"""
    #setup gpio's
    # to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)

    #green 11
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, GPIO.LOW)

    #orange 13
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(13, GPIO.LOW)

    #red 15
    GPIO.setup(15, GPIO.OUT)
    GPIO.output(15, GPIO.LOW)

def setLED(val):
    if val == 1:
        #led green
        GPIO.output(11, GPIO.HIGH)#green
        GPIO.output(13, GPIO.LOW)#orange
        GPIO.output(15, GPIO.LOW)#red
        print ("#")
    elif val == 2:
        #led green & orange
        GPIO.output(11, GPIO.HIGH)#green
        GPIO.output(13, GPIO.HIGH)#orange
        GPIO.output(15, GPIO.LOW)#red
        print ("##")
    elif val == 3:
        #led green & orange & red 
        GPIO.output(11, GPIO.HIGH)#green
        GPIO.output(13, GPIO.HIGH)#orange
        GPIO.output(15, GPIO.HIGH)#red
        print ("###")
    else:
        #all leds off
        GPIO.output(11, GPIO.LOW)#green
        GPIO.output(13, GPIO.LOW)#orange
        GPIO.output(15, GPIO.LOW)#red

if __name__ == "__main__":
    main()