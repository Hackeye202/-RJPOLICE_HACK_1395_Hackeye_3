import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from datetime import datetime
model = tf.keras.models.load_model("C:/Users/Manoj/violence_detection_model.h5")
def predict_and_get_info(image_path, camera_status="Active", location="Dummy Location"):
    result = {}
    img = image.load_img(image_path, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0 
    prediction = model.predict(img_array)
    current_datetime = datetime.now()
    result['date'] = current_datetime.strftime("%Y-%m-%d")
    result['time'] = current_datetime.strftime("%H:%M:%S")
    result['camera_status'] = camera_status
    result['location'] = location
    if 'detection_count' not in result:
        result['detection_count'] = 0
    if prediction[0] >= 0.5:
        result['violence_detected'] = True
        result['detection_count'] += 1
    else:
        result['violence_detected'] = False
    return result
test_image_path ="C:/Users/Manoj/Downloads/gun.jpg" 
detection_info = predict_and_get_info(test_image_path, camera_status="Active", location="Street A")
print(detection_info)
