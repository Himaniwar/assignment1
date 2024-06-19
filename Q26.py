#!/usr/bin/env python
# coding: utf-8

# In[ ]:


str=input("enter the prefix or sufux: ")
word=input("enter the word: ")
if (word.startswith(str)):
 print(str, "is the prefix of ", word)
elif (word.endswith(str)):
 print(str, "is the suffix of", word)


# In[ ]:




