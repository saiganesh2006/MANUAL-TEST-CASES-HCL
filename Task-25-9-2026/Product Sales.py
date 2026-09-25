'''
5. Product Sales Analysis
A retail company stores the daily sales quantity of a product for several consecutive days. 
Due to seasonal changes, some days may have negative adjustments. The company wants to identify
the period that produced the highest multiplication of sales-related values. Develop a solution to determine this maximum product.

'''
sales=[2,3,-2,4]
ans=sales[0]
for i in range(len(sales)):
    prod=1
    for j in range(i,len(sales)):
        prod*=sales[j]
        if prod>ans:
            ans=prod
print("Maximum Product:",ans)