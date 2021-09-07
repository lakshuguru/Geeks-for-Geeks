'''Given a list of numbers, the task is to write a Python program to find the second largest number in the given list.
Examples: 

Input: list1 = [10, 20, 4]
Output: 10

Input: list2 = [70, 11, 20, 4, 100]
Output: 70'''

l=[70,11,20,4,100]
for i in range(len(l)):
    for j in range(len(l)):
        if j<4:
            if l[j]<l[j+1]:
                k=l[j]
                l[j]=l[j+1]
                l[j+1]=k
print(l[1])        

'''def findLargest(arr):
    secondLargest = arr[0]
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
 
    for i in range(len(arr)):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
 
    return secondLargest
 
 
print(findLargest([10, 20, 4, 99]))'''

'''l=[10,20,4,15,17]
lst=[]
max=0
for i in l:
    if max<i:
        max=i
        a=max
        l.remove(max)
for j in l:
    if max<j:
        max=j
        b=max

if a<b:
    print(a)
if b<a:
    print(b)'''

