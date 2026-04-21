import cv2
import pytesseract
import numpy as np
import os
from tkinter import Tk, filedialog

# IMPORTANT: Set Tesseract path (change if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# =========================
# OPTIONAL: File Picker
# =========================
def select_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    return file_path

# =========================
# LOAD IMAGE
# =========================
image_path = select_image()

# image_path = "D:/test.jpg"  # optional hardcode

if not image_path:
    print("No file selected")
    exit()

print("Loaded File:", image_path)

image = cv2.imread(image_path)

# Safe check
if image is None:
    print("Error: Unable to load image. Check path or file format.")
    exit()

orig = image.copy()

# =========================
# PREPROCESSING
# =========================
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur to remove noise
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Adaptive threshold
thresh = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11, 2
)

# Morphology to group text
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilate = cv2.dilate(thresh, kernel, iterations=1)

# =========================
# TEXT DETECTION
# =========================
contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("\nDetected Text:\n")

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Filter noise
    if w > 40 and h > 20:
        roi = orig[y:y+h, x:x+w]

        # OCR
        config = '--oem 3 --psm 6'
        text = pytesseract.image_to_string(roi, config=config)

        if text.strip():
            print(text.strip())

            # Draw rectangle
            cv2.rectangle(orig, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Put text label
            cv2.putText(orig, text.strip(), (x, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 1)

# =========================
# OUTPUT
# =========================
cv2.imshow("Text Detection + Recognition", orig)
cv2.waitKey(0)
cv2.destroyAllWindows()