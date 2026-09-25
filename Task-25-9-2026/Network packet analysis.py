'''
9. Network Packet Analysis
A network monitoring system receives packet identifiers in chronological order.
The system must determine the longest sequence of consecutive packets whose 
identifiers form a continuous numerical sequence, regardless of their original
order in the incoming data.

'''
packets=[100,4,200,1,3,2]
packets=sorted(set(packets))
count=1
max_count=1
for i in range(1,len(packets)):
    if packets[i]==packets[i-1]+1:
        count+=1
    else:
        count=1
    if count>max_count:
        max_count=count
print("Longest Sequence:",max_count)