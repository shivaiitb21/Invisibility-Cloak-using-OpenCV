import numpy as np
import cv2

# Import time library to provide camera setup some time
import time

# Capture the video
cap = cv2.VideoCapture(0) # Put 0 for your machine's camera and may vary if you use other camera 

time.sleep(2)

# Capture the background, which is diaplayed when you have cloak on yourself
background = 1

# Capture the background image 50 times -> best result
for i in range(50):
    # cap.read returns the two things
    # -> 1) Image captured 2)Return value which is True if read is working fine or else false
    ret, background = cap.read()

# While loop with (Cap.isOpened) ensures that code is running till the webcam is capturing
# Or else code will run in background
while(cap.isOpened()):

    # Capture image to perform operation on it
    ret, img = cap.read()

    # To stop code from running
    if not ret:
        break
    # HSV -> Heu, Saturation and Value
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Also called HSB -> B stands for brightness
# Note-> In RGB every value depends upon the colour and brightness of the colour
# But in HSB, only Hue depends upon the colour, rest S and B are independant of colour

# Hue --> we will take 0-10 and 170-180, actually Hue is from 0-30
# but we wont consider it or else every minute detail will be considered, which will hamper the magic

# HSV Values
    lower_red = np.array([0, 120, 70])
# Saturation is the darkness of the color, brightness are required values
    upper_red = np.array([10, 255, 255])
# Making the mask
    mask1 = cv2.inRange(hsv, lower_red, upper_red) # Seperating the cloak part here by checking if there is any part from lower red to upper red

# Red color is from 170 to 180 as well
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

### NOTE -->> Saturation and Brightness values depends upon the colour
# If there are any shades from 0-10 and 170-180, that would be segmented
    mask1 = mask1 + mask2

# Noise removal
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2) # Noise removal
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1) # Smoothening the image
# As morphological operations are generally done on greyspace images but here we have taken coloured

# Except the cloack, everything will be there --> Use bitwise NOT
# As remember mask1 is the cloak part
    mask2 = cv2.bitwise_not(mask1) # Except the cloak

    res1 = cv2.bitwise_and(background, background, mask=mask1) # Used for segmentation of colour from rest of background
    res2 = cv2.bitwise_and(img, img, mask=mask2) # Used to substitute the cloak part
# Linearly added two images
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0) # Its like linear equation -> (alpha, beta, gamma)

    cv2.imshow("Magic!!!!", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

