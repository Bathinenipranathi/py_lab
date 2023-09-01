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
import re
# Define the regular expression for phone numbers
phone_regex = re.compile(r'\+\d{12}')
email_regex = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')
# Open the file for reading
with open('untitled1.txt', 'r') as f:
 
   for line in f:

        matches = phone_regex.findall(line)

        for match in matches:
            print(match)
        matches = email_regex.findall(line)
 
        for match in matches:
            print(match)




