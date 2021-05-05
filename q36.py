def add_numbers(a,b):
    if not (isinstance(a,int) and isinstance(b,int)):
        raise TypeError("Inputs must be integers")
    return a+b

print(add_numbers(2.3,2))
print(add_numbers(3,4))