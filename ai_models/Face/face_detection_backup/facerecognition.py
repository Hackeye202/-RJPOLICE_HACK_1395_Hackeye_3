import face_recognition
import cv2

# Load known faces and their corresponding names from the database
known_face_encodings = []
known_face_names = []

# Add known faces to the database
# Replace the paths below with the paths to your own images
person1_image = face_recognition.load_image_file("images/angela.jpg")
person1_encoding = face_recognition.face_encodings(person1_image)[0]
known_face_encodings.append(person1_encoding)
known_face_names.append("Angela")

person2_image = face_recognition.load_image_file("images/tomcruise.jpeg")
person2_encoding = face_recognition.face_encodings(person2_image)[0]
known_face_encodings.append(person2_encoding)
known_face_names.append("Tom cruise")

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

    # Display the result
    cv2.imshow("Face Recognition", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
video_capture.release()
cv2.destroyAllWindows()
