import cv2
import picamera
from picamera.array import PiRGBArray
import time


class VideoCamera(object):

    def __init__(self):
        self.camera = picamera.PiCamera()
        self.rawCapture = PiRGBArray(self.camera)
        self.car_cascade = cv2.CascadeClassifier('cars.xml')
        #self.video = cv2.VideoCapture('/root/Desktop/flask/virtualenv/project_env/car.mp4')   #cv2.VideoCapture(0)

    def __del__(self):
        self.camera.close()

    def get_frame(self):
        self.last_access = time.time()
        self.rawCapture.truncate(0)
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            ret, jpeg = cv2.imencode('.jpg', image)
            if time.time() - self.last_access > 1:
                self.camera.closed
                break
            return jpeg.tobytes()