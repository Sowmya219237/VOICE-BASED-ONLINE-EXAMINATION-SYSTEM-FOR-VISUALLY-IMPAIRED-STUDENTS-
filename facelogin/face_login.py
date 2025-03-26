import cv2
import face_recognition
import numpy as np
import os
import json
import sys

def load_registered_faces():
    known_faces = {}
    for file in os.listdir("faces"):
        user_name = file.split(".")[0]
        image_path = os.path.join("faces", file)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_faces[user_name] = encoding
    return known_faces

def recognize_face():
    known_faces = load_registered_faces()
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)
            if True in matches:
                matched_user = list(known_faces.keys())[matches.index(True)]
                cam.release()
                cv2.destroyAllWindows()
                
                # Return JSON response to PHP
                print(json.dumps({"status": "success", "username": matched_user}))
                return

        cam.release()
        cv2.destroyAllWindows()
        print(json.dumps({"status": "failed"}))  # If no match found

recognize_face()
