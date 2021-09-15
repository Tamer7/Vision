import cv2
import numpy as np


def get_color(image):
    lower = {'red':(0, 30, 50), 'green':(40, 100, 100), 'blue':(97, 100, 117), 'yellow':(20, 100, 100), 'orange':(5, 50, 50)} 
    upper = {'red':(10,255,255), 'green':(80,255,255), 'blue':(117,255,255), 'yellow':(30,255,255), 'orange':(15,255,255)}


    # Here we are defining the standard colors.
    colors = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0), 'yellow':(0, 255, 217), 'orange':(0,140,255)}

    im_resize = cv2.resize(image, (600, 600))
    blurred = cv2.GaussianBlur(im_resize, (11,11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    radiuss = []
    colorss = []
    for key, value in upper.items():
            kernel = np.ones((9,9),np.uint8)
            mask = cv2.inRange(hsv, lower[key], upper[key])
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None
       
            if len(cnts) > 0:
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                radiuss.append(radius)
                colorss.append(key)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                return colorss[0]
