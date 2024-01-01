import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from datetime import datetime
import cv2

model = tf.keras.models.load_model("C:/Users/Manoj/violence_detection_model.h5")

def predict_and_get_info(frame, camera_type="Dummy Camera", camera_status="Active", location="Dummy Location"):
    result = {}
    img_array = cv2.resize(frame, (64, 64))
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    prediction = model.predict(img_array)
    current_datetime = datetime.now()
    result['date'] = current_datetime.strftime("%Y-%m-%d")
    result['time'] = current_datetime.strftime("%H:%M:%S")
    result['camera_type'] = camera_type
    result['camera_status'] = camera_status
    result['location_of_camera'] = location
    if 'detection_count' not in result:
        result['detection_count'] = 0
    if prediction[0] >= 0.5:
        result['violence_detected'] = True
        result['detection_count'] += 1
        result['type_of_crime'] = "Violence"
    else:
        result['violence_detected'] = False
    
    return result
def process_video(video_path, camera_type="Dummy Camera", camera_status="Active", location="Street A"):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detection_info = predict_and_get_info(frame, camera_type=camera_type, camera_status=camera_status, location=location)
        cv2.putText(frame, f"Violence Detected: {detection_info['violence_detected']}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Violence Detection", frame)
        if detection_info['violence_detected']:
            print("Violence detected. Ending program.")
            cap.release()
            cv2.destroyAllWindows()
            return detection_info
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
video_path = "C:/Users/Manoj/Downloads/pistol5.mp4"
result_info = process_video(video_path, camera_type="Dummy Camera", camera_status="Active", location="Street A")
print(result_info)
