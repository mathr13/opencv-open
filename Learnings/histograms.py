import cv2
import matplotlib.pyplot as plt
import numpy as np

base_addresss = "/Users/shishirmathur/Downloads/Computer-Vision-with-Python/DATA/"

blue_bricks = cv2.imread(base_addresss+'bricks.jpg')
rainbow = cv2.imread(base_addresss+'rainbow.jpg')
horse = cv2.imread(base_addresss+'horse.jpg')
red_colour = cv2.imread(base_addresss+'red_colour.png')
black_colour = cv2.imread(base_addresss+'black_colour.jpg')
white_colour = cv2.imread(base_addresss+'white_colour.jpg')
black_colour000 = cv2.imread(base_addresss+'black_colour00.png')
red_colour255 = cv2.imread(base_addresss+'red_colour255.png')
mid_colour_one = cv2.imread(base_addresss+'mid_colour_one.png')
mid_colour_two = cv2.imread(base_addresss+'mid_colour_two.png')

blue_bricks_rgb = cv2.cvtColor(blue_bricks, cv2.COLOR_BGR2RGB)
rainbow_rgb = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)
horse_rgb = cv2.cvtColor(horse, cv2.COLOR_BGR2RGB)

winname = 'image_window'
cv2.namedWindow(winname,cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname, 302,600)
cv2.moveWindow(winname, 978,60)

# histogram_red = cv2.calcHist([red_colour], [2], None, [256], [0,256])
# histogram_green = cv2.calcHist([red_colour], [1], None, [256], [0,256])
# histogram_blue = cv2.calcHist([red_colour], [0], None, [256], [0,256])
# print(histogram.shape)

def showImageWithGraph(image):
    histogram_red = cv2.calcHist([image], [2], None, [256], [0,256])
    histogram_green = cv2.calcHist([image], [1], None, [256], [0,256])
    histogram_blue = cv2.calcHist([image], [0], None, [256], [0,256])
    while True:
        cv2.imshow(winname, image)
        plt.plot(histogram_red, color = 'red', linewidth = 1)
        plt.plot(histogram_green, color = 'green', linewidth = 1)
        plt.plot(histogram_blue, color = 'blue', linewidth = 1)
        plt.show()
        if cv2.waitKey():
            break

def showImageWithGraphWithInversion(image):
    histogram_red = cv2.calcHist([image], [2], None, [256], [0,256])
    histogram_green = cv2.calcHist([image], [1], None, [256], [0,256])
    histogram_blue = cv2.calcHist([image], [0], None, [256], [0,256])
    inv_image = cv2.bitwise_not(image)
    inv_histogram_red = cv2.calcHist([inv_image], [2], None, [256], [0,256])
    inv_histogram_green = cv2.calcHist([inv_image], [1], None, [256], [0,256])
    inv_histogram_blue = cv2.calcHist([inv_image], [0], None, [256], [0,256])
    while True:
        cv2.imshow(winname, image)
        plt.plot(histogram_red, color = 'red')
        plt.plot(histogram_green, color = 'green')
        plt.plot(histogram_blue, color = 'blue')
        plt.plot(inv_histogram_red, color = 'cyan', linestyle="dashed", linewidth = 2)
        plt.plot(inv_histogram_green, color = 'magenta', linestyle="dashed", linewidth = 2)
        plt.plot(inv_histogram_blue, color = 'yellow', linestyle="dashed", linewidth = 2)
        plt.show()
        if cv2.waitKey():
            break
# showImageWithGraph(black_colour000)

mask = np.ones(red_colour.shape[:2], dtype=np.uint8)
mask[10:40,30:60] = 0
and_image = cv2.bitwise_and(red_colour, red_colour, mask = mask)

showImageWithGraph(and_image)
# showImageWithGraphWithInversion(red_colour)

# while True:
#     cv2.imshow(winname, red_colour)
#     plt.plot(histogram_red, color = 'red')
#     plt.plot(histogram_green, color = 'green')
#     plt.plot(histogram_blue, color = 'blue')
#     plt.show()
#     if cv2.waitKey():
#         break

#closing all open windows
cv2.destroyAllWindows()
