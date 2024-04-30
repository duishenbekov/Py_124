# n = int(input("napiwite chislo: "))
# list_ = []
# for i in range(1, n+1): 
#     print(i)
# # for i in range(1, n+1): 
#     list_.append(i * i * i)
# print(list_)


# zadanie2
# n = int(input("napiwite chislo: "))
# print(n)
# list_ = []
# for i in range(1, n+1):
#     if n % i == 0:
#         list_.append(i)
# print(list_)
# zadanie3
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# step = int(input("napiwite shag: "))
# stroka = input("napiwite soobwenie: ")
# new_stroka = ''
# # bwfusvfupdbftbs
# for simvol in stroka:
#     ind = alphabet.index(simvol)
#     new_simvol = alphabet[ind-step]
#     new_stroka += new_simvol
#     print(f'{new_simvol}')
# print(new_stroka)

num = int(input('napiwite chislo: '))
numbers = []
for i in range(num):
    num2 = int(input())
    numbers.append(num2)
print(numbers)
sum_nums = []
for i in range(num-1):
    sum_element = numbers[i] + numbers[i + 1]
    sum_nums.append(sum_element)
print(sum_nums)



