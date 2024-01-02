#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[10]:


df = pd.read_csv("C:\\Users\\DELL\\Downloads\\housing.csv")
df.head()


# In[11]:


df.shape


# Handling Missing Values: Identify and briefly describe the strategy to handle missing values in each dataset.
# 
# Removal of Duplicates: Briefly explain how you would identify and remove duplicate entries in each dataset.
# 
# Removal of Outliers - Using IQR Method: Provide a concise overview of how the Interquartile Range (IQR) method would be applied to detect and remove outliers in each dataset

# In[12]:


df.dtypes


# In[13]:


df.drop_duplicates(inplace=True)


# In[14]:


df.isnull().sum()


# In[15]:


df['total_bedrooms'].agg(['mean','median'])


# In[18]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[19]:


sns.boxplot(x=df['total_bedrooms'])
plt.show()


# In[20]:


Q1 = df['total_bedrooms'].quantile(0.25)
Q3 = df['total_bedrooms'].quantile(0.75)
IQR = Q3 - Q1

threshold = 1.5
outliers = df[(df['total_bedrooms'] < Q1 - threshold * IQR) | (df['total_bedrooms'] > Q3 + threshold * IQR)]

num_outliers = len(outliers)
print(f"Number of outliers: {num_outliers}")


# In[21]:


df['total_bedrooms'].count()


# In[24]:


df.isnull().sum()


# In[ ]:




