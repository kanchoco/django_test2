# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 11:56:58 2024

@author: USER
"""
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# https://www.geeksforgeeks.org/count-number-of-faces-using-python-opencv/?ref=lbp

import numpy as np
import cv2



# Try using DirectShow backend
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)  # Increase buffer size

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()