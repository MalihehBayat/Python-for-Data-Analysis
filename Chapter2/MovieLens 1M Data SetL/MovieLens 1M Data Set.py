#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[36]:


unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::', header=None, names=unames, engine='python')


# In[10]:


rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, names=rnames, engine='python')


# In[15]:


mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names= mnames, engine='python', encoding="ISO-8859-1")


# In[17]:


users.head(5)


# Occupation is chosen from the following choices:
# 
# | Number     | Description |
# | -----------| ----------- |
# | 0     | "other" or not specified       |
# | 1  | "academic/educator"        |
# |2 | "artist"|
# |3| "clerical/admin"|
# |4| "college/grad student"|
# |5|"customer service"|
# |6| "doctor/health care"|
# |7| "executive/managerial"|
# |8|"farmer"|
# |9| "homemaker"|
# |10|"K-12 student"|
# |11|"lawyer"|
# |12|"programmer"|
# |13|"retired"|
# |14|"sales/marketing"|
# |15|"scientist"|
# |16| "self-employed"|
# |17|"technician/engineer"|
# |18|"tradesman/craftsman"|
# |19|"unemployed"|
# |20|"writer"|
# 

# In[22]:


occupation={0:"other or not specified",  1:"academic/educator", 2:"artist",  3:"clerical/admin", 4:"college/grad student",  5:"customer service",
 6:"doctor/health care", 7:"executive/managerial" , 8: "farmer", 9: "homemaker",10:  "K-12 student", 11:  "lawyer", 12:  "programmer", 13:  "retired",
 14:  "sales/marketing", 15:  "scientist", 16:  "self-employed", 17:  "technician/engineer",18:  "tradesman/craftsman", 19:  "unemployed",20:  "writer"}


# In[37]:


users["occupation title"]=users.occupation.map(occupation)


# Age is chosen from the following ranges:
# 
# |Number| Age Range|
# |------|-----|
# |1| Under 18|
# |18|18-24|
# |25|25-34|
# |35|35-44|
# |45|45-49|
# |50|50-55|
# |56|56+|
# 
# 
# 

# In[40]:


Ages= {1:  "Under 18", 18:  "18-24", 25:  "25-34", 35:  "35-44", 45:  "45-49", 50:  "50-55", 56:  "56+"}


# In[41]:


users["Age range"]=users.age.replace(Ages)


# In[42]:


users.head()


# In[44]:


users.info()


# In[18]:


ratings.head(5)


# In[46]:


ratings.rating.unique()


# In[47]:


movies.head()


# In[48]:


data = pd.merge(pd.merge(ratings, users), movies)


# In[49]:


data.head()


# In[151]:


mean_ratings = data.pivot_table('rating', index='title', columns='gender',aggfunc='mean')
#mean_ratings.reset_index(inplace=True)
mean_ratings.columns=["Female Users", "Male Users"]


#mean_ratings.set_index('title')
#mean_ratings


# ## Analysing the Most Frequently rated Movies

# In order to analyse the most frequently watched (rated) movies, the data is filtered down to movies that received at least 250 ratings (a completely arbitrary number)

# In[152]:


ratings_by_title = data.groupby('title').size()


# In[153]:


ratings_by_title[:10]


# In[154]:


active_titles = ratings_by_title.index[ratings_by_title >= 250]


# In[130]:


type(active_titles)


# In[155]:


mean_ratings = mean_ratings[mean_ratings.index.isin(active_titles)]


# In[161]:


mean_ratings.sort_values(by=["Female Users","Male Users"], ascending=False).head(10)


# In[157]:


mean_ratings.sort_values(by=["Male Users"], ascending=False).head(10)


# In[158]:


mean_ratings.sort_values(by=["Female Users"], ascending=False).head(10)


# In[166]:


mean_ratings.plot.scatter(x='Female Users', y='Male Users', s=20)
    #x = 'Name', y = 'Age', s = 100);)


# ## Measuring rating disagreement

# In[171]:


mean_ratings['diff'] = mean_ratings['Male Users'] - mean_ratings['Female Users']
mean_ratings['absdiff']=abs(mean_ratings['Male Users'] - mean_ratings['Female Users'])


# In[174]:


mean_ratings.sort_values(by=['absdiff'], ascending=False).head()


# In[ ]:




