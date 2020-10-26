# code based on example from here: https://gist.github.com/adarsh1021/8181bf655a1ef8128d09bda952fc78f2#file-face_detection_img-py
import cv2

face_cascade = cv2.CascadeClassifier('face_detector.xml')
img = cv2.imread('americangothic.jpg')
facefound = face_cascade.detectMultiScale(img,1.1,4)

for(x,y,w,h) in facefound:
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),4)
    cv2.imwrite("facedetected.jpg",img)
    print("faces found")

print("finished searching")
