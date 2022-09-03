#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


acad=pd.read_excel("D:/Sonali/data analytics/acad.xlsx")


# In[3]:


acad


# In[6]:


#cross table between gender and student's motivation
obs=pd.pivot_table(acad[['g','sm']],index='g',columns='sm',aggfunc=len)
obs


# In[8]:


##perform chi2 test to check independence
from scipy.stats import chi2_contingency


# In[9]:


chi2,p,dof,tbl=chi2_contingency(obs)


# In[10]:


chi2


# In[11]:


p


# In[12]:


dof


# In[13]:


tbl


# In[ ]:




