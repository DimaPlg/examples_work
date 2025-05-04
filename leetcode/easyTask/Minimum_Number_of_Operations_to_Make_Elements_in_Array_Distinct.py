def minimumOperations(nums):
    length = len(nums)
    num_rev = [nums[i] for i in range(-1, -length -1, -1)]
    count = 0
    nums_dict = {}
    for i in num_rev:
        count += 1
        if nums_dict.get(i) == 1:
            count -=1
            break
        elif not nums_dict.get(i):
            nums_dict[i] = 1
    if (length - count) % 3 != 0:
        return int((length - count) // 3) + 1
    return int((length - count)//3)




#[1,2,3,4,2,3,3,5,7]
print(minimumOperations([4,5,6,4,4]))