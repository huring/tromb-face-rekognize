import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while(True):
	ret, frame = cap.read()
<<<<<<< HEAD
	frame = cv2.flip(frame, -1)
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame', frame)
	# cv2.imshow('gray', gray)
=======
	frame = cv2.flip(frame, 1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)
>>>>>>> 124f7b7ea5595b054b44c40f7b6206fb28a250f6

	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()