import cv2

imgone = cv2.imread('/Users/shishirmathur/Downloads/Computer-Vision-with-Python/DATA/00-puppy.jpg', cv2.COLOR_BGR2RGB)
imgtwo = cv2.imread('/Users/shishirmathur/Downloads/Computer-Vision-with-Python/DATA/watermark_no_copy.png', cv2.COLOR_BGR2RGB)

winname = 'image_window'
cv2.namedWindow(winname,cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname, 302,600)
cv2.moveWindow(winname, 978,60)

imgone = cv2.resize(imgone, (1000,1000))
imgtwo = cv2.resize(imgtwo, (1000,1000))

print(imgone.shape)
print(imgtwo.shape)

x_offset = 0
y_offset = 0

x_end = x_offset + imgtwo.shape[1]
y_end = y_offset + imgtwo.shape[0]

# blendedImage = cv2.addWeighted(src1=imgtwo, alpha=0.4, src2=imgtwo, beta=0.0, gamma=0)
#
# imgone[y_offset:y_end, x_offset:x_end] = blendedImage

blendedImage = cv2.addWeighted(src1=imgone, alpha=1, src2=imgtwo, beta=0.2, gamma=1)

while True:
    # cv2.imshow(winname, imgone)
    cv2.imshow(winname, blendedImage)
    if cv2.waitKey():
        break

#closing all open windows
cv2.destroyAllWindows()
