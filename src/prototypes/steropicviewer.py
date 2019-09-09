import numpy as np
import cv2

from picamera import PiCamera

try:
    camera = PiCamera(stereo_mode='side-by-side', resolution=(1280,720))
    # Uncomment following lines if your images are upside down
    camera.rotation = 180
    camera.capture('captures/foo.jpg')
    img = cv2.imread('captures/foo.jpg',0)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

finally:
    camera.close()
