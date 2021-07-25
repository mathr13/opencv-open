import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

winname = 'image_window'
cv2.namedWindow(winname, cv2.WINDOW_NORMAL)

save_address = "/Users/shishirmathur/Desktop/testingvid.mp4"

writer = cv2.VideoWriter(save_address, cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))
#  XVID-DVIX

while True:
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    writer.write(frame)
    cv2.imshow(winname, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
