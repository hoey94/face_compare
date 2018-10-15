import picamera
import picamera.array
import time

with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.framerate = 30
    print ("start preview direct from GPU")
    camera.start_preview()
    while(1):
        a = 1
