#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Handling missing data
import numpy as np
import pandas as pd
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data


# In[2]:


string_data.isnull()


# In[3]:


string_data[0] = None


# In[4]:


string_data.isnull()


# In[5]:


#Filtering out missing data
from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
data.dropna()


# In[6]:


data[data.notnull()]


# In[7]:


data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],[NA, NA, NA], [NA, 6.5, 3.]])

cleaned = data.dropna()

data


# In[8]:


cleaned


# In[9]:


data.dropna(how='all')


# In[11]:


data[4] = NA

data


# In[12]:


data.dropna(axis=1, how='all')


# In[14]:


df = pd.DataFrame(np.random.randn(7, 3))

df.iloc[:4, 1] = NA

df.iloc[:2, 2] = NA

df


# In[15]:


df.dropna()


# In[16]:


df.dropna(thresh=2)


# In[17]:


#Filling in missing data
df.fillna(0)


# In[18]:


df.fillna({1: 0.5, 2: 0})


# In[19]:


_ = df.fillna(0, inplace=True)

df


# In[20]:


df = pd.DataFrame(np.random.randn(6, 3))

df.iloc[2:, 1] = NA

df.iloc[4:, 2] = NA

df


# In[21]:


df.fillna(method='ffill')


# In[22]:


df.fillna(method='ffill', limit=2)


# In[23]:


data = pd.Series([1., NA, 3.5, NA, 7])

data.fillna(data.mean())


# In[ ]:




