'''
2. Online Shopping Price Analysis
An online shopping application stores the prices of products viewed by a customer during
a browsing session. The customer wants to identify a continuous range of products that provides 
the maximum possible total discount value. Given the discount values, determine the maximum value 
that can be obtained from any continuous range.

'''

dis=[2, -1, 4, -2, 5, -3]
sumi=0
maxi=0
for i in range(len(dis)):
    sumi+=dis[i]
    if sumi<0:
        sumi=0
    maxi=max(sumi,maxi)
print("Maximum:",maxi)