#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lst=[]
list_len=int(input("enter the length of the list: "))
for i in range(0, list_len):
 num=int(input("enter the number you want to insert in the list:"))
 lst.append(num)
print(lst)
MIN=lst[0]
for i in range(0, len(lst)):
 if MIN>lst[i]:
 MIN=lst[i]
print(MIN)
print("The minimum value in list ", lst, " is ", MIN)
MAX=lst[0]
for i in range(0, len(lst)):
 if MAX<lst[i]:
 MAX=lst[i]
print("The maximum value in the list ", lst, " is ", MAX)


# In[ ]:




