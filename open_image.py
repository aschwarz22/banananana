import cv2
import numpy as np

def not_white(rgb):
    if ((rgb[0] < 245) & (rgb[1] < 245) & (rgb[2] < 245)):
        return True
    else:
        return False


def open_image(fname):
    good = 0
    tot = 0
    lower_yellow = np.array([20, 20, 20])
    upper_yellow = np.array([50, 230, 300])
    image = cv2.imread(fname, 1)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    height, width, channels = image.shape
    res = cv2.bitwise_and(image, image, mask=mask)

    for y in range(width):
        start = 0
        end = 0
        for x in range(height):
            if res[x, y][0] != 0:
                good += 1
                if start == 0:
                    start = x
                end = x
        tot += (end - start)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    print(good/tot)
    cv2.waitKey(0)





open_image('badnana.jpg')