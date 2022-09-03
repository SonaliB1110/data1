#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

df=pd.read_csv("D:/Sonali/data analytics/employees.csv")

print(df.head())


# In[2]:


print(df.dtypes)
print(df.describe())


# In[3]:


print('Salary')
print(df['Salary'].head(10))


# In[4]:


print(df['Gender'].head(10))


# In[6]:


missing_value_formats=["n.a.","?","NA","n/a","na","--"]
df=pd.read_csv("D:/Sonali/data analytics/employees.csv",na_values=missing_value_formats)

print(df['Gender'].head(10))


# In[7]:


missing_value_formats=["n.a.","?","NA","n/a","na","--"]
df=pd.read_csv("D:/Sonali/data analytics/employees.csv",na_values=missing_value_formats)

def make_int(i):
    try:
        return int(i)
    except:
        return pd.np.nan
    
df['Salary']=df['Salary'].map(make_int)
print(df['Salary'].head())


# In[8]:


print(df['Gender'].isnull().head(10))
print(df['Gender'].notnull().head(10))


# In[9]:


null_filter=df['Gender'].notnull()
print(df[null_filter].head())


# In[10]:


print(df.isnull().values.any())


# In[11]:


print(df.isnull().sum())


# In[12]:


new_df=df.dropna(axis=0)

print(new_df.isnull().values.any())


# In[13]:


new_df=df.dropna(axis=0,how='any')

new_df=df.dropna(axis=0,how='all')

new_df=df.dropna(axis=1,how='any')

new_df=df.dropna(axis=1,how='all')


# In[14]:


df['Salary'].fillna(0)


# In[15]:


df['Gender'].fillna('No Gender')


# In[16]:


df['Salary'].fillna(method='pad')


# In[17]:


df['Salary'].fillna(method='bfill')


# In[18]:


df['Salary'].fillna(df['Salary'].median())


# In[19]:


df['Salary'].fillna(int(df['Salary'].mean()))


# In[20]:


df['Salary'].replace(to_replace=np.nan,value=0)


# In[21]:


df['Salary'].interpolate(method='linear',direction='forward')


# In[ ]:




