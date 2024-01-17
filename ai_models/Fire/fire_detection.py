import cv2
import numpy as np
from datetime import datetime
from tensorflow.keras.models import load_model
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

# Load the trained model
loaded_model = load_model('ai_models/Fire/fire_detection_model.h5')

# Function to preprocess video frames for prediction
def preprocess_frame_for_prediction(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = np.expand_dims(frame, axis=0) / 255.0
    return frame

# Open a camera capture object
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera device

# Attributes
camera_no = 1  # Camera index
camera_name = "Webcam"  # Camera name
camera_loc = "Entrance"  # Camera location
type_of_crime = "Fire"  # Type of crime
detection_count = 0  # Initialize detection count

# Variables for video clip and thumbnail creation
frames_list = []
start_time = None

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Preprocess the frame for prediction
    preprocessed_frame = preprocess_frame_for_prediction(frame)

    # Make predictions
    prediction = loaded_model.predict(preprocessed_frame)

    # Set a threshold for detection
    if prediction[0, 0] > 0.5:
        # Fire Detected
        detection_count += 1

        # Get current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_datetime = datetime.now()
        # Create a dictionary with attributes
        detection_info = {
            'date': current_time.split(' ')[0],
            'time': current_time.split(' ')[1],
            'camera_no': camera_no,
            'camera_name': camera_name,
            'camera_loc': camera_loc,
            'type_of_crime': type_of_crime,
            'detection_count': detection_count
        }

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

        # Release the camera capture object and close windows
        cap.release()
        cv2.destroyAllWindows()

        # Return the detection information
        print(detection_info)
        mysql_crime_insert.insert_into_crime(list(detection_info.values()))
        print("SQL Entry successful.")
        print("Video and Thumbnail Saved Successfully.")
        requests.post("https://ntfy.sh/hackeye_hackathon",data="Fire Detected".encode(encoding='utf-8'))
        print("Notification Sent.")
        break

    # Display the resulting frame
    cv2.imshow('Fire Detection', frame)
    # Append frame to the list for video clip creation
    frames_list.append(frame)
    
    # Remove frames older than clip_duration seconds
    if len(frames_list) > clip_duration * fps:
        frames_list.pop(0)

    # Update start_time for the first frame
    if start_time is None:
        start_time = datetime.now()
    # Break the loop if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
