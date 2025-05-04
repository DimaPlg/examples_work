#There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this
# party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with
# the smallest number.
#For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
#When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at
# that same moment, they can sit in that chair.
#You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and
# leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.
#Return the chair number that the friend numbered targetFriend will sit on.
from logging import fatal
from operator import index


def smallestChair(times, targetFriend):
    remember_user = times[targetFriend]
    res_list = [[0, 0]]
    friend_before_target = [x for x in times if x[0] - 1 < remember_user[0]]
    friend_before_target = sorted(friend_before_target)
    min_value_end = res_list[0][1]
    for i in friend_before_target:
        for j in range(len(res_list)):
            if res_list[j][1] - 1 < i[0] and min_value_end - 1 < i[0]:
                res_list[j][1] = i[1]
                if res_list[j][1] < min_value_end - 1:
                    min_value_end = res_list[j][1]
                if i == remember_user:
                    remember_user = res_list[j]
                break
            elif j == len(res_list) - 1:
                res_list.append(i)
                break
    print(res_list)
    return res_list.index(remember_user)

def smallestChair1(times, targetFriend):
    remember_user = times[targetFriend]
    times.sort()
    friends_num = len(times)
    chair_time = [0] * friends_num

    for i in times:
        for j in range(friends_num):
            if chair_time[j] <= i[0]:
                chair_time[j] = i[1]
                if i == remember_user:
                    return j
                break
    return 0

# def smallestChair(times, targetFriend):
#     chek_val = times[targetFriend]
#     chair_l = []
#     result_c = []
#     count = 0
#     for x in sorted(times):
#         chair_l += [x]
#         if x == chek_val:
#             break
#     for x in chair_l:
#         result_c[count] += x
#         if x[-1] - 1 < chek_val[0]:
#             result_c[count]
#     return chair_l.index(chek_val)


# print(smallestChair([[1,4],[2,3],[4,6]], 1)) #1
# print(smallestChair([[3,10],[1,5],[2,6]], 0)) #2
#print(smallestChair([[2,4],[4,9],[3,4],[6,8],[5,10]], 4)) #1
print(smallestChair1([[33,35],[26,29],[9,28],[4,31],[8,10],[32,34],[15,24],[27,39],[14,36],[1,14],[25,39],[5,27],[6,15],[2,38],[19,36],[24,34],[3,26]],0)) #3
