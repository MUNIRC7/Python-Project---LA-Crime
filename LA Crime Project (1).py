#!/usr/bin/env python
# coding: utf-8

# # Load Data

# In[230]:


import pandas as pd
import matplotlib.pyplot as plt
crime = pd.read_csv('Crime LA/Crime_Data_from_2020_to_Present.csv')


# # Understand and Clean Data

# In[231]:


crime.head()


# In[232]:


crime.columns


# In[233]:


crime.shape


# In[234]:


crime.dtypes


# In[235]:


#Check Nulls
crime.isna().sum()


# In[236]:


df = crime.drop(labels = ['modus_operandi','weapon_code','weapon_description','crime_code_2','crime_code_3',
                          'crime_code_4','cross_street'], axis = 1)
df


# In[237]:


df.sort_values(by = 'date_reported')


# In[238]:


df.dtypes


# In[239]:


#Update Datatypes
df['date_reported'] = pd.to_datetime(df['date_reported'], format = '%Y-%m-%d')
df['date_occurred'] = pd.to_datetime(df['date_occurred'], format = '%Y-%m-%d')


# In[240]:


df.info()


# In[241]:


df.describe(include = ['float64', 'int64'])


# In[242]:


df['victim_age'].value_counts()


# In[243]:


df_age = df[df['victim_age'] > 0]


# In[244]:


df_age['victim_age'].value_counts()


# In[245]:


df['year'] = df['date_occurred'].dt.year
df['month'] = df['date_occurred'].dt.month


# In[246]:


df.sort_values(by = 'date_reported')


# # Feature Understanding

# In[247]:


df['month'].value_counts().sort_index().plot()


# In[248]:


df['year'].value_counts().sort_index().plot(kind='bar')


# In[249]:


df = df[~((df['month'] == 12) & (df['year'] == 2023))]


# In[250]:


df.sort_values(by = 'date_occurred')


# In[251]:


crime_over_time = df.groupby(['year','month']).size().plot()
crime_over_time


# In[252]:


plt.hist(df_age['victim_age'], edgecolor = 'black', bins = 15)


# In[253]:


df['date_occurred_no_time'] = df['date_occurred'].dt.date


# In[254]:


crime_count_per_day = df.groupby(['date_occurred_no_time', 'crime_description']).size()


# In[255]:


top_20_crimes = crime_count_per_day.groupby('crime_description').mean()\
.reset_index(name = 'average_daily_count').sort_values(by = 'average_daily_count', ascending = False).head(20)


# In[256]:


top_20_crimes_sorted = top_20_crimes.sort_values(by = 'average_daily_count', ascending = True)


# In[257]:


plt.barh(top_20_crimes_sorted['crime_description'], top_20_crimes_sorted ['average_daily_count'])


# In[258]:


plt.style.available


# In[259]:


plt.style.use('ggplot')


# In[260]:


plt.figure(figsize = (12, 8))

#Plot 1 - Line Chart
plt.subplot(2,2,1)
crime_plot = df.groupby(['year','month']).size().plot(color = 'green', linewidth = 2)
crime_plot.set_xlabel('Year - Month', fontsize = 10)
crime_plot.set_title('Crime Over Time')


#Plot 2 - Histogram
plt.subplot(2,2,2)
plt.hist(df_age['victim_age'], edgecolor = 'black', bins = 15)
plt.tight_layout()
plt.xlabel('Age', fontsize = 10)
plt.title('Distribution Of Age')

#plot 3 - Horizontal Bar
plt.figure()
plt.barh(top_20_crimes_sorted['crime_description'], top_20_crimes_sorted ['average_daily_count'], color = 'orange')
plt.title('Top 20 Crimes')


# In[261]:


#Show difference in reported and occurred - How long it takes to report?
df['Time to report'] = (pd.to_datetime(df['date_reported']) - pd.to_datetime(df['date_occurred_no_time'])).dt.days


# In[262]:


df


# In[263]:


df['Time to report'].value_counts().head(10)


# In[264]:


df.groupby(['crime_description'])['Time to report'].mean().sort_values().head(10)


# In[265]:


#Identify the top 3 crimes with the highest average victim age


# In[266]:


df_age.groupby('crime_description')['victim_age'].mean().reset_index().sort_values(by = 'victim_age', ascending = False).head(3)


# In[ ]:





# In[ ]:





# In[ ]:





# In[325]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




