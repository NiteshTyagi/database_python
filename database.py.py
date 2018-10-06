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

''' for insert data into the table ,there are 2 ways:
1.? placeholder
2.using python tuple  and  keyname placeholder'''

id1=1
Name1="Nitesh"

id2=2
Name2="Tyagi"

cursor.execute("insert into firsttable(ID,Name) values(?,?)",(id1,Name1)) #By using ? placeholder

cursor.execute('insert into firsttable(ID,Name) values(:id,:Name)',{'id':id2,'Name':Name2})


# ###                          Now at last don't forget to add commit() command .

# In[15]:


db.commit()


# ###  Go to directary where python library/module is save in the system and check whether database(.db) file create or not... 
