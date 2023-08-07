#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1 = pd.read_csv("C:\\Users\\suraj\\Downloads\\tmdb_5000_movies.csv\\tmdb_5000_movies.csv")


# In[3]:


df2 = pd.read_csv("C:\\Users\\suraj\\Downloads\\tmdb_5000_credits.csv\\tmdb_5000_credits.csv")


# In[4]:


df1.head()


# In[5]:


df2.head()


# In[6]:


df2.rename(columns = {
    'movie_id':'id'
},inplace=True)


# In[7]:


df = pd.merge(df1,df2,on='id')


# In[8]:


df.head()


# In[9]:


data = df['genres'][0]


# In[10]:


data


# In[11]:


import json


# In[12]:


parse_data = json.loads(data)


# In[13]:


parse_data


# In[14]:


result = [item['name'] for item in parse_data]


# In[15]:


result2 = " ".join(result)


# In[16]:


result2


# In[17]:


def extract_genres(data):
    parse_data = json.loads(data)
    result = [item['name'] for item in parse_data]
    result2 = " ".join(result)
    return result2

    


# In[18]:


df['genres']=df['genres'].apply(extract_genres)


# In[19]:


df['genres']


# In[20]:


df['keywords']=df['keywords'].apply(extract_genres)


# In[21]:


df['keywords'][0]


# In[22]:


df.info()


# In[23]:


df['spoken_languages']=df['spoken_languages'].apply(extract_genres)


# In[24]:


df['title_y']


# In[25]:


columns_to_drop= ['homepage','original_title','overview','popularity','production_companies','production_countries','release_date','revenue','runtime','status','tagline','title_x','vote_average','vote_count','title_y']


# In[26]:


df.info()


# In[27]:


df.drop(columns=columns_to_drop,inplace=True)


# In[ ]:





# In[29]:


df


# In[ ]:





# In[30]:


import pandas as pd


# In[31]:


df['cast']=df['cast'].str.lower()


# In[32]:


df['cast'][0]


# In[33]:


data=json.loads(df['cast'][0])


# In[34]:


''.join(data[0]['name'].split())


# In[35]:


a=5
name =[]
for item in data:
    if(a):
        name.append(''.join(item['name'].split()))
        a=a-1
    else:
        break
print(' '.join(name))


# In[36]:


data


# In[37]:


data[0]['name']


# In[38]:


def extract_names(data):
    a = 5
    name = []
    parse_data = json.loads(data)
    for item in parse_data:
        if a:
            name.append(''.join(item['name'].split()))
            a = a - 1
        else:
            break      
    return ' '.join(name)


# In[39]:


df['name']= df['cast'].apply(extract_names)


# In[40]:


df['name'][0]


# In[41]:


df.drop(columns=['cast'],inplace=True)


# In[42]:


data2 = json.loads(df['crew'][1])


# In[43]:


data2


# 

# In[48]:


def director_(data):
    parsedata = json.loads(data)
    name=''
    for items in parsedata:
        if items['job']=='Director':
            name = items['name']
            break
    return name


# In[47]:


json.loads(df['crew'][0])


# In[49]:


df['director']=df['crew'].apply(director_)


# In[122]:


df['director'].str.lower()


# In[137]:


def join_name(data):
    result = ''.join(data.lower().split())
    return result


# In[138]:


join_name('James Cameron')


# In[139]:


df['director']=df['director'].apply(join_name)


# In[140]:


df['director']


# In[51]:


df.rename(columns={
    'name':'actors'
},inplace=True)


# In[52]:


df.head()


# In[53]:


df.drop(columns=['budget','crew'],inplace=True)


# In[54]:


df.head()


# In[55]:


df2.info()


# In[56]:


df['title']=df2['title']


# In[141]:


df.head()


# In[101]:


df['keywords'].shape


# In[104]:


import numpy as np


# In[105]:


a = np.array([' ']*4803)


# In[117]:


space_df=pd.DataFrame(a)


# In[118]:


df['genres']+space_df[0]+df['keywords']


# In[142]:


df['tags']=df['genres']+space_df[0]+df['keywords']+space_df[0]+df['actors']+space_df[0]+df['director']


# In[143]:


df['tags'][0]


# In[144]:


df.head()


# In[68]:


df.describe()


# In[145]:


df['tags'][0]


# In[83]:


get_ipython().system('pip install nltk')


# In[95]:


import nltk


# In[154]:


from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


# In[157]:


def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return ' '.join(y)


# In[159]:


stem('Hello Brothe How Are you')


# In[162]:


df['tags']=df['tags'].apply(stem)


# In[163]:


df['tags']


# In[166]:


from sklearn.feature_extraction.text import CountVectorizer


# In[167]:


cv = CountVectorizer(max_features=5000,stop_words='english')


# In[168]:


vector=cv.fit_transform(df['tags']).toarray()


# In[169]:


vector


# In[170]:


data9=pd.DataFrame(cv.get_feature_names_out())


# In[171]:


data9.sample(5)


# In[172]:


from sklearn.metrics.pairwise import cosine_similarity


# In[173]:


cosine_similarity(vector)


# In[175]:


similarity=cosine_similarity(vector)


# In[245]:


similarity


# In[181]:


df['title']


# In[188]:


df[df['title']=='Avatar'].index[0]


# In[213]:


df.iloc[2403,7]


# In[192]:


distances=similarity[0]


# In[225]:


sorted_array=sorted(enumerate(distances),key=lambda x:x[1],reverse=True)
for item in sorted_array[1:6]:
    df.iloc[item[0],7]


# In[195]:


for index,dist in enumerate(distances):
    


# In[217]:


movie ='Avatar'
movie.lower()


# In[221]:


df['title'].str.lower()


# In[230]:


def recomend_movie(movie):
    movie = movie.lower()
    rec_movies=[]
    movie_index = df[df['title'].str.lower()==movie].index[0]
    distances = similarity[movie_index]
    sorted_array=sorted(enumerate(distances),key=lambda x:x[1],reverse=True)
    for item in sorted_array[1:6]:
        rec_movies.append(df.iloc[item[0],7])
    return rec_movies


# In[236]:


recomend_movie('spectre')


# In[237]:


import pickle


# In[238]:


pickle.dump(df,open('movies.pkl','wb'))


# In[244]:


np.array(df['title'].values)


# In[246]:


pickle.dump(similarity,open('similarity.pkl','wb'))


# In[250]:


import requests
from PIL import Image
from io import BytesIO


# In[251]:


def get_movie_poster(movie_title):
    api_key = 'd84abdce4b7b8a069bdb83d14a36aff7'
    base_url = 'https://api.themoviedb.org/3/search/movie'
    params = {'api_key': api_key, 'query': movie_title}

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['results']:
        poster_path = data['results'][0]['poster_path']
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return poster_url
    else:
        return None


# In[252]:


get_movie_poster('Avatar')

