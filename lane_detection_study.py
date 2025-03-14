# -*- coding: utf-8 -*-
"""Lane Detection Study.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jvIuqaQsD2DmtChpu5KyXNppC-N1UQKn
"""

# Importing Open CV Functions To Extract Image
# Convert The Image Into Grayscale
# Use Gaussian Blur
# Use Canny Edge Detector

import cv2
import matplotlib.pyplot as plt
# from google.colab.patches import cv2_imshow
import numpy as np

img1 = cv2.imread(
    'F:\GIT\Lane_Detection\Lane Detection Image Learning/Lane1.jpg')
plt.imshow(img1)
plt.show()

gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
plt.imshow(gray)
plt.show()

blur = cv2.GaussianBlur(gray, (5, 5), 0)
plt.imshow(blur)
plt.show()

canny = cv2.Canny(blur, 50, 150)
plt.imshow(canny)
plt.show()
# img2 = plt.imread('/content/Lane3.jpg')
# gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
# blur = cv2.GaussianBlur(gray, (5, 5), 0)
# # blur = np.uint8(blur)
# canny = cv2.Canny(blur, 50, 150)
# plt.imshow(img2)
# # plt.imshow(gray)
# # plt.imshow(blur)
# cv2_imshow(canny)

# img3 = plt.imread('/content/Lane2.jpeg')
# gray = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)
# blur = cv2.GaussianBlur(gray, (5, 5), 0)
# # blur = np.uint8(blur)
# canny = cv2.Canny(blur, 50, 150)
# plt.imshow(img3)
# # plt.imshow(gray)
# # plt.imshow(blur)
# cv2_imshow(canny)

plt.imshow(img1)
plt.show()
height = img1.shape[0]
# print(height)
# Creates a triangular polygon for the mask defined by three (x, y) coordinates
polygons = np.array([
    [(0, height), (800, height), (380, 290)]
])
# print(polygons)
# Creates an image filled with zero intensities with the same dimensions as the img1
mask = np.zeros_like(img1)
# print('The Image MASK {}'.format(mask))
# Allows the mask to be filled with values of 1 and the other areas to be filled with values of 0
cv2.fillPoly(mask, polygons, 255)
# A bitwise and operation between the mask and img1 keeps only the triangular area of th img2
segment = cv2.bitwise_and(img1, mask)
plt.imshow(segment)
plt.show()
