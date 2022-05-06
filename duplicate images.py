#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib
from scipy.misc import imread, imresize, imshow
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
get_ipython().run_line_magic('matplotlib', 'inline')
import time
import numpy as np


# In[ ]:


from hashlib import md5


# In[ ]:


def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return md5(f.read()).hexdigest()


# In[2]:


import os


# In[3]:


os.getcwd()


# In[ ]:





# In[40]:


os.chdir(r'F:\kuthea\all_pictures\48-1')
os.getcwd()


# In[41]:


file_list = os.listdir()
print(len(file_list))


# In[42]:


import hashlib,os
duplicates = []
hash_keys = dict()
for index, filename in  enumerate(os.listdir('.')):  #listdir('.') = current directory
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys: 
            hash_keys[filehash] = index
        else:
            duplicates.append((index,hash_keys[filehash]))


# In[43]:


duplicates


# In[44]:


from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
for file_indexes in duplicates[:30]:
    try:
    
        plt.subplot(121),plt.imshow(imread(file_list[file_indexes[1]]))
        plt.title(file_indexes[1]), plt.xticks([]), plt.yticks([])

        plt.subplot(122),plt.imshow(imread(file_list[file_indexes[0]]))
        plt.title(str(file_indexes[0]) + ' duplicate'), plt.xticks([]), plt.yticks([])
        plt.show()
    
    except OSError as e:
        continue


# In[45]:


for index in duplicates:
    os.remove(file_list[index[0]])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




