#!/usr/bin/env python
# coding: utf-8

# In[5]:


#install ibm_watson and ibm_cloud_sdk_core using PIP
from ibm_watson import LanguageTranslatorV3 as LTV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[28]:


#Get your own API url and key https://cloud.ibm.com/catalog/services
url = "API URL goes here!"
key = IAMAuthenticator("Get_your_key")


# In[29]:


LT = LTV3(version="2018-05-01",authenticator= key)
LT.set_service_url(url)


# In[34]:


mytext = "Hello World! how are you?"


# In[38]:


resp = LT.translate(text = mytext, model_id= 'en-hi').get_result()
resp['translations'][0]['translation']


# In[ ]:




