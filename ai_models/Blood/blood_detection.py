import cv2
from tensorflow.keras.models import load_model
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

model = load_model("ai_models/Blood/blood_detection_model.h5")

cap = cv2.VideoCapture(0)

camera_info = {
    'camera_no': 1,
    'camera_name': 'Webcam',
    'camera_loc': 'Hallway'
}

result_dict = {}

frames_list = []
start_time = None

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_array = np.expand_dims(img, axis=0)
    img_array = img_array / 255.0

    predictions = model.predict(img_array)

    if predictions[0][0] < 0.5:
        status_text = "Blood Detected"

        current_datetime = datetime.now()
        result_dict['date'] = current_datetime.strftime("%Y-%m-%d")
        result_dict['time'] = current_datetime.strftime("%H:%M:%S")
        result_dict['camera_no'] = camera_info['camera_no']
        result_dict['camera_name'] = camera_info['camera_name']
        result_dict['camera_loc'] = camera_info['camera_loc']
        result_dict['type_of_crime'] = 'Blood'
        result_dict['detection_count'] = 1

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
        print(result_dict)
        mysql_crime_insert.insert_into_crime(list(result_dict.values()))
        print("SQL Entry successful.")
        print("Video and Thumbnail Saved Successfully.")
        requests.post("https://ntfy.sh/hackeye_hackathon",data="Blood Detected".encode(encoding='utf-8'))
        print("Notification Sent.")
        exit()

    else:
        status_text = "No Blood Detected"

    cv2.putText(frame, status_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Webcam Blood Detection', frame)


    frames_list.append(frame)

    if len(frames_list) > clip_duration * fps:
        frames_list.pop(0)

    if start_time is None:
        start_time = datetime.now()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
