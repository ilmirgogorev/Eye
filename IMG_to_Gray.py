import cv2
in_img = cv2.imread("life_07.jpg")
cv2.namedWindow("Gray")
gray = cv2.cvtColor(in_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original image", in_img)
cv2.imshow("Gray", gray)
cv2.waitKey(0)