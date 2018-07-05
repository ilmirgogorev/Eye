import cv2


in_img = cv2.imread("life_07.jpg")
cv2.namedWindow("Original image")
cv2.namedWindow("Mask")
cv2.namedWindow("Final")
cv2.namedWindow("settings")


def nothing(*x):
    pass


cv2.createTrackbar('h1', 'settings', 0, 180, nothing)
cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
cv2.createTrackbar('h2', 'settings', 180, 180, nothing)
cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
cv2.createTrackbar('g', 'settings', 5, 15, nothing)

while 1:

    hsv = cv2.cvtColor(in_img, cv2.COLOR_BGR2HSV)
    g = cv2.getTrackbarPos('g', 'settings')
    d = divmod(g, 2)
    if d[1] == 0:
        g = g - 1
    hsv = cv2.GaussianBlur(hsv, (g, g), 2)
    h1 = cv2.getTrackbarPos('h1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')

    h_min = (h1, s1, v1)
    h_max = (h2, s2, v2)

    mask = cv2.inRange(hsv, h_min, h_max)
    mask = cv2.dilate(mask, (5, 5), iterations=1)
    obj = cv2.bitwise_and(in_img, in_img, mask=mask)

    cv2.imshow("Original image", in_img)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Mask", mask)
    cv2.imshow("Final", obj)

    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()