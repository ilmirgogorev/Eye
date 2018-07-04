import cv2
in_img = cv2.imread("life_07.jpg")
cv2.namedWindow("HSL")
hsl = cv2.cvtColor(in_img, cv2.COLOR_BGR2HLS)
cv2.imshow("Original image", in_img)
cv2.imshow("HSL", hsl)
cv2.waitKey(0)