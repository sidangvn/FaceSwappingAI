'''The mini group project was written by Si Dang, Karishma and Krishna in Dec - 2017
	The mini project can swap 2 faces in an image
	The project uses Opencv and "haarcascade_frontalface_default.xml" by using the following path on Github: opencv/data/haarcascades/haarcascade_frontalface_default.xml
	According to Zenva Academy lessions
	'''

import cv2
import sys

#retrives information from an other file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#image which has 2 faces / the path of the image
img = cv2.imread('picture.jpg')

#convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 8)

#print len(faces)
if len(faces) != 2:
	sys.exit('Please input an image with EXACTLY 2 faces!')

#coordinate declaration
x1, y1, w1, h1 = faces[0]
x2, y2, w2, h2 = faces[1]

#the faces position on the image
face1 = img[y1:y1+h1, x1:x1+w1]
face2 = img[y2:y2+h2, x2:x2+w2]

#resize images of faces
face1 = cv2.resize(face1, (w2, h2))
face2 = cv2.resize(face2, (w1, h1))

#swapping images of faces
# face 1
img[y1:y1+h1, x1:x1+w1] = face2
# face 2 
img[y2:y2+h2, x2:x2+w2] = face1

#show on screen
cv2.imshow('Swapped image', img)

count = 1
#save and quit app
while True:
	button = cv2.waitKey(1) & 0xFF
	if button == ord('q'): #press q to quit
		break
	elif button == ord('s'): #press s to save
		cv2.imwrite('Swapped%d.jpg' % count, img)
		count = count + 1

cv2.destroyAllWindows()


