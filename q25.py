def is_group_member(group_data,n):
    for value in group_data:
        if n==value:
            return True
    return False

print(is_group_member([2,5,7,8,5,3,2,],3))

print(is_group_member([3,5,7,8,9,],2))
