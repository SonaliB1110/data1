#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[2]:


import matplotlib as mpl
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression
from scipy import stats


# In[3]:


tbl=pd.read_excel("D:/Sonali/data analytics/regr.xlsx")
tbl


# In[6]:


tbl.plot('TV Ads','car Sold',style='o')
plt.ylabel('car Sold')
plt.title('Sales in several UK Regions')
plt.show()


# In[17]:


t=tbl['TV Ads']
c=tbl['car Sold']


# In[18]:


import statsmodels.api as sm
t=s.add_constant(t)
model1=sm.OLS(c,t)
result1=model1.fit()
print(result1.summary())

