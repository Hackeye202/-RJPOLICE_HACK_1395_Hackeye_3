import cv2
import numpy as np
from datetime import datetime
from tensorflow.keras.models import load_model
import sys
import os
sys.path.insert(1, 'ai_models/')
import mysql_crime_insert
import requests

output_directory = 'dashboard/videos/crimes'
thumbnail_output_directory = 'dashboard/videos/crimes/thumbnails/'
clip_duration = 10
fps = 8
os.makedirs(output_directory, exist_ok=True)

loaded_model = load_model('ai_models/Fire/fire_detection_model.h5')

def preprocess_frame_for_prediction(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = np.expand_dims(frame, axis=0) / 255.0
    return frame

cap = cv2.VideoCapture(0)

camera_no = 1
camera_name = "Webcam"
camera_loc = "Entrance"
type_of_crime = "Fire"
detection_count = 0

frames_list = []
start_time = None

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    preprocessed_frame = preprocess_frame_for_prediction(frame)

    prediction = loaded_model.predict(preprocessed_frame)

    if prediction[0, 0] > 0.5:
        detection_count += 1

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_datetime = datetime.now()
        detection_info = {
            'date': current_time.split(' ')[0],
            'time': current_time.split(' ')[1],
            'camera_no': camera_no,
            'camera_name': camera_name,
            'camera_loc': camera_loc,
            'type_of_crime': type_of_crime,
            'detection_count': detection_count
        }

        if len(frames_list) > 0:
            out_filename = os.path.join(output_directory, f"{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.mp4")
            out = cv2.VideoWriter(out_filename, cv2.VideoWriter_fourcc(*'avc1'), fps, (frame.shape[1], frame.shape[0]))
            for saved_frame in frames_list:
                out.write(saved_frame)
            out.release()

        thumbnail_filename = os.path.join(thumbnail_output_directory, f"{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}-thumbnail.jpg")
        cv2.imwrite(thumbnail_filename, frame)

        cap.release()
        cv2.destroyAllWindows()

        print(detection_info)
        mysql_crime_insert.insert_into_crime(list(detection_info.values()))
        print("SQL Entry successful.")
        print("Video and Thumbnail Saved Successfully.")
        requests.post("https://ntfy.sh/hackeye_hackathon",data="Fire Detected".encode(encoding='utf-8'))
        print("Notification Sent.")
        break

    cv2.imshow('Fire Detection', frame)
    frames_list.append(frame)
    
    if len(frames_list) > clip_duration * fps:
        frames_list.pop(0)

    if start_time is None:
        start_time = datetime.now()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
