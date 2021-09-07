'''The problem of finding the summation of digits of numbers is quite common. 
This can sometimes come in form of a list and we need to perform that. 
This has application in many domains such as school programming and web development. 
Let’s discuss certain ways in which this problem can be solved.'''



l=[12,67,98,34]
for i in l:
    l=i%10+i//10 
    print(l)     
        