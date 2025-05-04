#here is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile
# i is represented by colors[i]:
#colors[i] == 0 means that tile i is red.
#colors[i] == 1 means that tile i is blue.
#An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except
# the first and last one has a different color from its left and right tiles).
#Return the number of alternating groups.
#Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
#https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-03-09

def numberOfAlternatingGroups(colors, k):
    number_of_gr = 0
    count = 0
    vel_before = colors[-(k - 1)]
    for i in range(-(k - 1), len(colors), 1):
        if colors[i] != vel_before:
            count += 1
        else:
            count = 0
        vel_before = colors[i]
        if count > k - 2:
            number_of_gr += 1
    return number_of_gr

def numberOfAlternatingGroups1(colors, k):
    number_of_gr = 0
    count = 0
    vel_before = colors[-k]
    for i in range(-(k - 1), len(colors) - 1, 1):
        if colors[i] != vel_before:
            count += 1
            if count > k - 2:
                number_of_gr += 1
                vel_before = colors[i]
                continue
            vel_before = colors[i]
            continue
        vel_before = colors[i]
        count = 0
    return number_of_gr

def numberOfAlternatingGroups2(colors, k):
    test_list = colors + colors[0:k - 1]
    number_of_gr = 0
    count = 0
    vel_before = test_list[0]
    for i in test_list:
        if i != vel_before:
            count += 1
        else:
            count = 0
        vel_before = i
        if count > k - 2:
            number_of_gr += 1
    return number_of_gr


print(numberOfAlternatingGroups1([0,1,0,1,0], 3)) #3
print(numberOfAlternatingGroups2([0,1,0,0,1,0,1], 6)) #2
print(numberOfAlternatingGroups([1,1,0,1],4)) #0

