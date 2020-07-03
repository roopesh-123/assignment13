#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=input("enter a string=")
d=input("enter a character=")
if(n[0]==d[0]):
    print("starts with specified character")
else:
    print("does not start with specified character")


# In[8]:


n=input("enter a string")
d=input('enter a character')
if(n.startswith(d)):
    print("starts with specified character")
else:
    print("doesn't starts with specified character")

