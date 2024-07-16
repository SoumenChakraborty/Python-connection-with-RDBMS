#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector as sql_db
mydb = sql_db.connect(
       host="localhost",
       user="root",
       password="9239067843")
print(mydb)


# In[3]:


yvar = mydb.cursor()


# In[ ]:





# In[3]:


yvar.execute('show databases')


# In[4]:


for x in yvar:
    print(x)


# In[5]:


yvar.execute('use classicmodels')


# In[6]:


yvar.execute('show tables')


# In[7]:


for x in yvar:
    print(x)


# In[14]:


yvar.execute('select customerName,orderNumber from customers join orders using(customerNumber)')


# In[15]:


for x in yvar:
    print(x)


# In[10]:


yvar.execute('select substr(customerName,1,3) from customers')


# In[11]:


for i in yvar:
    print(i)

