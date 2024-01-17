import cv2
import numpy as np
import tensorflow as tf
from datetime import datetime

# Load the trained model
model = tf.keras.models.load_model('ai_models/Accident/accident_detection_model.h5')

# Open the video file
cap = cv2.VideoCapture(0)

# Get the frames per second (fps) and frame size of the video
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_width, frame_height)

# Create VideoWriter object to save the output
output_path = 'output.mp4'
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'avc1'), fps, frame_size)

# Define the target size for the model input
target_height, target_width = 224, 224

# Initialize variables for accident details
accident_detected = False
accident_details = {}

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Resize the frame to the target size
    resized_frame = cv2.resize(frame, (target_width, target_height))

    # Preprocess the frame
    normalized_frame = resized_frame / 255.0
    input_frame = np.expand_dims(normalized_frame, axis=0)

    # Make a prediction
    prediction = model.predict(input_frame)
    label = "Accident" if prediction[0][0] > 0.5 else "Non-Accident"

    # Display the result on the frame
    cv2.putText(frame, f'Prediction: {label}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # If accident is detected, capture details and end the video
    if label == "Accident" and not accident_detected:
        accident_detected = True

        # Capture accident details
        current_datetime = datetime.now()
        accident_details['date'] = current_datetime.strftime('%Y-%m-%d')
        accident_details['time'] = current_datetime.strftime('%H:%M:%S')
        accident_details['location'] = 'Your Location'  # Replace with actual location data
        accident_details['camera_type'] = 'Your Camera Type'  # Replace with actual camera type
        accident_details['accident_detection'] = 'Accident Detected'

        # Release resources
        cap.release()
        out.release()
        cv2.destroyAllWindows()

        # Return the accident details
        print("Accident Detected. Details:", accident_details)
        break

    # Write the frame to the output video
    out.write(frame)

    # Display the frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break