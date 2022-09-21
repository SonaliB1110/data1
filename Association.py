#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Libraries
import pandas as pd


# In[2]:


#Load the data
dataset=pd.read_csv('D:/Sonali/data analytics/retail_bakery_transactions.csv')


# In[3]:


dataset.columns=dataset.columns.str.lower()


# In[4]:


dataset=dataset.applymap(lambda s:s.lower()if type(s)==str else s)


# In[5]:


dataset.head()


# In[6]:


dataset.info()


# In[7]:


dataset.isnull().sum()


# In[8]:


transaction_list=dataset.groupby(['transaction','date_time'])['item'].apply(lambda x:list(x))


# In[9]:


transaction_list.head()


# In[10]:


df=transaction_list.values.tolist()


# In[11]:


df[:5]


# In[14]:


from mlxtend.preprocessing import TransactionEncoder


# In[15]:


encoder=TransactionEncoder().fit(df)


# In[16]:


onehot=encoder.transform(df)


# In[17]:


transf_df=pd.DataFrame(onehot,columns=encoder.columns_)


# In[18]:


transf_df.head()


# In[19]:


from mlxtend.frequent_patterns import fpgrowth


# In[20]:


frequent_itemsets=fpgrowth(transf_df,min_support=0.05,use_colnames=True)


# In[21]:


frequent_itemsets.sort_values('support',ascending=False)


# In[22]:


frequent_itemsets['length']=frequent_itemsets['itemsets'].apply(lambda x:len(x))
frequent_itemsets


# In[23]:


frequent_itemsets['length'].value_counts()


# In[24]:


from mlxtend.frequent_patterns import association_rules


# In[25]:


rules=association_rules(frequent_itemsets,metric='lift',min_threshold=1.0)


# In[26]:


rules.head()


# In[ ]:




