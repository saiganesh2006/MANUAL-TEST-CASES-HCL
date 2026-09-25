'''
8. Employee Skill Grouping
A company receives a list of employee skill codes represented as strings. 
Employees having the same set of characters in their skill codes belong to the
same skill category, even if the characters appear in a different order. 
The HR system needs to organize employees into appropriate skill groups

'''
skills=["eat","tea","tan","ate","nat","bat"]
groups={}
for word in skills:
    key="".join(sorted(word))
    if key not in groups:
        groups[key]=[]
    groups[key].append(word)
print(list(groups.values()))