'''a=[1,8,0,3]
siz=len(a)
b=a[0]
a[0]=a[siz-1]
a[siz-1]=b
print(a)   '''



b=[23,65,19,90]  #23 <---> 19   

pos1,pos2=0,2
#q=int(input('enter the positions to swap :  '))
m=b[pos1]
b[pos1]=b[pos2]
b[pos2]=m
print(b)
