from itertools import groupby
from operator import not_
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        num_null = 0
        const_val = 0
        value_list = []
        for i in nums:
            if i == 0:
                num_null+=1
                const_val = 0
            elif i != const_val:
                value_list.append(i)
                const_val = i
            elif i == const_val:
                value_list[-1] *= 2
                const_val = 0
                num_null += 1
        return value_list + [0]*num_null

    def applyOperations2(self, nums: List[int]) -> List[int]:
        return sorted(sum(((l := len([*g])) // 2 * [k * 2, 0] + l % 2 * [k] for k, g in groupby(nums)), []), key=not_)


test_list = [0,1]
c = Solution()
print(c.applyOperations2(test_list))
