#!/usr/bin/env python
# coding: utf-8

# In[ ]:


temp=int(input("enter the temperature: "))
check=input("cel to fahrenheit?(CF) or fahrenheit to cel(FC)")
if (check=="CF"):
 tempnew=((temp*9)/5)+32
 print(tempnew)
elif (check=="FC"):
 tempnew=((temp-32)*5)/9
 print(tempnew)
else:
 print("not recognized.")


# In[ ]:




