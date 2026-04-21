import cv2


img = cv2.imread("ex2.jpg")
if img is None:
    print("Image not found!")
    exit()

# Resize factor (e.g., 50% of original size)
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize images
img_small = cv2.resize(img, dim)
avg_blur = cv2.resize(cv2.blur(img, (7, 7)), dim)
gaussian_blur = cv2.resize(cv2.GaussianBlur(img, (7, 7), 0), dim)
median_blur = cv2.resize(cv2.medianBlur(img, 7), dim)
bilateral_blur = cv2.resize(cv2.bilateralFilter(img, 9, 75, 75), dim)

# Display images
cv2.imshow("Original", img_small)
cv2.imshow("Average Blur", avg_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Bilateral Filter", bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
