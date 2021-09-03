import cv2   #Import Video Capture Module
import keyboard #Import Module That Detects Key Presses

from PIL import Image
from time import sleep
import os
import numpy as np         #Numpy graphing
from numpy import asarray

ColorValueRed = int(225) #Choose the red value of the color you want to detect
ColorValueGreen = int(0) #Choose the green value of the color you want to detect
ColorValueBlue = int(0)  #Choose the blue value of the color you want to detect

videoCaptureObject = cv2.VideoCapture(0) #Makes the live video called variable "videoCaptureObject"

video_stream = True
while(video_stream): #Creates an infinite loop with line above While(true)
 ret,frame = videoCaptureObject.read()
 cv2.imshow('Capturing Video',frame)   #Shows the current frame. Since this is in a quickly repeating infinite loop, it shows a video
 if(cv2.waitKey(1) & 0xFF == ord('q')): #if it detects you pressing the "q" button...
  videoCaptureObject.release()          #this line and the one below stops the stream and stops displaying the camera view
  cv2.destroyAllWindows()
  
 cv2.imwrite("NewPicture.jpg",frame) #Each frame of the video stream turns into a photo in the same location as the python file. Each loop of this infinte loop overrides the past photo of the same name.


 img = Image.open("NewPicture.jpg") #Read sources at the end of this code to find a link to an explanation from Stack Overflow source
 WIDTH, HEIGHT = img.size                                   

 data = list(img.getdata())
 data =[data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]


 #The text 2 lines "for row..." and "for i..." are going to set up a loop where each pixel is checked for the desired color before moving onto the next pixel.
 
 for row in data: #The RGB values of each pixel are stored in lists in a list. For each row of pixel values in the list of pixel values...
  for i in row: #Each pixel value has...
   Red = i[0]   #A red value turned into a variable called "Red"
   Green = i[1] #A green value turned into a variable called "Green"
   Blue = i[2]  #A blue value turned into a variable called "Blue"

   if (ColorValueRed-100) <= Red <= (ColorValueRed+50):   #If that pixel's red value is close to the red value in the desire color...
    if (ColorValueGreen-50) <= Green <= (ColorValueGreen+50): #Check if the pixel's green value is close to the green value of the desired color. If it is... 
     if (ColorValueBlue-50) <= Blue <= (ColorValueBlue+50): #Check if the pixel's blue value is close to the blue value of the desired color.
      print("Color Detected") #If all color values are approved, You found the desired color and are notified with python telling you.
          

#Sources
#https://www.studytonight.com/post/capture-videos-and-images-with-python-part2
#https://stackoverflow.com/questions/24072790/how-to-detect-key-presses
#https://stackoverflow.com/questions/40727793/how-to-convert-a-grayscale-image-into-a-list-of-pixel-values
