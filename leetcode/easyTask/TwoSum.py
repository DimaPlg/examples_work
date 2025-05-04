def twoSum(nums, target):
    # contr_list = [target] * len(nums)
    # for i in range(len(nums)):
    #     if nums[i] in contr_list and i != contr_list.index(nums[i]):
    #         return [contr_list.index(nums[i]), i]
    #     contr_list[i] -= nums[i]
    # return []
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    return []

print(twoSum([0,4,3,0], 0))