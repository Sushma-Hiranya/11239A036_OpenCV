import cv2

# Load the image
img = cv2.imread("ex2.jpg")
if img is None:
    print("Image not found!")
    exit()

# Resize factor (e.g., 50% of original size)
scale_percent = 50  # change this to adjust size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize original image
img_small = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Flip images
flip_vertical = cv2.flip(img_small, 0)
flip_horizontal = cv2.flip(img_small, 1)
flip_both = cv2.flip(img_small, -1)

# Display images
cv2.imshow("Original", img_small)
cv2.imshow("Vertical Flip", flip_vertical)
cv2.imshow("Horizontal Flip", flip_horizontal)
cv2.imshow("Both Flip", flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
