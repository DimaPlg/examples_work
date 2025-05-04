#A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j].
# The width of such a ramp is j - i.
#Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.
from xmlrpc.client import Boolean


def maxWidthRamp(nums):
    len_nums = len(nums)
    max_w = 0
    for i in range(len_nums - 1, 0, -1):
        if nums[i] - nums[i - 1] == 1:
            continue
        for j in range(0, i):
            if nums[j] < nums[i] and max_w < i - j:
                max_w = i - j
        if max_w > i:
            break
    return max_w

def maxWidthRamp1(nums):
    n = len(nums)
    indices = [i for i in range(n)]

    # Sort indices based on corresponding values in nums and ensure stability
    indices.sort(key=lambda i: (nums[i],i))

    min_index = n  # Minimum index encountered so far
    max_width = 0

    # Calculate maximum width ramp
    for i in indices:
        max_width = max(max_width, i - min_index)
        min_index = min(min_index, i)

    return max_width

#print(maxWidthRamp([6,0,8,2,1,5]))
l = [49997,49997,49995,49994,49994,49993,49993,49992,49991,49991,49991,49991,49990,49989,49988,49987,49984,49983,49983,
     49982,49982,49981,49981,49978,49978,49977,49977,49976,49976,49975,49975,49974,49972,49972,49971,49971,49969,49967,
     49966,49965,49965,49962,49960,49959,49959,49956,49956,49955,49954,49954,49952,49952,49951,49951,49951,49951,49950,
     49949,49949,49949,49948,49947,49946,49945,49942,49941,49941,49941,49940,49939,49938,49937,49936,49935,49934,49934,
     49932,49931,49931,49931,49930,49930,49926,49925,49925,49925,49925,49924,49923,49923,49921,49920,49918,49917,49917,
     49917,49916,49916,49916,49915,49915,49911,49911,49909,49907,49905,49905,49904,49901,49899,49898,49898,49898,49897,
     49896,49896,49894]

#print(maxWidthRamp(l))
#print(maxWidthRamp1(l))
# n = len(l)
# indices = [i for i in range(n)]
# print(indices)
# indices.sort(key=lambda i: (l[i]))
# print(indices)
# indices.sort(key=lambda i: (l[i], i))
# print(indices)
string = '123.045.067.089'
ip_list = string.split(".")
for st in ip_list:
    if not st.isdigit() or len(st) > len(str(int(st))) or (int(st) < 0 and int(st) < 256):
        break
res = (False for st in string.split(".") if not st.isdigit() or len(st) > len(str(int(st))) or (int(st) < 0 and int(st) < 256))
