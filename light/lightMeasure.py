from picamera import PiCamera
from time import sleep

camera = PiCamera()

def take_photo(name):
    camera.start_preview()
    sleep(1.5)
    camera.capture("/home/gr106/Downloads/light-main/scripts/" + name + ".jpeg")
    camera.stop_preview()
take_photo('blue_gallogen')