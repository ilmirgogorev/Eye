import cv2
import numpy as np
in_img = cv2.imread("life_07.jpg")
cv2.namedWindow("HSL")
cv2.namedWindow("Size")
img = np.zeros((300, 512, 3), np.uint8)


def nothing(*x):
    pass


cv2.createTrackbar('size', 'Size', 1, 10, nothing)

while 1:

    size = cv2.getTrackbarPos('size', 'Size')
    if size == 0:
        cv2.namedWindow("Error")
        cv2.imshow("Error", img)
        cv2.putText(img, "Error", (256, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        size = 1
        cv2.waitKey(1000)
        cv2.destroyWindow("Error")
    dim = (int(in_img.shape[1] / size), int(in_img.shape[0] / size))
    rezult = cv2.resize(in_img, dim, interpolation=cv2.INTER_AREA)
    hsl = cv2.cvtColor(rezult, cv2.COLOR_BGR2HLS)

    cv2.imshow("Original image", rezult)
    cv2.imshow("HSL", hsl)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()