def histogram(items):
    for n in items:
        output=""
        times=n
        while(times>0):
            output+="*"
            times=times-1
        print(output)


histogram([2,3,4,5])
histogram([7,6,1,2,3])