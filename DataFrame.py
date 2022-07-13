#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing python library
import pandas as pd
import numpy as np


# In[2]:


#DataFrme will have its index assigned automatically,
#the columns are placed in sorted order
data={'state':['Ohio','Ohio','Ohio','Neveda','Neveda','Neveda'],'year':[2000,2001,2002,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame=pd.DataFrame(data)
#using the Jupyter notebook,pandas DataFrame objects will be displayed as a more brower-friendly HTML table.
frame


# In[3]:


#head method selects only first five rows
frame.head()


# In[4]:


#specify a sequence od columns
pd.DataFrame(data,columns=['year','state','pop'])


# In[5]:


#If you pass a column that isn't contained in the dict,it will appear with missing values in the result
frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
frame2


# In[6]:


frame2.columns


# In[7]:


#A column in a DataFrame can be retrieved as a Series either by dict-like notation or by attribute
frame2['state']


# In[8]:


frame2.year


# In[9]:


#Rows can be retrieved by position or name with the special loc attribute
frame2.loc['three']


# In[10]:


#Columns can be modified by assignment
#'debt' column could be assigned a scalar value or an array of values
frame2['debt']=16.5
frame2


# In[11]:


frame2['debt']=np.arange(6.)
frame2


# In[12]:


#assign a Series,its labels will be realigned exactly to the DataFrame's index,inserting missing values in any holes
val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
frame2


# In[13]:


#add a new column of boolean values where the state column equals 'Ohio'
frame2['eastern']=frame2.state=='Ohio'
frame2


# In[14]:


#The del method can then be used to remove this column
del frame2['eastern']
frame2.columns


# In[15]:


#data is a nested dict of dicts
pop={'Neveda':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3=pd.DataFrame(pop)
frame3


# In[16]:


frame3.T


# In[17]:


#sorted to form the index in the result
pd.DataFrame(pop,index=[2001,2002,2003])


# In[18]:


#DataFrame's index and columns have their name attributes set
frame3.index.name='year';frame3.columns.name='state'
frame3


# In[19]:


#values attributes returns the data contained in the DataFrame as a two-dimensional ndarray
frame3.values


# In[20]:


frame2.values


# In[ ]:




