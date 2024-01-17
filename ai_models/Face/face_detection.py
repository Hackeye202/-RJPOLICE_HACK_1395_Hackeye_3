import os
import face_recognition
import cv2
from datetime import datetime
import mysql.connector

# Database Details
host = "localhost"
user = "root"
password = "1234"
database = "hackeye"

conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()


def load_images_from_subfolders(parent_folder):
    face_encodings = []
    face_names = []

    for person_folder in os.listdir(parent_folder):
        person_folder_path = os.path.join(parent_folder, person_folder)
        if os.path.isdir(person_folder_path):
            for filename in os.listdir(person_folder_path):
                if filename.endswith(('.jpg', '.jpeg', '.png')):
                    person_name = person_folder  
                    image_path = os.path.join(person_folder_path, filename)
                    person_image = face_recognition.load_image_file(image_path)
                    person_encoding = face_recognition.face_encodings(person_image)

                    if len(person_encoding) > 0:
                        face_encodings.append(person_encoding[0])
                        face_names.append(person_name)

    return face_encodings, face_names

known_face_encodings = []
known_face_names = []
parent_folder_path = "dashboard/images/criminals"

known_face_encodings, known_face_names = load_images_from_subfolders(parent_folder_path)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            current_datetime = datetime.now()
            result_dict = {
                'date': current_datetime.strftime("%Y-%m-%d"),
                'time': current_datetime.strftime("%H:%M:%S"),
                'camera_no': 1,
                'camera_loc': 'Prison', 
                'face': name
            }
            data_to_insert = list(result_dict.values())
            insert_query = "INSERT INTO face (date, time, camera_no, camera_loc, face) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(insert_query, data_to_insert)
            conn.commit()
            cursor.close()
            conn.close()
            video_capture.release()
            cv2.destroyAllWindows()

            print(result_dict)
            print("SQL Entry successful.")
            exit()

        box_color = (0, 255, 0) 
        if name == "Unknown":
            box_color = (0, 0, 255)  

        cv2.rectangle(frame, (left, top), (right, bottom), box_color, 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        print(f"Detected: {name}")

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
