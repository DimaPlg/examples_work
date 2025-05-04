def lengthOfLongestSubstring(s):
    long = 0
    substring = ''
    max_long = 0
    for char in s:
        if char not in substring:
            long +=1
            substring += char
            if max_long < long:
                max_long = long
        else:
            long -= substring.index(char)
            substring = substring[substring.index(char) + 1:] + char

    for num in range(len(s)):
        if s[num] not in substring:
            long += 1
            substring += s[num]
            if max_long < long:
                max_long = long
        else:
            long
    return max_long

print(lengthOfLongestSubstring("aabaab!bb"))