'''Given a list of numbers, the task is to write a Python program to find the largest number in given list.

Examples:

Input : list1 = [10, 20, 4]
Output : 20'''

k=[10,20,4,30]
max=20
for i in k:
    if max<i:
        max=i
print(max)     