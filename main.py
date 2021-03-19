import numpy as np 
import cv2
import face_recognition
#from datetime import datetime

#image path  
path = r'D:\Projects\Group\iAttend\images\messi.jpg'
img1 = cv2.imread(path) 
path2 = r'D:\Projects\Group\iAttend\test_images\test_img1.jpg'
test_img1 = cv2.imread(path2) 

#loading saved image
#img1 = face_recognition.load_image_file('images/messi.jpg')
#img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

#loading test image
#test_img1 = face_recognition.load_image_file('test_images/test_img1.jpg')
#test_img1 = cv2.cvtColor(test_img1,cv2.COLOR_BGR2RGB)

#returns an array of bounding box of the test face 
face_Location = face_recognition.face_locations(test_img1)[0]

#returns a list of 128-dimensional face encodings for each face in the images
face_Encoding = face_recognition.face_encodings(img1)[0]
face_Encoding2 = face_recognition.face_encodings(test_img1)[0]

#A list of tuples of found face locations in css (top, right, bottom, left) order
start_point = (face_Location[3], face_Location[0]) 
end_point = (face_Location[1], face_Location[2]) 
color = (255, 0, 0) 

#makes rectangle on located face
cv2.rectangle(test_img1,start_point,end_point, color , cv2.LINE_4)

#comparing known face with the test face
comparison = face_recognition.compare_faces([face_Encoding], face_Encoding2)
print(comparison)

#Displaying images
cv2.imshow('Lionel Messi', img1)  
cv2.imshow('Messi Test', test_img1)  
cv2.waitKey(0)

 