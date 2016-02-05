import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

while True:
	#Capture frame-by-frame
	ret, frame = cap.read()
	#print ret
	#print ret
	#print ret

	# Our operations on the frame come here
	frame = cv2.medianBlur(frame,5)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(gray,78,255,0)
	#(thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	#print thresh
	edges = cv2.Canny(gray,50,150,apertureSize = 3)
	lines = cv2.HoughLines(edges,1,np.pi/180,1)

	if lines is not None:
		for rho,theta in lines[0]:
			a = np.cos(theta)
			b = np.sin(theta)
			x0 = a*rho
			y0 = b*rho
			x1 = int(x0 + 1000*(-b))
			y1 = int(y0 + 1000*(a))
			x2 = int(x0 - 1000*(-b))
			y2 = int(y0 - 1000*(a))
			cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
		
	#print "here's what I found: ", lines[0]
	# Display the resulting frame
	cv2.imshow('detected circles',frame)
	#cv2.imshow('frame', thresh)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		print 'Quitting...'
		cv2.destroyAllWindows()
		break
		
	#time.sleep(0)

# When everything done, release the capture
cap.release()

def big_time_circles():
	circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=60,minRadius=0,maxRadius=0)
	if circles is None:
		#continue
		print "I'm a dope."
	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
		# draw the outer circle
		cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
		# draw the center of the circle
		cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
		print "x coord:", i[0], "y coord:", i[1]
