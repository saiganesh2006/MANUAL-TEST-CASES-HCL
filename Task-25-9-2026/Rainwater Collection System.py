'''
3. Rainwater Collection System
A city installs buildings of different heights along a straight road.
During rainfall, water gets collected between taller buildings.
The engineering team needs to calculate the total amount of water that can remain trapped after heavy rainfall based 
on the heights of the buildings.

'''

hei=[3,0,2,4,0]
l=0
r=len(hei)-1
l_m=0
r_m=0
w=0
while l<r:
    if hei[l]<hei[r]:
        if hei[l]>=l_m:
            l_m=hei[l]
        else:
            w=w+(l_m-hei[l])
        l+=1
    else:
        if hei[r]>=r_m:
            r_m=hei[r]
        else:
            w=w+(r_m-hei[r])
        r-=1
print("Water:",w)
