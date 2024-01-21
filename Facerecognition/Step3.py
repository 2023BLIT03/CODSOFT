import cv2
import numpy as np

facedetect = cv2.CascadeClassifier("C:/Users/Dell/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
capt = cv2.VideoCapture(0)

recogniser = cv2.face.LBPHFaceRecognizer_create()
recogniser.read("Trainer.yml")

nameList = ["","Zeeshan"]

imgBackground = cv2.imread("background.png")

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
        serial, confi = recogniser.predict(clr[y:y+h, x:x+w])
        if confi<50:
            cv2.rectangle(vidop,(x,y),(x+w, y+h),(0,0,250),1)
            cv2.rectangle(vidop,(x,y),(x+w, y+h),(50,50,250),2)
            cv2.rectangle(vidop,(x,y-40),(x+w, y),(50,50,250),-1)
            cv2.putText(vidop, nameList[serial], (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
        else:
            cv2.rectangle(vidop,(x,y),(x+w, y+h),(0,0,250),1)
            cv2.rectangle(vidop,(x,y),(x+w, y+h),(50,50,250),2)
            cv2.rectangle(vidop,(x,y-40),(x+w, y),(50,50,250),-1)
            cv2.putText(vidop, "Unknown", (x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (225,225,255), 2)
    cv2.imshow("LIVE",vidop)
    if cv2.waitKey(10) == ord("s"):
        break
capt.release()
cv2.destroyAllWindows()

print("Done")

