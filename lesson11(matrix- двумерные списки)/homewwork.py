'zadanie 1'
# nomer_1 = 3
# nomer_2 = 4
# array = []
# for i in range(nomer_1):
#     array.append([])
#     for j in range(nomer_2):
#         array[i].append(1)
# print(array)
# matrix = [[1 for i in range(4)]for j in range(3)]
# print(matrix)

'zadanie2'
# nomer1 = 3
# array = []
# num = 1
# for i in range(nomer1):
#     array.append([])
#     for j in range(nomer1):
#         array[i].append(num)
#         num += 1
# print(array)
# matrix2 = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]
# print(matrix2)
'zadanie 3'
# n = int(input("napiwite"))
# m = int(input("napiwite"))
# array = list(range(n))
# for i in range(n):
#     array[i] = list(range(m))
#     for j in range(m):
#         text = f'vvedite element v {i} x {j} pozociya'
#         el = input(text)
#         array[i][j] = el
# print(array)
matrix3 = [[input(f'zapolnite element {i+1}:{j+1}: ')for j in range(3)] for i in range(2)]
for row in matrix3:
    print(*row)
# n = 3
# m = 3
# array = list(range(n))
# for i in range(n):
#     array[i] = list(range(m))
#     for j in range(m):
#         text = f'vvedite element v {i} x {j} poziciya'
#         el = input(text)
#         array[i][j] = el
# print(array)

'zadanie 4'

# for i in range(1, 6):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i * j}')
#     print()

'zadanie 5'
# n = '.'
# m = 4
# array = []
# for i in range(1,9):
#     array.append([])
#     for j in range(1,9):
#         array[i].append(j)
#         n += 1
# print(array)

