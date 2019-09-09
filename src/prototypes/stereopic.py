from picamera import PiCamera

try:
    camera = PiCamera(stereo_mode='side-by-side', resolution=(1280,720))
    # Uncomment following lines if your images are upside down
    camera.rotation = 180
    camera.capture('captures/foo.jpg')
finally:
    camera.close()
