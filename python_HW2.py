# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# S = int(input('Введите сумму чисел: '))
# P = int(input('Введите произведение чисел: '))
# D = S**2 - 4*P
# if D == 0:
#     x_1 = S / 2
#     x_2 = S / 2
#     print(x_1, x_2)
# elif D > 0:
#     x_1 = (S + D**0.5) / 2 
#     x_2 = (S - D**0.5) / 2
#     print(round(x_1, 2), round(x_2, 2))
# else:
#     print('решения нет')


# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input("Введите кол-во монет: "))
# count_orel = 0
# count_reshka = 0
# for i in range(n):
#     x = int(input("Введите сторону монеты(1 или 0): "))
#     if x == 1:
#         count_reshka += 1
#     else:
#         count_orel += 1
# if count_orel > count_reshka:
#     print(count_reshka)
# else:
#     print(count_orel)

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# N = int(input('Введите степень двойки: '))
# for i in range(N + 1):
#     print(2, '**',  i, '=', 2 ** i)