#You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing
#the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
#You are also given an integer k, which is the desired number of consecutive black blocks.
#In one operation, you can recolor a white block such that it becomes a black block.

def minimumRecolors(blocks,k):
    max_b  = 0
    now_b = 0
    lenth = len(blocks)
    for i in range(lenth):
        if blocks[i] == "B":
            now_b +=1
            if i > k and blocks[i - k] == "B":
                now_b -=1
        elif i > k and blocks[i - k] == "B":
            now_b -= 1
        if  now_b > max_b:
            max_b = now_b
    if max_b > k:
        return 0
    return k - max_b

print(minimumRecolors("WBWBBBW", 2))