#!/usr/bin/env python
# coding: utf-8

# In[202]:
import pandas as pd 
import numpy as np
data= pd.read_csv("C:\\Users\\Srinivas\\Downloads\\dataset - netflix1.csv")
# In[203]:
print(data.head())

# In[204]:
print(data.tail())

# In[205]:
# Assuming 'Not Given' is a string in your data
data.loc[data['director'] == 'Not Given', 'director'] = pd.NA

# In[206]:
# Assuming 'Not Given' is a string in your data
data.loc[data['country'] == 'Not Given', 'director'] = pd.NA
data.head()

# In[207]:
print(data.isnull().any())

# In[208]:
data.sort_values(by='show_id', ascending=True, inplace=True)
data.head()

# In[209]:
#info of data
data.info()

# In[210]:
#checking for missing value 
data.isna().any()

# In[211]:
#drop missing values 
data.dropna(inplace=True)

# In[212]:
#checking to see,have dropped the missing values
data.isna().any().sum()

# In[213]:
data.duplicated().any()

# In[214]:
data.shape

# In[215]:
data.size

# In[216]:
data.columns

# In[217]:
data.dtypes

# In[218]:
#finding a duplicate value and remove duplicate values 
data[data.duplicated()]
#no duplicates values found after executing

# In[219]:
#data.drop_duplicates(inplace=True)

# In[220]:
data.shape

# In[221]:
#null values 
data.isnull()

# In[222]:
data.isnull().sum()
#no null value 

# In[223]:

import seaborn as sns 
sns.heatmap(data.isnull())

# In[225]:
#show id and who is director of the show 
data[data['title'].isin(['Midnight Mass'])]

# In[226]:
data[data['title'].str.contains('Midnight Mass')]

# In[227]:
#year with highest number of the TV shows &Shows were realeased using bar grapgh
data.dtypes

# In[228]:
data['release_year'] = data['release_year'].astype(str)

# In[229]:
data.dtypes

# In[230]:
data['DATA_NEW'] = pd.to_datetime(data['date_added'])

# In[231]:
data.head()

# In[232]:
data.dtypes

# In[233]:
data['DATA_NEW'].dt.year.value_counts()

# In[234]:
#how many movies and tv shows in dataset
data.head(2)

# In[235]:
data.groupby('type').listed_in.count()

# In[236]:
#movies released on year 2016
data['DATA_YEAR']=data['DATA_NEW'].dt.year

# In[237]:
data.head(2)

# In[238]:
data[(data['type']=='Movie') & (data['DATA_YEAR']==2017)]

# In[239]:
#TV Shows released in UNITED STATES 
data[(data['type']=='TV Show') & (data['country']=='United States')]

# In[240]:
#TV Shows released in UNITED STATES only title
data[(data['type']=='TV Show') & (data['country']=='United States')] ['title']

# In[241]:
#top 10 ditrector who gave the highest number of movies and tv shows in the dataset
data['director'].value_counts().head(10)

# In[242]:
#show all the records , where type is movie and listed_in Dramas or country is INDIA 
data[(data['type']=='Movie')& (data['listed_in']=='Dramas')]

# In[243]:
data[(data['type']=='Movie')& (data['listed_in']=='Dramas') | (data['country']=='India')]

# In[244]:
#different ratings defined by the netflix
data['rating'].nunique()

# In[245]:
data['rating'].unique()

# In[246]:
#how many movies got TV-14 rating in Canada
data[(data['type']=='Movie')& (data['rating']=='TV-14')]

# In[247]:
data[(data['type']=='Movie')& (data['rating']=='TV-14')&(data['country']=='Canada')]

# In[248]:
#How many Movies got rating R after 2005
data[(data['type']=='Movie')&(data['rating']=='R')]

# In[249]:
data[(data['type']=='Movie')&(data['rating']=='R')& (data['DATA_YEAR'] > 2005)].shape

# In[250]:
data[(data['type']=='Movie')&(data['rating']=='R')& (data['DATA_YEAR'] > 2005)]

# In[251]:
#maximum duration of a movie/show on netflix
data['duration'].nunique()

# In[252]:
data['duration'].unique()
data.duration.dtypes

# In[254]:
#str.split
data[['Minutes','Unit']]=data['duration'].str.split(' ',expand=True)

# In[255]:
data.head()

# In[256]:
data['Minutes'].max()

# In[257]:
data['Minutes'].min()

# In[258]:
data.dtypes

# In[259]:
#which individual country has the highest no.TV Show ???
data_tvshows=data[data['type']=='TV Show']

# In[260]:
data_tvshows.head(5)

# In[261]:
data_tvshows.country.value_counts().head(5)

# In[262]:
#how can we sort the dataset my YEAR??
data.sort_values(by='DATA_YEAR',ascending=False).head()

# In[263]:
import pandas as pd 
import numpy as np

# Read the dataset
data = pd.read_csv("C:\\Users\\Srinivas\\Downloads\\dataset - netflix1.csv")

# Check the column names to find the right column to use
print(data.columns)

# Let's consider 'viewership_count' as the column of interest
column_of_interest = 'release_year'

# Calculate the z-score for the column
z_scores = np.abs((data[column_of_interest] - data[column_of_interest].mean()) / data[column_of_interest].std())

# Define a threshold (e.g., z-score greater than 3 is considered an outlier)
threshold = 3

# Find the outliers based on the threshold
outliers = data[z_scores > threshold]

print("Outliers based on z-score:")
print(outliers)


