import cv2
import time
 
# capture frames from a video
cap = cv2.VideoCapture('./video.m4v')
 
car_cascade = cv2.CascadeClassifier('./cars.xml')
count = 0
rate = 0

start = time.time()
# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    width = cap.get(3) 
    height = cap.get(4)

    cv2.line(frames, (0, int(height*1/4)), (int(width), int(height*1/4)), (0,0,255), 1)
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    
 
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        if height*1/4 - 2 <= y+h <=  height*1/4 + 2: 
            count = count + 1
            now = time.time() 
            timeElapsed = now - start 
            rate = "{0:.2f}".format(count / timeElapsed)
            
        cv2.rectangle(frames,(x,y),(x+w,y+h),(255,128,0),2)
        # cv2.putText(frames, str(y+h) , (x,h), cv2.FONT_HERSHEY_DUPLEX, 1 , (0,255,0))
        totalCount = "total " + str(count)
        rateText =  str(rate) + " cars per second "
        cv2.putText(frames, totalCount , (50,50), cv2.FONT_HERSHEY_DUPLEX, 1 , (0,255,0))
        cv2.putText(frames, rateText , (50,80), cv2.FONT_HERSHEY_DUPLEX, 1 , (0,255,0))
   # Display frames in a window 
    cv2.imshow('video2', frames)
     
    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()
