import cv2
import numpy as np
import tensorflow as tf
from datetime import datetime

model = tf.keras.models.load_model('ai_models/Accident/accident_detection_model.h5')

cap = cv2.VideoCapture(0)

fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_width, frame_height)

output_path = 'output.mp4'
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'avc1'), fps, frame_size)

target_height, target_width = 224, 224

accident_detected = False
accident_details = {}

while True:
    ret, frame = cap.read()

    if not ret:
        break

    resized_frame = cv2.resize(frame, (target_width, target_height))

    normalized_frame = resized_frame / 255.0
    input_frame = np.expand_dims(normalized_frame, axis=0)

    prediction = model.predict(input_frame)
    label = "Accident" if prediction[0][0] > 0.5 else "Non-Accident"

    cv2.putText(frame, f'Prediction: {label}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if label == "Accident" and not accident_detected:
        accident_detected = True

        current_datetime = datetime.now()
        accident_details['date'] = current_datetime.strftime('%Y-%m-%d')
        accident_details['time'] = current_datetime.strftime('%H:%M:%S')
        accident_details['location'] = 'Your Location'
        accident_details['camera_type'] = 'Your Camera Type'
        accident_details['accident_detection'] = 'Accident Detected'

        cap.release()
        out.release()
        cv2.destroyAllWindows()

        print("Accident Detected. Details:", accident_details)
        break

    out.write(frame)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break