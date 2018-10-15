# capture stream and close

from time import sleep
from picamera import PiCamera

# open stream
my_image = open('my_image.jpg','wb')
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture(my_image,resize=(320,240))
my_image.close()
