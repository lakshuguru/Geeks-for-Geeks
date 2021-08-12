#Write a Python function to find the Max of three numbers.

def max(x,y,z):
    #evaluating for x
    if x>y and x>z:
        print(f'{x} is greater')
    #eval for y
    elif y>x and y>z:
        print(f'{y} is greater')
    #eval for z  
    else:
        print(f'{z} is greater')

max(12,45,77)              