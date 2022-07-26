#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
# Our image processing tools
import skimage.filters
import skimage.io as io
import skimage.morphology
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageOps


# In[2]:


im_list2 = []


# In[3]:


import os
path = r"C:\Users\Виталик\Desktop\project"


# In[4]:


def process(filename):
    img=Image.open(filename)
    im = img.convert('RGB')
    im = ImageOps.grayscale(im)
    plt.imshow(im)
    im_list2.append(im)
    print(im_list2)
    


# In[116]:


image2 = r"C:\Users\Виталик\Documents\bak1.png"


# In[7]:


process(image2)


# In[8]:


import glob
for file in glob.glob(r'C:\Users\Виталик\Desktop\project/*.bmp'):
    process(file)


# In[17]:


plt.imshow(im_list2[0])


# In[10]:


plt.imshow(im_list2[2])


# In[31]:


fig, axes = plt.subplots(ncols=7)
axes.ravel()
axes[0].imshow(im_list2[0])
axes[1].imshow(im_list2[1])
axes[2].imshow(im_list2[2])
axes[3].imshow(im_list2[3])
axes[4].imshow(im_list2[4])
axes[5].imshow(im_list2[5])
axes[6].imshow(im_list2[6])


# In[36]:


fig, ax = plt.subplots(2, 2, sharex='col', sharey='row')
ax[0,0].imshow(im_list2[0], cmap="gray")
ax[0,1].imshow(im_list2[1], cmap="gray")
ax[1,0].imshow(im_list2[2], cmap="gray")
ax[1,1].imshow(im_list2[3], cmap="gray")



# In[ ]:





# In[10]:


im_list2


# In[37]:


im_list2[5]


# In[12]:


plt.imshow(im_list2[5])


# In[13]:


im_list2[4]


# In[41]:


from skimage.filters import roberts, sobel, scharr, prewitt


# In[102]:


img2 = im_list[2]


# In[120]:


im_listspl = []


# In[121]:


def crops(filename, number):
    im = Image.open(filename)
    w, h = im.size
    unit = w//6
    for n in range(number):
        im1 = im.crop((unit *n,0, unit * (n+1),h))
        im_listspl.append(im1)
        print(im_listspl)
        
    


# In[122]:


crops(image2,4)


# In[124]:


im_listspl[3]


# In[118]:


Image.open(image2)


# In[117]:





# In[125]:


from skimage.filters import meijering, sato, frangi, hessian


# In[133]:


from numpy import asarray
im3 = asarray(im_list2[2])


# In[134]:


print(im3)


# In[135]:


mej = meijering(im3)


# In[138]:


plt.imshow(mej, cmap='gray')


# In[139]:


sato1 = sato(im3)
plt.imshow(sato1)


# In[140]:


hes = hessian(im3)
plt.imshow(hes)


# In[141]:


im_listrid = []


# In[146]:


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
    
    


# In[147]:


ridge(im3)


# In[ ]:





# In[98]:





# In[ ]:





# In[80]:


from skimage import util, exposure, io, measure, feature


# In[ ]:





# In[94]:


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
    
    


# In[95]:


filters(im_list2[2])


# In[89]:


filters(im_list2[3])


# In[88]:


filters(im_list2[1])


# In[15]:


fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True,
                        figsize=(8,8))
ax = axes.ravel()


# In[19]:




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

  
    
    


# In[17]:


for img in im_list2:
    filts(img)


# In[20]:


filts(im_list2[3])


# In[ ]:




