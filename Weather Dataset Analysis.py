#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"C:\Users\kudali vasuki\Favorites\Downloads\archive (1)\weather.csv")


# In[3]:


data


# In[5]:


data.head()


# In[6]:


data.shape


# In[8]:


data.index


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[13]:


data['MinTemp'].unique()


# In[14]:


data.nunique()


# In[15]:


data.count()


# In[17]:


data['MinTemp'].value_counts()


# In[18]:


data.info()


# In[ ]:


# 1.find all the" MinTemp "values in data


# In[19]:


data.nunique()


# In[38]:


data["MinTemp"].nunique()


# In[39]:


data["MinTemp"].unique()


# In[ ]:


# 2.Find the no. of times when the "RainTomorrow" is exactly yes


# In[22]:


data.head(2)


# In[42]:


#value_counts()
data.RainTomorrow.value_counts()


# In[34]:


#filtering

data[data.RainTomorrow == "Yes"]


# In[36]:


#groupby()
#data.head(2)
data.groupby("RainTomorrow").get_group("Yes")


# In[49]:


# 3.find the number of times the rainfall is exactly o.o


# In[48]:


data.head(2)


# In[47]:


data.groupby("Rainfall").get_group(0.0)


# In[52]:


data[data.Rainfall == 0.0]


# In[53]:


# 4. find the null values
data.isnull() #gives answer in boolean form


# In[54]:


data.isnull().sum()


# In[55]:


data.notnull().sum()


# In[ ]:


# 5.rename the column name 'rainfall' as 'rain'


# In[56]:


data.head(2)


# In[57]:


data.rename(columns = {"Rainfall" : "Rain"})
#data.rename(columns = {"Rainfall" : "Rain"}, inplace = True) rename permenantly


# In[ ]:


# 6.Mean RISK


# In[58]:


data.head(2)


# In[64]:


data.RISK_MM.mean()


# In[65]:


# 7.Standard deviation 
data.Cloud9am.std()


# In[66]:


# 8.Variance
#if there is no space between name we use . if there is a gap we use[]
data.MaxTemp.var()


# In[ ]:


# 9.find all instances


# In[68]:


#value_counts
#data.head(2)
data.MinTemp.value_counts()


# In[70]:


#filtering
data[data.MinTemp == 1]


# In[78]:


data.rename(columns = {"RainToday" : "Rain Today"}, inplace = True)


# In[79]:


data[data["Rain Today"].str.contains("Yes")]


# In[ ]:


# 10.Find all instances when "Sun Shine" is above 9 and "Cloud3pm" is above 7


# In[84]:


data.head(2)


# In[85]:


data[(data["Sun Shine"] > 9) & (data["Cloud3pm"] == 7)]


# In[86]:


#11. mean value of each column against 'Rain Today'
data.head(2)    


# In[90]:


data.groupby('Rain Today').mean()


# In[ ]:


#12. Minimum and maximum value of each column against each "Rain today"


# In[91]:


data.groupby("Rain Today").min()


# In[92]:


data.groupby("Rain Today").max()


# In[93]:


#13. show all records where rain today is yes

data[data["Rain Today"] == "Yes"]


# In[98]:


#14. find all instances where 'rain today is no' or evaporation is 7

data[(data["Rain Today"] == "No") | (data.Evaporation == 7)].tail(50)


# In[ ]:


#15. find all instances when a.Sun shine is greater than 5 and Rain TOday is No .. or b. evaporation is 7.4


# In[99]:


data.head(2)


# In[104]:


data[(data["Rain Today"] == "No") & (data["Sun Shine"] > 5) | (data["Evaporation"] == 7.4)]


# In[ ]:




