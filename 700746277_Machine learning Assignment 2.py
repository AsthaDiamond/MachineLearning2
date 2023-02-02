#!/usr/bin/env python
# coding: utf-8

# In[6]:


#question 1
for i in range(1,6):
    print("*"*i)
for j in range(4,0,-1):
    print("*"*j)


# In[7]:


#question 2
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("the list is :")
print(my_list)
print("the elements in odd indexes are :")
for i in range(1, len(my_list), 2):
    print(my_list[i])


# In[3]:


#question 3
x=[23,'Python',23.98]
print(x)
type_list=[]
for i in x:
    type_list.append(type(i))
print(type_list)


# In[4]:


#question 4
sample_list =  [1,2,3,3,3,3,4,5]
unique_list  = (set(sample_list))
print(unique_list)


# In[5]:


#question 5
s=input("Enter your string: ")
lower=0
upper=0
for i in s:
    if(i.islower()):
        lower=lower+1
    elif(i.isupper()):
            upper=upper+1
print("The number of upper case characters:")    
print(upper)
print("The number of lower case characters: ")
print(lower)
            


# In[ ]:




