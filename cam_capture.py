import time
from picamera2 import Picamera2, Preview

def camstart():
    picam2 = Picamera2()

    preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
    picam2.configure(preview_config)

    picam2.start_preview(Preview.QT)

    picam2.start()
    time.sleep(2)

    metadata = picam2.capture_file("test.jpg")
    picam2.close()