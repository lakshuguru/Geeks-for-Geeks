'''The problem of finding the summation of digits of numbers is quite common. This can sometimes come in form of a list and we need to perform that. This has application in many domains such as school programming and web development. 
Let’s discuss certain ways in which this problem can be solved.'''


l=[4,2,3]
k=1
for i in range(len(l)):
        #k*=l[i]*l[i+1]
        k*=i
print(k)

    