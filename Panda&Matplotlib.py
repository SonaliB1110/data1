#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[4]:


#Load the dataset
data1=pd.read_csv('D:\Sonali\data analytics\gapminder-FiveYearData.csv')


# In[6]:


#display dataset
data1


# In[7]:


#display the head of the dataset(shows only 5 rows)
data1.head()


# In[8]:


#get number of rows and columns
print(data1.shape)


# In[9]:


#get column names
data1.columns


# In[10]:


#get the dtype of each column
data1.dtypes


# In[11]:


#get more information about data
data1.info()


# In[12]:


#looking at Columns,Rows and cells
#get the country column and save it in a new variable
country_data=data1['country']
#show the first 5 observation
country_data.head()


# In[13]:


#show the last 5 observation
country_data.tail()


# In[15]:


#looking at country,continent and year
subset=data1[['country','continent','year']]
subset.head()


# In[16]:


#Looking at country,continent and year
subset=data1[['country','continent','year']]
subset.head()


# In[17]:


subset.tail()


# In[18]:


#Analytical summary of the dataset
data1.describe(include='all')


# In[19]:


#Histogram of all the variables in the dataset
data1.hist(figsize=(10,5))


# In[20]:


#relationship between catagorical and continuous variable
sns.boxplot(x="year",y="lifeExp",data=data1)


# In[21]:


#Drop irrelevant columns
data1=data1.drop(['year'],axis='columns')
data1.head(5)


# In[22]:


#Renaming the column name
data1=data1.rename(columns={"country":"Countries"})
data1.head(5)


# In[23]:


#Rows containing duplicate data
duplicate_rows=data1[data1.duplicated()]
print('Number of duplicate rows:',duplicate_rows.shape)


# In[24]:


#count the rows before moving the data
data1.count()


# In[ ]:




