import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

winname = 'image_window'
cv2.namedWindow(winname,cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname, 302,600)
img = cv2.imread('/Users/shishirmathur/Downloads/Computer-Vision-with-Python/DATA/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
cv2.moveWindow(winname, 978,60)

#Blank Image
blank_image = np.zeros(shape=(512,512,3), dtype=np.uint8)
cv2.rectangle(blank_image, pt1=(10, 110), pt2=(110,10), color=(0,0,255), thickness=-1)
cv2.circle(blank_image, center=(60,60), radius=50, color=(255,0,0), thickness=5)
cv2.line(blank_image, pt1=(10, 10), pt2=(110,110), color=(0,255,0), thickness=5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_image, text="PUPPY", org = (10,100), fontFace = font, fontScale = 4, color=(255,255,255), thickness = 3, lineType=cv2.LINE_AA)

vertices = np.array([[102,200], [302,200], [102,400], [302, 400]], dtype=np.int32)
points = vertices.reshape((-1,1,2))
cv2.polylines(blank_image, [points], isClosed=True, color=(255,255,255),thickness=5)

#DRAW CIRCLE ON CLICK
def drawCircle(event, x, y, flags, params):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print(x)
        print(y)
        print("-----------")
        cv2.circle(blank_image, center=(60,60), radius=50, color=(255,0,0), thickness=5)
        cv2.imshow(winname, blank_image)
cv2.setMouseCallback(winname, drawCircle)


while True:
    cv2.imshow(winname, blank_image)
    if cv2.waitKey():
        break

#closing all open windows
cv2.destroyAllWindows()
