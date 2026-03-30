from flask import Flask, request, jsonify, Response
from picamera2 import Picamera2
import cv2

app = Flask(__name__)
picam2 = Picamera2()

picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Detection Result:", data)
    return jsonify({"status": "success"})

@app.route('/')
def home():
    return "Camera Stream Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
