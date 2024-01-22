import cv2
import numpy as np

facedetect = cv2.CascadeClassifier("C:/Users/Dell/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
capt = cv2.VideoCapture(0)

i=0

id = input("Enter Your Id")

while True :
    ret , vidop = capt.read()
    clr = cv2.cvtColor(vidop,cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(
        clr,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40,40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        i=i+1
        cv2.imwrite('datasets/User.'+str(id)+"."+str(i)+".jpg", clr[y:y+h, x:x+w])
        cv2.rectangle(vidop,(x,y),(x+w,y+h),(0,250,0),1)
    cv2.imshow("LIVE",vidop)
    if cv2.waitKey(10) == ord("s") or i>500:
        break
capt.release()
cv2.destroyAllWindows()

print("Done")

