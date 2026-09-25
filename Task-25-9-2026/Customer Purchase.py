'''
6. Customer Purchase History
An e-commerce application stores the product IDs purchased by a customer in 
chronological order. The same product may appear multiple times. The system 
needs to determine the longest sequence of consecutive purchases in which every
 product ID is unique.

'''
product=[1,2,3,2,4,5]
l=0
seen=[]
max_len=0
for r in range(len(product)):
    while product[r] in seen:
        seen.remove(product[l])
        l+=1
    seen.append(product[r])
    if r-l+1>max_len:
        max_len=r-l+1
print("Maximum Length:",max_len)