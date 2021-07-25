import cv2
import numpy as np

imgone = cv2.imread('/Users/shishirmathur/Downloads/Computer-Vision-with-Python/DATA/dog_backpack.png', cv2.COLOR_BGR2RGB)
imgtwo = cv2.imread('/Users/shishirmathur/Downloads/Computer-Vision-with-Python/DATA/watermark_no_copy.png', cv2.COLOR_BGR2RGB)

winname = 'image_window'
cv2.namedWindow(winname,cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname, 302,600)
cv2.moveWindow(winname, 978,60)

imgone = cv2.resize(imgone, (600,600))
imgtwo = cv2.resize(imgtwo, (600,600))

column = 600
row = 600

roi = imgone[:column, :row]
img2gray = cv2.cvtColor(imgtwo, cv2.COLOR_RGB2GRAY)
maskinv = cv2.bitwise_not(img2gray)

whitebkg = np.ones(shape=(600,600), dtype=np.uint8)
whitebkg.fill(255)
masked = cv2.bitwise_or(whitebkg, whitebkg, mask = maskinv)

foreground = cv2.bitwise_or(imgtwo, imgtwo, mask = masked)

blendedImage = cv2.addWeighted(src1=imgone, alpha=1, src2=foreground, beta=1, gamma=5)

while True:
    # cv2.imshow(winname, imgone)
    cv2.imshow(winname, blendedImage)
    if cv2.waitKey():
        break

#closing all open windows
cv2.destroyAllWindows()
