#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lst=[]
list_len=int(input("enter the length of the list: "))
for i in range(0, list_len):
 num=int(input("enter the number you want to insert in the list:"))
 lst.append(num)
print(lst)
element=int(input("enter the element: "))
count=0
for i in range(0, len(lst)):
 if (lst[i]==element):
 count+=1
print(element, " occured ", count, " times in the list ", lst)


# In[ ]:




