#!/usr/bin/env python
# coding: utf-8

# # Duplicate Product Listing
# 
# The dataset for this project originates from the [Lead Talent Acquisition Specialist](https://drive.google.com/open?id=1fR0KHk5nJpXxFbV5ls24CrtB3uA0hGxv) The datset was donated by Madhav Kommineni. 
# 
# **My Goal**:- 
# In this project, main goal is that pick two product and compare, these items are similar or not. If two product are same then output is Yes, if not same then output is No.  
# 
# ## Take a first look at the data
# 
# The first thing we'll need to do is load in the libraries and datasets we'll be using. For today, I'll be using a dataset of E-commerce donated by Madhav Kommineni
# 

# In[1]:


# modules we'll use
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read all datasets and display first 20 rows to check NaN or empty value , carefully.

# In[2]:


#read all dataset
data = pd.read_csv('datafile.csv')
data.head(20)


# In[3]:


data.shape


# ## Check For  missing values 
# 
# we find lot of data is empty column wise and also row wise (but in less number). There are many method to drop data which is give follwing.
# 
# * we Will drop all rows that have any missing values by using command--->  #data.dropna(inplace=True) 
# * You can also select to drop the rows only if all of the values in the row are missing. --->     #data.dropna(how='all',inplace=True)
# * Sometimes, you may just want to drop a column (variable) that has some missing values. ---> #data.dropna(axis=1,inplace=True)
# * Back-fill or forward-fill to propagate next or previous values respectively. ---> #       a. data.fillna(method='bfill',inplace=True) b. data.fillna(method='ffill',inplace=True)

# In[4]:


missing_value_count = data.isnull().sum()
# look at the # of missing points in the first twenty columns
missing_value_count[0:20]


# In[5]:


#missing_value_count
Total_missing = missing_value_count.sum()

Total_cells = np.product(data.shape)
Total_pecentage_of_missingValue = (Total_missing / Total_cells) *100
print('Total missing percent {} %'.format(Total_pecentage_of_missingValue))


# In[6]:


taget = data['productId']
taget.head()


# In[7]:


features = data.drop('productId', axis=1)
features.head()


# ## In my opinion, 
# Back-fill or forward-fill is always better to keep data than to delete them. The only case that it may worth deleting a variable is when its missing values are more than 60% of the observations but only if that variable is insignificant. Taking this into consideration, imputation is always a preferred choice over deleting variables.

# In[8]:


#features.dropna(axis=1,inplace=True)

features.fillna(method='bfill',inplace=True)
features.head()


# In[9]:


#look 10 to 20 rows and 20 to 30 columns
features.iloc[10:20,20:30]


# In[10]:


#sellerAverageRating:- Keyali, sellerNoOfRatings :- Usually Delivered in 5 - 6 days., sellerNoOfReviews:- Free, 
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
numerical = ['mrp', 'sellingPrice','specialPrice', 'discount', 'shippingCharges' ]
features[numerical] = scaler.fit_transform(features[numerical])
features.head()

