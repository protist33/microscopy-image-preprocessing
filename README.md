# microscopy-image-preprocessing
The first part of project which we make with the team of my students
I have been teaching some programming skills with my biology students, and some of them want to study it deeper.
we started to make one project about image preprocessing. Firstly they studied main functions of scikit-image package,
used for one image, for understanding like it works. Finally they made some functions. After we want to make any system for
microorganisms recognition( I think about a machine learning algorithm 
```
import numpy as np
import pandas as pd
# Our image processing tools
import skimage.filters
import skimage.io as io
import skimage.morphology
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageOps
```
Make the first empty list and the path to the folder with images
```
im_list2 = []
import os
path = r"C:\Users\Виталик\Desktop\project"
```
After the first function, which take an image, open it, convert to RGB(from RGBA)
to grayscale, append it to the list and show it. 
```
def process(filename):
    img=Image.open(filename)
    im = img.convert('RGB')
    im = ImageOps.grayscale(im)
    plt.imshow(im)
    im_list2.append(im)
    print(im_list2)
```
So, we use it to every image in the folder
```
import glob
for file in glob.glob(r'C:\Users\Виталик\Desktop\project/*.bmp'):
    process(file)
```    
I can look at any image from the list
```
plt.imshow(im_list2[0])
```
![1](https://user-images.githubusercontent.com/90727271/181111954-4bf08973-195c-423f-a20e-513af596ff55.png)
I wanna observe all images 
```
fig, axes = plt.subplots(ncols=7, figsize = (20,15))
axes.ravel()
axes[0].imshow(im_list2[0])
axes[1].imshow(im_list2[1])
axes[2].imshow(im_list2[2])
axes[3].imshow(im_list2[3])
axes[4].imshow(im_list2[4])
axes[5].imshow(im_list2[5])
axes[6].imshow(im_list2[6])
```
![3](https://user-images.githubusercontent.com/90727271/181113328-3e6afaed-2650-41cb-979b-3d5d57a51aa8.png)
And in the grayscale
```
fig, ax = plt.subplots(2, 2, sharex='col', sharey='row')
ax[0,0].imshow(im_list2[0], cmap="gray")
ax[0,1].imshow(im_list2[1], cmap="gray")
ax[1,0].imshow(im_list2[2], cmap="gray")
ax[1,1].imshow(im_list2[3], cmap="gray")
```
![4](https://user-images.githubusercontent.com/90727271/181113694-7c114076-8bfd-41af-83bc-d5538a01503a.png)
If I dont use imshow, I see what every image is already gray
```
im_list2[5]
```
![5](https://user-images.githubusercontent.com/90727271/181114219-d3a771cd-d530-49d1-b72c-94a5c10fcd71.png)
Import some main tipes of ridge filters 
```
from skimage.filters import meijering, sato, frangi, hessian
```
I can use one for example
```
mej = meijering(im3)
plt.imshow(mej, cmap='gray')
```
![6](https://user-images.githubusercontent.com/90727271/181116329-f856d6cb-08a2-404d-ab80-73097059b4c4.png)
Make another list and a function for using filters to every image and add to the list
```
def ridge(filename):
    sat = sato(filename)
    im_listrid.append(sat)
    hes = hessian(filename)
    im_listrid.append(hes)
    mej = meijering(filename)
    im_listrid.append(mej)
    fig, axe = plt.subplots(ncols=3, figsize = (15,10))
    axe[0].imshow(im_listrid[0])
    axe[1].imshow(im_listrid[1])
    axe[2].imshow(im_listrid[2])
```
![7](https://user-images.githubusercontent.com/90727271/181116755-f4115d7f-221f-4c21-91ac-3781ebdcaf1d.png)
Another function 
```
from skimage import util, exposure, io, measure, feature
```
We write a function that apply every filter to the image, append it to the list and show the plot
```
def filters(filename):
    im_listf = []
    sob = sobel(filename)
    sob = exposure.adjust_gamma(sob, gamma=0.5)
    im_listf.append(sob)
    rob = roberts(filename)
    rob = exposure.adjust_gamma(rob, gamma=0.5)
    im_listf.append(rob)
    pew = prewitt(filename)
    pew = exposure.adjust_gamma(pew, gamma=0.5)
    im_listf.append(pew)
    fig, ax = plt.subplots(ncols= 3, figsize=(40,20))
    ax[0].imshow(im_listf[0], cmap='gray')
    ax[1].imshow(im_listf[1], cmap='gray')
    ax[2].imshow(im_listf[2], cmap='gray')
```
apply to the image from the list
```
filters(im_list2[2])
```
![8](https://user-images.githubusercontent.com/90727271/181119110-bca9001d-2a24-4cad-a532-cabcd64cea74.png)
Another variant of the function
```
def filts(file):
    ig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True,
                        figsize=(8,8))
    ax = axes.ravel()
    sob = sobel(file)
    rob = roberts(file)
    prew = prewitt(file)
    sc = scharr(file)
    ax[0].imshow(file)
    ax[0].set_title("Original")
    ax[1].imshow(sob)
    ax[1].set_title("Sober")
    ax[2].imshow(rob)
    ax[2].set_title("Roberts")
    ax[3].imshow(sc)
    ax[3].set_title("Scharr")
    for a in ax:
        a.axis('off')
    plt.tight_layout() 
    plt.show
filts(im_list2[3])
```
![9](https://user-images.githubusercontent.com/90727271/181119498-3549e21a-fd9a-47bb-b272-7bd6c7b13ac7.png)
 



















    
    
















































    




















    
    



























