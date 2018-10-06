#!/usr/bin/env python
# coding: utf-8

# #                            How to connect with database(sqlite3) in python

# In[9]:


# First import sqlite3 module into the program
import sqlite3 as sql


# ###                       Then using connect() method open database if already exists or create if not.

# In[11]:


db=sql.connect('firstdatabase.db')


# ###                           Create Cursor object so to execute the sqlite queries.

# In[14]:


cursor=db.cursor()
cursor.execute("create table firsttable(ID integer,Name text)")

#Similarly for other queries


# ###                          Now at last don't forget to add commit() command .

# In[15]:


db.commit()


# ###  Go to directary where python library/module is save in the system and check whether database(.db) file create or not... 
