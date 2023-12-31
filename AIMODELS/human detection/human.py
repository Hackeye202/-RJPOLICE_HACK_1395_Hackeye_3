import cv2
import numpy as np
net = cv2.dnn.readNet("C:/Users/Manoj/Downloads/yolov4.weights", "C:/Users/Manoj/Downloads/yolov4.cfg")
with open("C:/Users/Manoj/Downloads/coco.names", "r") as f:
    classes = f.read().strip().split("\n")
layer_names = net.getUnconnectedOutLayersNames()
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()  
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)  
    detections = net.forward(layer_names)   
    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]           
            if confidence > 0.5 and classes[class_id] == "person":
                box = obj[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                (x, y, w, h) = box.astype("int")     
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = f"{classes[class_id]}: {confidence:.2f}"
                cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) 
    cv2.imshow("YOLOv4 Human Detection", frame)  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()