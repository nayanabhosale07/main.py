import numpy as np
import cv2

img = cv2.imread('resource/siemens-star-05.jpg', 0)
template = cv2.imread('resource/siemens-star-1.jpg', 0)  # this algorithm is done using gray scale

h, w = template.shape[::]
print(img)

methods = [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for methods in methods:
 img2 = img.copy()

result = cv2.matchTemplate(img2, template, methods)
# this method performs convolution

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

if methods in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
   location = min_loc
else:
   location = max_loc

   bottom_right = (location[0] + w, location[1] + h)
   cv2.rectangle(img2, location, bottom_right, 255, 5)
   cv2.imshow('Match', img2)
   cv2.waitKey(0)
   cv2.destroyAllWindows()