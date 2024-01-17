import cv2
import numpy as np
import datetime
import sys
import os
sys.path.insert(1, 'ai_models/')
import mysql_crime_insert
import requests

net = cv2.dnn.readNet("ai_models/Pistol/yolov3_training_2000.weights", "ai_models/Pistol/yolov3_testing.cfg")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
classes = ["Pistol"]

# Global variables for video saving
output_directory = 'dashboard/videos/crimes'
thumbnail_output_directory = 'dashboard/videos/crimes/thumbnails/'
clip_duration = 10  # seconds
fps = 8  # frames per second

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)


cap = cv2.VideoCapture(0)  # 0 represents the default camera (webcam)

# Camera information
camera_no = 0
camera_name = 'webcam'
camera_loc = 'STREET A'
type_of_crime = 'Pistol'
detection_count = 0

# Variables for video clip and thumbnail creation
frames_list = []
start_time = None

while True:
    _, img = cap.read()
    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 0:  # Assuming the class_id for 'Weapon' is 0
                detection_count += 1
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    if len(indexes) > 0:
        print("Weapon detected in frame")
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_datetime = datetime.datetime.now()
        result = {
            'date': current_time.split()[0],
            'time': current_time.split()[1],
            'camera_no': camera_no,
            'camera_name': camera_name,
            'camera_loc': camera_loc,
            'type_of_crime': type_of_crime,
            'detection_count': detection_count
        }
        # Save the video clip
        if len(frames_list) > 0:
            out_filename = os.path.join(output_directory, f"{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.mp4")
            out = cv2.VideoWriter(out_filename, cv2.VideoWriter_fourcc(*'avc1'), fps, (img.shape[1], img.shape[0]))
            for saved_frame in frames_list:
                out.write(saved_frame)
            out.release()

        # Save the thumbnail
        thumbnail_filename = os.path.join(thumbnail_output_directory, f"{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}-thumbnail.jpg")
        cv2.imwrite(thumbnail_filename, img)
        print(result)
        mysql_crime_insert.insert_into_crime(list(result.values()))
        print("SQL Entry successful.")
        print("Video and Thumbnail Saved Successfully.")
        requests.post("https://ntfy.sh/hackeye_hackathon",data="Pistol Detected".encode(encoding='utf-8'))
        print("Notification Sent.")
        break

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

    cv2.imshow("Image", img)
    # Append frame to the list for video clip creation
    frames_list.append(img)

    # Remove frames older than clip_duration seconds
    if len(frames_list) > clip_duration * fps:
        frames_list.pop(0)

    # Update start_time for the first frame
    if start_time is None:
        start_time = datetime.datetime.now()
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
