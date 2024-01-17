import os
import face_recognition
import cv2

# Function to load images from subfolders and return face encodings and names
def load_images_from_subfolders(parent_folder):
    face_encodings = []
    face_names = []

    for person_folder in os.listdir(parent_folder):
        person_folder_path = os.path.join(parent_folder, person_folder)
        if os.path.isdir(person_folder_path):
            for filename in os.listdir(person_folder_path):
                if filename.endswith(('.jpg', '.jpeg', '.png')):
                    person_name = person_folder  # Use the subfolder name as the person's name
                    image_path = os.path.join(person_folder_path, filename)
                    person_image = face_recognition.load_image_file(image_path)
                    person_encoding = face_recognition.face_encodings(person_image)

                    if len(person_encoding) > 0:
                        # Assuming only one face per image
                        face_encodings.append(person_encoding[0])
                        face_names.append(person_name)

    return face_encodings, face_names

# Load known faces and their corresponding names from the database
known_face_encodings = []
known_face_names = []

# Add known faces to the database
# Replace the path below with the path to your main folder containing subfolders
parent_folder_path = "dashboard\images\criminals"

# Load images from subfolders and add encodings and names to the database
known_face_encodings, known_face_names = load_images_from_subfolders(parent_folder_path)

# Open a video capture object using the webcam (camera index 0)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture each frame from the webcam feed
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop over each face found in the current frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match is found, use the name of the known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Choose the color for the bounding box based on whether the person is known or unknown
        box_color = (0, 255, 0)  # Default color for known persons (green)
        if name == "Unknown":
            box_color = (0, 0, 255)  # Red color for unknown persons

        # Draw a rectangle around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), box_color, 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Print out the detected person's name
        print(f"Detected: {name}")

    # Display the result
    cv2.imshow("Face Recognition", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
video_capture.release()
cv2.destroyAllWindows()
