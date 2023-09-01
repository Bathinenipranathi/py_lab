#!/usr/bin/env python
# coding: utf-8

# In[7]:
import re
def isphonenumber(numStr):
    if len(numStr)!=12:
        return False
    for i in range(len(numStr)):
        if i==3 or i==7:
            if numStr[i]!="-":
                return False
        else:
            if numStr[i].isdigit()==False:
                return False
        return True
def chkphonenumber(numStr):
     ph_no_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
     if ph_no_pattern.match(numStr):
        return True
     else:
        return False
ph_num = input("Enter a phone number : ")
print("Without using Regular Expression")
if isphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
print("Using Regular Expression")
if chkphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
        



# In[ ]:
import os.path
import sys
fname = input("Enter the filename : ") 
if not os.path.isfile(fname):
 print("File", fname, "doesn't exists")
 sys.exit(0)
infile = open(fname, "r")
lineList = infile.readlines()
for i in range(20):
 print(i+1, ":", lineList[i])
 
word = input("Enter a word : ")
cnt = 0
for line in lineList:
 cnt += line.count(word)
print("The word", word, "appears", cnt, "times in the file")




