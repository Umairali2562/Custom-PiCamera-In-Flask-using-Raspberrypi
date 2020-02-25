from flask import Flask, redirect, url_for, request
from flask import Flask, render_template, Response
import picamera
from picamera.array import PiRGBArray
from cameraa import VideoCamera
from picamera import PiCamera
from cameraa import VideoCamera
import cv2
import time
import socket
import io
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip=s.getsockname()[0]
s.close()
text="http://"
ip=text+ip

app = Flask(__name__)

@app.route('/')
def hello():
    #return "Hello World!"
    return render_template('index.html')

def gen(cameraa):
    while True:
            frame = cameraa.get_frame()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video')
def video_feed():
    
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['capture']
      
      camera = picamera.PiCamera()
      camera.capture('/root/Desktop/Umair/new/image.jpg')
      camera.close()
      
    
      return redirect(ip, code=302)

   else:
      user = request.args.get('capture')
      return redirect(ip, code=302)
if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')