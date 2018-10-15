# capturing to a PIL Image

from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

stream = BytesIO()
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture(stream,format='jpeg')
stream.seek(0)
image = Image.open(stream)
image.save('pilImage.jpeg')
