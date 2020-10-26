import cv2
import os, sys
from PIL import Image
# change the paths here to make them workable
path ="/Users/campberebe3/Desktop/faceassignment/trump_photos/"
path2 = "/Users/campberebe3/Desktop/faceassignment/Trumpfaces/"
dirs =os.listdir(path)

face_cascade = cv2.CascadeClassifier('face_detector.xml')


def findface():
    counter = 0
    for item in dirs:
        if os.path.isfile(path+item):
            img = cv2.imread(path+item)
            facez = face_cascade.detectMultiScale(img,1.1,4)

            for(x,y,w,h) in facez:
                
                counter += 1
                facew = x+w
                rectw = int(w/4)
                recth = int(h/4)
                offy =int(recth/2)
                offx =int(rectw/2)

                im = Image.open(path+item)
                im_crop = im.crop((x-offx,y-offy,x+w+rectw,y+h+recth))
                im_crop.save(path2+"crop"+str(counter)+".jpg")


    print("found "+str(counter)+" faces!")
    

findface()


