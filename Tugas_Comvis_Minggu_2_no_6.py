
from numpy import *
from numpy import random
from scipy.ndimage import filters
from PIL import *
from PIL import Image
from pylab import *
from scipy.ndimage import measurements, morphology

im = array(Image.open('foto.jpg').convert('L'))
im = 1*(im<128)

labels, nbr_objects = measurements.label(im)
print ("Number of objects", nbr_objects)

figure(figsize=(6, 12))
imshow(labels)
show()

figure()
hist(labels.flatten())
axis([5, 45, 0, 50000])
show()