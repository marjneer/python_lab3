#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Library
import qrcode
import cv2


# In[2]:


def generate_code(name,email,file_name):
    data=name+","+email
    img=qrcode.make(data)
    img.save(f'{file_name}.png')


# In[9]:


users=[]
new_user= lambda name, email: {'name': name, 'email': email}
insert_user= lambda new: users.append(new)
fetch_users= lambda : users


# In[10]:


def RegisterUserFromSmartScan(file_name):
    img=cv2.imread(f'{file_name}.png')
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)    
    us_email=val.split(',')
    if (len(us_email)==2):
        new=new_user(us_email[0],us_email[1])
        insert_user(new)
        return fetch_users()
    else:
        return "Invalid code"

