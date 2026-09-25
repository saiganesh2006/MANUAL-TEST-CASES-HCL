'''
4. Employee Performance Analysis
A company stores the monthly performance scores of an employee for several months.
The scores may contain both positive and negative values depending on the employee's performance.
Management wants to identify the continuous period during which the employee achieved the highest 
overall performance.

'''
score=[5,-2,3,4,-1]
curr=score[0]
maxi=score[0]
for i in range(1,len(score)):
    if curr+score[i]>score[i]:
        curr+=score[i]
    else:
        curr=score[i]
    if curr>maxi:
        maxi=curr
print("Maximum Overall performance:",maxi)