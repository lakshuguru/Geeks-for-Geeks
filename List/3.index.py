n=int(input())
k=[]
for i in range(n):
    p=int(input())
    k.append(p)
    #print(k)
print(k)    
for i in range(1,n+1):    
    if i==k[i-1]:
        print("\nans: ",k[i-1])
    