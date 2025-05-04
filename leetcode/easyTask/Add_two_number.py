def addTwoNumbers(l1, l2):
    dif = len(l1) - len(l2)
    if dif > 0:
        l2 +=[0]*dif
    else:
        l1 +=[0]*(-1*dif)
    count = 0
    for num in range(len(l1)):
        count = l1[num] + l2[num] + count
        l1[num] = int(count % 10)
        count = int(count // 10)
        if num == len(l1) - 1 and count !=0:
            l1 += [count]
    return l1

print(addTwoNumbers([2,4,3], [5,6,4]))
print(addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))