#!/usr/bin/env python
# coding: utf-8

# In[1]:


m1=int(input("enter marks for test:"))
m2=int(input("enter marks for test2"))
m3 = int(input("enter marks for test3"))

if m1<= m2 and m1<=m3:
    avgmarks = (m2+m3)/2
elif m2<=m1 and m2<= m3:
        avgmarks = (m1+m2)/2
elif m3<=m1 and m2<+m2:
      avgmarks = (m1+m2)/2
print("average of best two test marks out of three test's marks is",avgmarks)


# In[ ]:




