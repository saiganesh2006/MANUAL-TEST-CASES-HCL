'''1. Student Attendance Analysis
A college maintains the daily attendance details of its students in the form of a list containing student IDs. Some students may have attended multiple sessions on the same day. The administration wants to identify the longest continuous sequence of sessions in which no student ID is repeated. Develop a solution that determines the maximum length of such a sequence.
'''
ids=[1,2,4,2,1,3]
seen=[]
left=0
maxLen=0
for right in range(len(ids)):
    while ids[right] in seen:
        seen.remove(ids[right])
        left+=1
    seen.append(ids[right])
    if right-left+1 > maxLen:
        maxLen=right-left+1
print("Maximum Length:",maxLen)


