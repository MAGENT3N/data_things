# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:39:58 2026

@author: arjun and yash
"""

# group = {"france": 0 ,"germany" : 0 , "brazil" : 0 ,"argentina": 0}
# for key,values in group.items():
#     if group[key]:
        
teams = ["france","germany","brazil","argentina"]
pairs = []
for i in range(len(teams)):
    for j in range(i + 1 , len(teams)):
        if i != j :
            pair = (teams[i],teams[j])
            pairs.append(pair)
print(pairs)
            

    
