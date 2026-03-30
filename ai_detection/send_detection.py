import cv2
import requests
from ultralytics import YOLO

video_url = "http://YOUR_PI_IP:5000/video_feed"
pi_url = "http://YOUR_PI_IP:5000/receive_data"

model = YOLO("yolov8n.pt")
capture = cv2.VideoCapture(video_url)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    results = model(frame)

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            requests.post(pi_url, json={"object": label})

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
