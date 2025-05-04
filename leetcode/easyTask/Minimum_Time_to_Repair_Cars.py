def repairCars(ranks, cars):
    ranks.sort()
    min_v = ranks[0]
    l = min_v * (cars ** 2)
    res = 0
    while l > 0:
        for i in ranks:
            res += int((l / i) ** 0.5)
        if res < cars:
            return l + 1
        l -=1
        res = 0

def repairCars1(ranks, cars):
    ranks.sort()
    low_rank = ranks[-1]
    aver_car = (cars/ len(ranks))
    list_c_rep = [int(((low_rank *aver_car**2)/ rank)**0.5) for rank in ranks]
    index = sum(list_c_rep) - cars
    while True:
        if index < 0:
            index += len(ranks)
        elif index > len(ranks):
            index -= len(ranks)
    if index == len(ranks):
        return ranks[-1]**list_c_rep[- index]**2
    return ranks[-index]**list_c_rep[- index]**2


# print(repairCars1([4,2,3,1], 10))
# print(repairCars1([5,1,8], 6))
print(repairCars1([3,3,1,2,1,1,3,2,1], 58))
t = [35,5,31,9,25,16,30,12,29,11,33,15,31,14,30,3,29,26,19,3,4,16,12,30,10,22,25,44,41,37,3,41,13,18,19,41,40,17,40,38,
     12,25,24,18,5,2,32,44,10,16,33,10,35,36,31,3,5,19,42,34,1,27,29,39,4,21,13,3,14,8,9,16,27,18,20,4,41,26,43,34,18,
     34,26,13,5,43,5,32,7,36,33,25,19,32,4,21,33,13,37,34,21,11,42,42,4,8,42,32,15,20,3,38,9,32,12,7,43,19,17,23,11,
     10,8,38,3,4,42,7,11,35,38,14,13,13,2,1,1,10,43,14,7,20,41,7,21,14,21,38,2,17,31,21,4,31,5,8,44,40,16,11,11,21,11,
     31,44,14,14,30,2,2,6,9,39,34,8,21,42,29,32,12,31,20,6,26,21,25,34,3,14,6,8,38,26,18,25,9,43,9,37,14,24,20,6,33,25,
     38,32,10,35,18,19,31,17,43,37,11,15,28,11,31,11,39,27,39,11,38,9,27,8,22,44,29,14,37,21,16,7,31,1,15,34,8,35,32,21,
     5,27,9,42,11,15,22,5,38,44,26,9,41,16,3]
print(repairCars1(t, 890583))
print(155235920)