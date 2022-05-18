#!/usr/bin/env python
# coding: utf-8

# # Guide to `password.py` module

# In[1]:


from randomly.password import generate_password


# To generate a password, enter a length, True/False for if you want to include punctuation, and a list of characters you do not want in the password. 

# In[2]:


password = generate_password(5, True, ['@'])


# In[3]:


password

