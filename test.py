from picamera2 import Picamera2, Preview
import time
picam2 = Picamera2()
config = picam2.create_preview_configuration()
picam2.configure(config)
picam2.start()
time.sleep(2)
picam2.stop_preview()
picam2.start_preview(True)
time.sleep(200)