import numpy as np 
import cv2
import face_recognition
import os
#from datetime import datetime

images = []
known_names = []
         
def face_recog():

    cap = cv2.VideoCapture(0)

    while True:

        # Grab a frame of video
        ret, cap_img = cap.read()

        # Finds all the faces and their encodings in the current frame of video
        cap_face_loc = face_recognition.face_locations(cap_img)
        cap_face_enc = face_recognition.face_encodings(cap_img, cap_face_loc)

        # i and j represent each single face encoding and face location
        for i,j in zip(cap_face_enc, cap_face_loc):
            comparison = face_recognition.compare_faces(encodings, i)
            distances = face_recognition.face_distance(encodings, i)
            #print(distance)

            smallest_distance = np.argmin(distances)
            top, right, bottom, left = j
            color = (255, 0, 0) 
            color2 = (0, 0, 255)
            font = cv2.FONT_HERSHEY_PLAIN

            if comparison[smallest_distance]:
                student = known_names[smallest_distance].upper()
                #print(student)
                #makes rectangle with the name on each located face
                cv2.rectangle(cap_img,(left,top),(right,bottom), color , cv2.LINE_4)
                cv2.putText(cap_img, student,(left+8, top -8), font , 1, color2, 2)

        cv2.imshow('MARKING ATTENDANCE . . . ', cap_img)

        #press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def getImages(path):

    known_images = os.listdir(path)

    for i in known_images:
        img = cv2.imread(f'{path}/{i}')
        images.append(img)
        known_names.append(os.path.splitext(i)[0])

    return known_names

def getEncodings(images):

    encodedList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded = face_recognition.face_encodings(img)[0]
        encodedList.append(encoded)

    return encodedList

getImages('images')
encodings = getEncodings(images)
print('Encoding Complete!')
face_recog()
