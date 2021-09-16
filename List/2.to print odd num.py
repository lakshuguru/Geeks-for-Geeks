'''Given a list of numbers, write a Python program to print all odd numbers in given list.

Example:

Input: list1 = [2, 7, 5, 64, 14]
Output: [7, 5]

Input: list2 = [12, 14, 95, 3, 73]
Output: [95, 3, 73]'''

l=[10,33,65,22,74,38,35,14]
p=[]
for i in l:
    if(i%2!=0):
        p.append(i)
print(p)    
