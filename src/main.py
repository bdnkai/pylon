import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = [WindowCapture('badbar0'), WindowCapture('badbar1')]

loop_time = time()
while(True):

    # get an updated image of the game
    for i in wincap:
        j = 1    
        screenshot = i.get_screenshot()
        cv.imshow(f'{i}', screenshot)

    

    # debug the loop rate


    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')