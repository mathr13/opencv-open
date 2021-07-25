import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

winname = 'image_window'
cv2.namedWindow(winname,cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname, 302,600)
img = cv2.imread('/Users/shishirmathur/Downloads/Computer-Vision-with-Python/DATA/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
cv2.moveWindow(winname, 978,60)


flipped_image = cv2.flip(img, 1)
# cv2.imshow(winname, flipped_image)
# cv2.waitKey(0)

while True:
    cv2.imshow(winname, flipped_image)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

#closing all open windows
cv2.destroyAllWindows()
