# 开启摄像头并且进行录像将其保存到名为“file.h264”的文件中

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024,768)
camera.start_preview()
sleep(2)
camera.capture("foo.jpg")
