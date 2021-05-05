def list_count_4(nums):
    count=0
    for num in nums:
        if num==4:
            count=count+1

    return count

print(list_count_4([4,7,8,4,9,3,4,1,4,8,4,6,4,3,4]))