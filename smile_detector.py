import numpy as np      #importing libraries
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #loading the pre-trained classifiers for face and smile detection
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
 
cap = cv2.VideoCapture(0)   #opens the webcam for video capturing

while True:                 #infinite loop to continuously capture frames from the webcam
    ret, img = cap.read()   #reads a frame from the webcam and stores it in the variable 'img'
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #converts the captured frame to grayscale for better processing. We used grayscale because the Haar Cascade classifier works better on single channel images. Uses less memory and is faster to process than color images.
    faces = faceCascade.detectMultiScale(           #detects faces in the grayscale image using the face cascade classifier
        gray,
        scaleFactor=1.3,    #specifies how much the image size is reduced at each image scale. A value of 1.3 means the image size is reduced by 30% at each scale.
        minNeighbors=5,     #specifies how many neighbors each candidate rectangle should have to retain it. A higher value results in fewer detections but with higher quality.
        minSize=(30, 30)    #specifies the minimum possible object size. Objects smaller than this are ignored.
    )

    for (x,y,w,h) in faces: #loops through the detected faces and draws rectangles around them. It also detects smiles within the detected face region.
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  #draws a rectangle around the detected face in the original image.
        roi_gray = gray[y:y+h, x:x+w]   #extracts the region of interest (ROI) from the grayscale image, which is the detected face region. This ROI is used for smile detection.
                
        smile = smileCascade.detectMultiScale(  #detects the smile
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors=15,
            minSize=(25, 25),
            )
        
        for i in smile:
            if len(smile)>1:
                cv2.putText(img,"Smiling",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,
                    2,(0,255,0),3,cv2.LINE_AA)
               
    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()