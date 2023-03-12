################## Дано ціле число (int). Визначити скільки нулів у цьому числі.
# num = 120000330
# end = str(num)
# result = end.count('0')
# print(result)



############## Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі

# num = 1002000
# s = str(num)
# count = 0
# for i in range(len(s)-1, -1, -1):
#     if s[i] != '0':
#         break
#     count += 1
# print(count)


#########Дано списки my_list_1 та my_list_2.Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.

# my_list_1 = [4, 5, 7, 988, 76]
# my_list_2 = [1, 23, 45, 67, 9]
# my_result = []
# for i in my_list_1[1:-1:2]:
#     my_result.append(i)
# for i in my_list_2[1:-1:2]:
#     my_result.append(i)
# print(my_result)




#########Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
#стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]

# my_list = [1, 2, 3, 4]
# my_list.pop(0)
# my_list.append(1)
# new_list = my_list.copy()
# print(new_list)


################аний список my_list. У цьому списку перший елемент переставити на останнє місце.
# [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)

#my_list = [1, 2, 3, 4]
# my_list.pop(0)
# my_list.append(1)
# new_list = my_list.copy()
# print(new_list)

#################Дано рядок у якому є числа (розділяються пробілами).
#Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
#Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)

# sentence = "43 більше ніж 34 , але менше ніж 56 "
# words = sentence.split(' ')
# total_sum = 0
# for i in words:
#     if i.isdigit():
#         total_sum += int(i)
# print(total_sum



#  Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.

# list = [2,4,1,5,3,9,0,7]
# count = 0
# for i in range(0, len(list)-1):
#     if list[i] > list[i-1] + list[i+1]:
#         count += 1
#     else:
#         pass
# print(count)

# Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33] Створити новий список у який помістити лише рядки з my_list.


# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
# for i in my_list:
#     if type(i) == str:
#         new_list.append(i)
# print(new_list)

# Дано рядок my_str. Створити список в який помістити символи з my_str, які зустрічаються в рядку ТІЛЬКИ ОДИН разів.

# my_str = 'ffkkkkgggdlll;lllhhh'
# list = []
#
# for i in set(my_str):
#     if my_str.count(i) == 1:
#         list.append(i)
# print(list)

# Дано два рядки. Створити список, у якому помістити ті символи,які є в обох рядках хоча б один раз.

# str_1 = "rgk;fjoiropgk"
# str_2 = "gfdjklfjddlf04r"
# new_list = list(set(str_1).intersection(set(str_2)))
# print(new_list)

# Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,але в кожній ТІЛЬКИ З одного разу.
# Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу



# str_1 = "aaaasdf1"
# str_2 = "asdfff2"
# new_list = []
# for i in set(str_1).intersection(set(str_2)):
#     if str_1.count(i) == 1 and str_2.count(i) == 1:
#         new_list.append(i)
# print(new_list)