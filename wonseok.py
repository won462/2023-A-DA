#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [10,20,30,40],color="r",linestyle="--", label="dashed")
plt.plot([1,2,3,4], [40,30,20,10],color="b",ls=":",label="dotted")
plt.title("linestyle")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()


# In[10]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [10,20,30,40],color="r",linestyle="--",marker ="d", label="diamond")
plt.plot([1,2,3,4], [40,30,20,10],color="b",ls=":",marker="^",label="triangle up")
plt.title("marker")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()


# In[11]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [10,20,30,40],color="r",linestyle="--",marker ="d",linewidth=3, label="diamond")
plt.plot([1,2,3,4], [40,30,20,10],color="b",ls=":",linewidth=0.5,marker="^",label="thin line")
plt.title("marker")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()


# In[12]:


import matplotlib.pyplot as plt
plt.plot([-2,-1,0,1,2,3], [20,30,15,40,45,35],label="선1")
plt.plot([-2,-1,0,1,2,3], [25,10,35,20,15,25],label="선2")
plt.title("선 그래프")
plt.xlabel("x 축")
plt.ylabel("y 축")
plt.legend()
plt.show()


# In[13]:


import matplotlib.pyplot as plt

plt.rc("font,family="Malgun Gothic")
plt.tittle("선 그래프 예제")
       


# In[14]:


import numpy as np

x= np.arange(-10,10,0.1)
plt.plot(x,x**2)

plt.xticks(np.arange(-10,11,2))
plt.yticks(np.arange(0,101,20))
plt.rc("font",family="Malgun Gothic")
plt.tittle("선 그래프 예제")
       


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

N=8
y= np.zeros(N)

x1=nplinspace(0,10,N,endpoint=true)
x2=nplinspace(0,10,N,endpoint=false)

plt.legend()
plt.ylim([-0.5,1])
plt.show()

