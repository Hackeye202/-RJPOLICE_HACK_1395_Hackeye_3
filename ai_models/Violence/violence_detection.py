import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from datetime import datetime
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

model = tf.keras.models.load_model("ai_models/Violence/violence_detection_model.h5")

frames_list = []
start_time = None

def predict_and_get_info(frame, camera_no, camera_name, camera_loc):
    result = {}

    resized_frame = cv2.resize(frame, (64, 64))

    img_array = np.expand_dims(resized_frame, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)

    current_datetime = datetime.now()
    result['date'] = current_datetime.strftime("%Y-%m-%d")
    result['time'] = current_datetime.strftime("%H:%M:%S")

    result['camera_no'] = camera_no
    result['camera_name'] = camera_name
    result['camera_loc'] = camera_loc

    result['type_of_crime'] = 'violence_detected' if prediction[0] >= 0.5 else 'no_violence'

    result['detection_count'] = 1 if prediction[0] >= 0.5 else 0

    return result

cap = cv2.VideoCapture(0)

camera_no = 0
camera_name = 'webcam'
camera_loc = 'STREET A'

while True:
    ret, frame = cap.read()

    cv2.imshow('Live Feed', frame)

    detection_info = predict_and_get_info(frame, camera_no, camera_name, camera_loc)

    if detection_info['type_of_crime'] == 'Violence':
        current_datetime = datetime.now()
        
        if len(frames_list) > 0:
            out_filename = os.path.join(output_directory, f"{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.mp4")
            out = cv2.VideoWriter(out_filename, cv2.VideoWriter_fourcc(*'avc1'), fps, (frame.shape[1], frame.shape[0]))
            for saved_frame in frames_list:
                out.write(saved_frame)
            out.release()

        thumbnail_filename = os.path.join(thumbnail_output_directory, f"{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}-thumbnail.jpg")
        cv2.imwrite(thumbnail_filename, frame)
        print(detection_info)
        mysql_crime_insert.insert_into_crime(list(detection_info.values()))
        print("SQL Entry successful.")
        print("Video and Thumbnail Saved Successfully.")
        requests.post("https://ntfy.sh/hackeye_hackathon",data="Violence Detected".encode(encoding='utf-8'))
        print("Notification Sent.")
        break
    
    frames_list.append(frame)

    if len(frames_list) > clip_duration * fps:
        frames_list.pop(0)

    if start_time is None:
        start_time = datetime.now()
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
