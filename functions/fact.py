#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. 
'''
def fact(x):
    y=1
    for i in range(1,x+1):
        y=y*i
    print(y)
fact(5) '''   

#doubt(renu)
n=int(input("Enter upto :"))
def fact():
    i=1
    f=1
    while i<=n:
        if i!=0:
            f=f*i
        i+=1
        
    print(f)
fact()