#!/usr/bin/env python
# coding: utf-8

# In[ ]:


test_str = input("Enter a string:")
all_freq = {}
 
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
 
print("Count of all characters  :\n "
      + str(all_freq))


# In[ ]:




