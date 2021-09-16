'''Given a list of numbers, write a Python program to print all positive numbers in given list.

Example:

Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64

Input: list2 = [12, 14, -95, 3]
Output: [12, 14, 3]'''

l=[12, -7, 5, 64, -14]
for i in l:
    if(i>0):
        print(i,end=', ')