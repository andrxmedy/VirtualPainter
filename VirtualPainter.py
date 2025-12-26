import cv2
import numpy as np
import time
import os

from numpy.distutils.misc_util import blue_text

import HandTrackingModule as htm

#######
brushThickness = 15
eraserThickness = 100
#######
folderPath = "header"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

header = overlayList[5]
header = cv2.resize(header, (140, 720))

drawColor = (180, 167, 214)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.85)

xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    #1. Import image
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (1280, 720))

    #2. Find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        #print(lmList)

        #Tip of index and middle finger
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]


        #3. Check witch fingers are up
        fingers = detector.fingersUp()
        #print(fingers)

        #4. If Selection Mode: Two Fingers Are Up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print("Selection Mode")
            #Checking for the click
            if x1 < 140:
                if y1 < 145:
                    #Pink
                    header = overlayList[5]
                    drawColor = (180,167,214)
                if 145 <= y1 < 260:
                    #Blue
                    header = overlayList[3]
                    drawColor = (232,197,159)
                if 260 <= y1 < 373:
                    #Purple
                    header = overlayList[0]
                    drawColor = (223,137,166)
                if 373 <= y1 < 450:
                    #Green
                    header = overlayList[4]
                    drawColor = (182,215,168)
                if y1 >= 450:
                    #Eraser
                    drawColor = (0, 0, 0)
                    header = overlayList[1]

            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)



        #5. If Drawing Mode: Index Finger Is Up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0,0,0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)


            xp, yp = x1, y1


    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    img[0:720, 0:140] = header
    #img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
    cv2.imshow("Image", img)
    # cv2.imshow("Canvas", imgCanvas)
    cv2.waitKey(1)
