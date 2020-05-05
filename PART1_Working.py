#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing the data


# In[14]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

searchResults = pd.read_csv('FP_SearchResults.csv')
display(searchResults)


# In[19]:


#Selecting the desired columns


# In[20]:


inputSearch = searchResults[['Title','PublicationDate','Version']]


# In[21]:


display(inputSearch)


# In[33]:


Titles = searchResults[['Title']]


# In[34]:


display(Titles)


# In[42]:


while True:
    titleSearch = input("Enter the name of the policy you are looking for or type 'Quit' to exit: ").title()
    if titleSearch == 'Quit':
        break
    
    if titleSearch in Titles:
        display(searchResults[(searchResults['Title'])]) == titleSearch
        
    else:
        print(f"Sorry, we aren't able to find '{userInput}'.")


# In[43]:


import csv
fields = []
rows = []

with open('FP_SearchResults.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for X in csvreader:
        rows.append(row)
        
    print("Total no. of rows: %d"%(csvreader.line_num))


# In[69]:


import csv
filename = 'FP_SearchResults.csv'
try:
    with open(filename, 'r') as csvfile:
        policy = input("Enter the name of the policy you are looking for or type 'Quit' to exit: ").title()
        print(f"Searching for... {policy}")
        for line in csvfile.readlines():
            if policy in line:
                Title = line.split(',')[0]
                print("Here is what you were looking for: ")
                break
                
        else:
            print(f"Sorry, the Congressional Research Service (CRS) could not find {policy}.")
                
except FileNotFoundError:
    print("Could not find data in file '%s'" % (filename))


# In[80]:


def find_policy(policy):
    df = pd.read_csv(filename)
    congress_data = df.to_records()
    for report in congress_data:
        report_title = report['Title']
        report_pub_date = report['PublicationDate']
        if (report_title.lower() == policy.lower()):
            print('%s was published on %s'%(report_title, report_pub_date))
            break


# In[83]:


while True:
    policy = input("Enter the name of the policy you are looking for or type 'Quit' to exit: ").title()
    if policy == 'quit':
        break
    find_policy(policy)
    break


# In[ ]:




