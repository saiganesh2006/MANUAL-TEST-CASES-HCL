'''
7. Bank Transaction Analysis
A bank stores transaction amounts for a customer's account. A continuous group 
of transactions may add up to a specific target amount. The auditing system needs
to determine how many different continuous transaction groups produce exactly the
specified amount.

'''
trans=[1,2,3,2,1]
tar=3

cnt=0
for i in range(len(trans)):
    total=0
    for j in range(i,len(trans)):
        total+=trans[j]
        if total==tar:
            cnt+=1
print("Count:",cnt)