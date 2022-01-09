from flask import Flask, Response, render_template
import cv2
from camera import gen

app = Flask(__name__)
# MacBookProの内蔵カメラ = 1
video = cv2.VideoCapture(1)

@app.route('/')
def index():
    global isFace
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333, threaded=True)