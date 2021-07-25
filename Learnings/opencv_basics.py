import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# np.random.seed(100)
# pic = Image.open('/Users/shishirmathur/Downloads/Computer-Vision-with-Python/DATA/00-puppy.jpg')
# pic_arr = np.asarray(pic)
# plt.imshow(pic_arr)
#
# pic_array_red = pic_arr[:,:,0]
# pic_array_green = pic_arr[:,:,1]
# pic_array_blue = pic_arr[:,:,2]
#
# print(pic_array_blue)


# arr = np.arange(0,25).reshape((5,5))
# arr[:,:] = 10
#
# arr1 = np.random.randint(0,100,(5,5))
#
# print(pic_arr[0:3,:,0])

winname = 'image'
cv2.namedWindow(winname,cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname, 302,600)
img = cv2.imread('/Users/shishirmathur/Downloads/Computer-Vision-with-Python/DATA/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
cv2.moveWindow(winname, 978,60)
cv2.imshow('image', img)
cv2.waitKey(0)

#closing all open windows
cv2.destroyAllWindows()
print(type(img))
