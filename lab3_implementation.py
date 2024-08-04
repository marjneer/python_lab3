#!/usr/bin/env python
# coding: utf-8

# In[1]:


from smartscan_registration_module import generate_code, fetch_users, RegisterUserFromSmartScan


# In[2]:


generate_code('marita','abc@gmail.com','temp1')
generate_code("glory","xyz@gmail.com",'temp2')


# In[3]:


RegisterUserFromSmartScan('temp1')
RegisterUserFromSmartScan('temp2')


# In[4]:


generate_code("maria" ,"boby,123@gmail.com",'temp3')
RegisterUserFromSmartScan('temp3')


# In[5]:


fetch_users()

