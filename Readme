# Lane Detection System

[https://youtu.be/u1pZE5VpDAQ](https://youtu.be/u1pZE5VpDAQ)

## Canny Detector

**Real-Time Edge Detection Algorithm** - The fundamental goal of the algorithm is to detect sharp changes in luminosity (large gradients), such as a shift from white to black, and defines them as edges, given a set of thresholds.

**Noise Reduction -**

Convolve (Smooth) the image to lower the detector's sensitivity to noise.

**Intensity Gradient** -

Sovel ,Roberts,Prewitt Filter's

**Non-maximum suppression**

Is applied to “thin” and effectively sharpen the edges. For each pixel, the value is checked if it is a local maximum in the direction of the gradient calculated previously

**Hysteresis Thresholding** -

Weak Pixels should be final analyzed to determine whether it constitutes as a edge or noise.Applying two pre-defined minVal and maxVal threshold values, we set that pixel with intensity gradient lower than minVal are not edges and discarded.

Pixels with intensity gradient in between minVal and maxVal are only considered edges

# Python Code

![Lane%20Detection%20System%20360b4aa1666e42df995387f4a374d2a4/Untitled.png](Lane%20Detection%20System%20360b4aa1666e42df995387f4a374d2a4/Untitled.png)

```python
import cv2
import matplotlit.pylot as plt

img = cv2.imread('Image_Path')
plt.imshow(img)

grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
plt.imshow(grayscle)

blur = cv2.GaussianBlur(gray, (5, 5), 0)
plt.imshow(blur)

canny = cv2.Canny(blur, 50, 150)
plt.imshow(canny)
```

![Lane%20Detection%20System%20360b4aa1666e42df995387f4a374d2a4/Untitled%201.png](Lane%20Detection%20System%20360b4aa1666e42df995387f4a374d2a4/Untitled%201.png)

### Another Image Example

![Lane%20Detection%20System%20360b4aa1666e42df995387f4a374d2a4/Untitled%202.png](Lane%20Detection%20System%20360b4aa1666e42df995387f4a374d2a4/Untitled%202.png)
