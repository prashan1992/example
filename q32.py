def sum(x,y,z):
    if x==y or y==z or z==x:
        sum=0
    else:
        sum=x+y+z
    return sum


print(sum(2,6,7))
print(sum(3,3,5))
print(sum(2,6,9))