def subsring_copy(str,n):
    flen = 2
    if flen>len(str):
        flen=len(str)
    substr=str[:flen]

    result=""
    for i in range(n):
        result=result+substr
    return result

print(subsring_copy("asdf",5))
print(subsring_copy("jk",6))
