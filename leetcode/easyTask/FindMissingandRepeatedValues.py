grid = [[9,1,7],[8,9,2],[3,4,6]]
n = len(grid[0])
# dict_checkingnumb = {num: 0 for num in range(1, n ** 2 + 1)}
# result_list = [0, 0]
# for i in grid:
#     for j in range(n):
#         dict_checkingnumb[i[j]] += 1
# for id, value in dict_checkingnumb.items():
#     if value == 0:
#         result_list[1] = id
#     if value == 2:
#         result_list[0] = id

# grid_list = []
# max_val = n ** 2 + 1
# n = len(grid[0])
# for i in grid:
#     for j in range(n):
#         grid_list.append(i[j])
# print(grid_list)
# grid_set = set(grid_list)
# result_l = [sum(grid_list) - sum(grid_set), sum(range(1, max_val))  - sum(grid_set)]

grid_list = sum(grid, [])
max_val = n ** 2 + 1
# for i in grid:
#     for j in i:
#         grid_list.append(j)
print(grid_list)
grid_set = set(grid_list)
result_l = [sum(grid_list) - sum(grid_set), sum(range(1, max_val))  - sum(grid_set)]
print(result_l)





