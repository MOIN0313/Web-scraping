#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
#Requests — A Python library used to send an HTTP request to a website and store the response object within a variable. 
#BeautifulSoup — A Python library used to extract the data from an HTML or XML document


# In[2]:


link="https://www.amazon.in/Test-Exclusive_2020_1181-Multi-3GB-Storage/product-reviews/B089MSK447?reviewerType=all_reviews"


# In[3]:


page=requests.get(link)


# In[4]:


page


# In[5]:


page.content


# In[6]:


soup=bs(page.content,"html.parser")
soup


# In[7]:


print(soup.prettify())# to format in rightway


# In[8]:


names=soup.find_all('span',class_="a-profile-name") # span = name of tag
names


# In[9]:


cust_names=[]
for i in names:
    cust_names.append(i.text.strip())


# In[10]:


cust_names


# In[11]:


cust_names.pop(0)


# In[12]:


cust_names.pop(0)


# In[13]:


cust_names


# In[14]:


title=soup.find_all("a",class_="review-title-content")
title


# In[15]:


review_title=[]
for i in title:
    review_title.append(i.text.strip())

review_title


# In[16]:


rating=soup.find_all("i",class_="review-rating")
rating


# In[17]:


ratings=[]
for i in rating:
    ratings.append(i.text.strip())
ratings    


# In[18]:


ratings.pop(0)


# In[19]:


ratings.pop(0)


# In[20]:


ratings


# In[21]:


review_content=soup.find_all("div",class_="a-row a-spacing-small review-data")
review_content


# In[22]:


review_comments=[]
for i in review_content:
    review_comments.append(i.text.strip())
review_comments 


# In[23]:


len(review_comments)


# In[24]:


cust_names


# In[25]:


ratings


# In[26]:


review_title


# In[27]:


review_comments


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # to save data in csv file

# In[28]:


import pandas as pd


# In[29]:


df=pd.DataFrame()


# In[30]:


df['customer_name']=cust_names
df


# In[31]:


df['review_title']=review_title
df['rate']=ratings
df['review_content']=review_comments
df


# # END !

# In[ ]:




