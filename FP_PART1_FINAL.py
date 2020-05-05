#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Importing the data


# In[30]:


import pandas as pd
import numpy as np
import csv
import warnings
warnings.filterwarnings('ignore')

searchResults = pd.read_csv('FP_SearchResults.csv')


# In[31]:


#Creating a function to select the titles of policy documentation


# In[32]:


filename = 'FP_SearchResults.csv'

def find_policy(policy):
    df = pd.read_csv(filename)
    congress_data = df.to_records()
    for report in congress_data:
        report_title = report['Title']
        report_pub_date = report['PublicationDate']
        if (report_title.lower() == policy.lower()):
            print('%s was published on %s'%(report_title, report_pub_date))
            break


# In[33]:


#Calling the function and incorporating user input


# In[34]:


try:
    while True:
        policy = input("Enter the name of the policy you are looking for: ").title()
        print("Searching...")
        find_policy(policy)
        break
except FileNotFoundError:
    print("Could not find data in file '%s'" % (filename))

