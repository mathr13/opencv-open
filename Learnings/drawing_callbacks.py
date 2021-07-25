import cv2
import numpy as np

winname = 'image_window'
cv2.namedWindow(winname,cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname, 302,600)
img = cv2.imread('/Users/shishirmathur/Downloads/Computer-Vision-with-Python/DATA/dog_backpack.jpg', cv2.IMREAD_COLOR)
cv2.moveWindow(winname, 978,60)

def showCoord(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (x,y,255), -1)
        label = "("+str(x)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, label, (x+10, y-10), font, 1, (255,255,255))
        cv2.imshow(winname, img)
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x,y), 3, (x,y,255), -1)
        label = "("+str(x)+", "+str(y)+")"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, label, (x+10, y-10), font, 1, (255,255,255))
        cv2.imshow(winname, img)

drawingStatus = False;
ix = 0
iy = 0

def drawOnDrag(event, x, y, flags, params):
    global ix, iy, drawingStatus
    if event == cv2.EVENT_LBUTTONDOWN:
        drawingStatus = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawingStatus == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255,0,255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawingStatus = False;
        cv2.rectangle(img, (ix, iy), (x, y), (255,0,255), -1)
    cv2.imshow(winname, img)

def drawRectOnDogFace():
    cv2.rectangle(img, (190, 370), (610, 700), (0,0,255), 5)
    cv2.imshow(winname, img)

# img = np.zeros(shape=(512,512,3), dtype=np.uint8)
cv2.imshow(winname, img)
# drawRectOnDogFace()
# cv2.setMouseCallback(winname, showCoord)
cv2.setMouseCallback(winname, drawOnDrag)
cv2.waitKey()
cv2.destroyAllWindows()
