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

# Global variables for video saving
output_directory = 'dashboard/videos/crimes'
thumbnail_output_directory = 'dashboard/videos/crimes/thumbnails/'
clip_duration = 10  # seconds
fps = 8  # frames per second

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Load the trained violence detection model
model = tf.keras.models.load_model("ai_models/Violence/violence_detection_model.h5")

# Variables for video clip and thumbnail creation
frames_list = []
start_time = None

# Function to predict violence and return information
def predict_and_get_info(frame, camera_no, camera_name, camera_loc):
    result = {}

    # Resize the frame to match the input size of the model
    resized_frame = cv2.resize(frame, (64, 64))

    img_array = np.expand_dims(resized_frame, axis=0)
    img_array = img_array / 255.0  # Normalize pixel values to be between 0 and 1

    # Predict violence using the model
    prediction = model.predict(img_array)

    # Get the current date and time
    current_datetime = datetime.now()
    result['date'] = current_datetime.strftime("%Y-%m-%d")
    result['time'] = current_datetime.strftime("%H:%M:%S")

    # Camera information
    result['camera_no'] = camera_no
    result['camera_name'] = camera_name
    result['camera_loc'] = camera_loc

    # Type of crime
    result['type_of_crime'] = 'violence_detected' if prediction[0] >= 0.5 else 'no_violence'

    # Detection count
    result['detection_count'] = 1 if prediction[0] >= 0.5 else 0

    return result

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Camera information
camera_no = 0
camera_name = 'webcam'
camera_loc = 'STREET A'

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Live Feed', frame)

    # Call the predict_and_get_info function on each frame
    detection_info = predict_and_get_info(frame, camera_no, camera_name, camera_loc)

    # Print or use the detection_info dictionary in your HTML document
    if detection_info['type_of_crime'] == 'violence_detected':
        current_datetime = datetime.now()
         # Save the video clip
        
        if len(frames_list) > 0:
            out_filename = os.path.join(output_directory, f"{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.mp4")
            out = cv2.VideoWriter(out_filename, cv2.VideoWriter_fourcc(*'avc1'), fps, (frame.shape[1], frame.shape[0]))
            for saved_frame in frames_list:
                out.write(saved_frame)
            out.release()

        # Save the thumbnail
        thumbnail_filename = os.path.join(thumbnail_output_directory, f"{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}-thumbnail.jpg")
        cv2.imwrite(thumbnail_filename, frame)
        print(detection_info)
        mysql_crime_insert.insert_into_crime(list(detection_info.values()))
        print("SQL Entry successful.")
        print("Video and Thumbnail Saved Successfully.")
        requests.post("https://ntfy.sh/hackeye_hackathon",data="Violence Detected".encode(encoding='utf-8'))
        print("Notification Sent.")
        break
    
    # Append frame to the list for video clip creation
    frames_list.append(frame)

    # Remove frames older than clip_duration seconds
    if len(frames_list) > clip_duration * fps:
        frames_list.pop(0)

    # Update start_time for the first frame
    if start_time is None:
        start_time = datetime.now()
        
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When violence is detected or 'q' is pressed, release the capture and close windows
cap.release()
cv2.destroyAllWindows()
