'''Given starting and end points, write a Python program to print all even numbers in that given range.

Example:

Input: start = 4, end = 15
Output: 4, 6, 8, 10, 12, 14

Input: start = 8, end = 11
Output: 8, 10'''

l=int(input('enter the starting num :'))
k=int(input('enter the ending number : '))
for i in range(l,k+1):
    if(i%2==0):
        print(i,end=',')
        
