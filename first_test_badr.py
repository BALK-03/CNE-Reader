import pytesseract
import cv2 as cv
import PIL
import os
import matplotlib.pyplot as plt
import numpy as np
import re





# Page segmentation modes:
#   0    Orientation and script detection (OSD) only.
#   1    Automatic page segmentation with OSD.
#   2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
#   3    Fully automatic page segmentation, but no OSD. (Default)
#   4    Assume a single column of text of variable sizes.
#   5    Assume a single uniform block of vertically aligned text.
#   6    Assume a single uniform block of text.
#   7    Treat the image as a single text line.
#   8    Treat the image as a single word.
#   9    Treat the image as a single word in a circle.
#  10    Treat the image as a single character.
#  11    Sparse text. Find as much text as possible in no particular order.
#  12    Sparse text with OSD.
#  13    Raw line. Treat the image as a single text line,
#        bypassing hacks that are Tesseract-specific.

# OCR Engine modes:
#   0    Legacy engine only.
#   1    Neural nets LSTM engine only.
#   2    Legacy + LSTM engines.
#   3    Default, based on what is available.





img = cv.imread(r"C:\Users\Lakhal Badr\Desktop\PFA-OCR\test\test1.jpg")


# Changing the pixels mode from BGR to RGB
RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

gray = cv.cvtColor(RGB_img, cv.COLOR_BGR2GRAY)


# Creating a black image and drawing a rectangle in the area of the information
blank = np.zeros(img.shape[:2], dtype='uint8')

(x1, y1), (x2, y2) = (550, 522), (377, 1264)
blank_rect = cv.rectangle(blank, (x1, y1), (x2, y2), (255, 0, 255), -1)



detected_img = cv.bitwise_and(RGB_img, RGB_img, mask=blank_rect)



plt.figure()
plt.imshow(blank_rect)
# plt.imshow(detected_img)
plt.show()


plt.imshow(detected_img)
plt.show()

# config = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(detected_img)


pattern = r"Matricule N° : (\d+)\n+(\w+\s+\w+)"

match = re.search(pattern, text)

if match:
    (matricule, name) = match.group(1, 2)
    print(f"Student's name: {name}\nStudent's identification: {matricule}")

else:
    print("Error!")