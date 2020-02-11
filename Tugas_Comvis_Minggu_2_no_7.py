
from numpy import *
from numpy import random
from scipy.ndimage import filters
from PIL import *
from pylab import *
from scipy.ndimage import measurements, morphology
from PIL import Image

im2 = array(Image.open('foto.jpg').convert('L'))
im2 = 1*(im2<64)
im_open = morphology.binary_opening(im2, ones((6, 3)), iterations=4)
figure(figsize=(8, 12))
subplot(1, 2, 1)
imshow(im2)
subplot(1, 2, 2)
imshow(im_open)
show()

labels2, nbr_objects2 = measurements.label(im_open)
print("Number of objects", nbr_objects2)

center = measurements.center_of_mass(im_open, labels2, range(nbr_objects2))

figure(figsize=(8, 8))
imshow(im_open)
for i in range(nbr_objects2):
    plot(center[i][1], center[i][0], "*")
show()

