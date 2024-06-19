#!/usr/bin/env python
# coding: utf-8

# In[24]:


a=int(input("enter a number:"))
x=0
y=1
print(x)
print(y)
for i in range(0,a-2):
      print(x+y)
      temp=x
      x=y
      y=temp+y
      


# In[ ]:




