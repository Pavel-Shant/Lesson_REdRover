# Домашнее задание (занятие 1)

# задание 1  Вывести строку "Hello, world!" (без кавычек) в консоль с помощью функции print
# print("Hello, world!")

# задание 2
#Выведите строку в консоли “Я люблю:”, а затем 3 пронумерованных пункта с тем, что вам нравится, например:
# print("Я люблю:")
# print("1. Заниматься спрортом")
# print("2. Кататься на велосипеде")
# print("3. Кататься на мотоцикле")

# name = input("введите имя:  ")
# print("Привет", name)
#
# """
# Задача 1:
# Необходимо ввести 2 числа из консоли, присвоив значения переменным.
# Произвести вывод результатов всех произведенных математических действий в консоль.
# Виды операций на Ваше усмотрение.
# Вывод необходимо производить используя один из трех вариантов форматирования строк.
# Пример получившегося вывода: "Результатом __операция__ над числами __а__ и __b__ будет __результат__"
# (Подсказка: __х__ - необходимые значения)
# (Пример вывода: "Результатом сложения над числами 3 и 5 будет 8")
#
# Задача 2:
# Необходимо получить слово, предложение и/или отрывок текста из консоли и присвоить их переменной/ым.
# Произвести над ним действия и применить методы, изученные на уроках и самостоятельно.
# Количество примененных методов и их тип зависят только от вашего воображения и изученного материала.
# """
# from math import trunc
# from multiprocessing.spawn import is_forking
#
# from pyexpat.errors import messages

# =================================================================================================
# Домашнее задание (занятие 2)
# Посмотрите на следующие переменные:
# 1num = 100                           num = 100
# имя = “Алексей”                       name = "Алексей"
#  First_Number = 1                     first_number = 1
# “Мой текст” = text                    text = "Мой текст"
# phone_number = “Hi!”                  phone_number = 1111111
# Что с ними не так? Как бы вы их исправили?

# Создать переменную name со значением в виде строки своего имени. Затем вывести строку на экран в виде:
# "Привет, меня зовут <ваше имя>."
# Попробуйте выполнить эту задачу разными способами.

# name = "Pavel"
# print(f"Привет, меня зовут {name}.")
# message = "Привет, меня зовут" + " " + name + "."
# print(message)

# name = input("Введите ваше имя:").title()
# surname = input("Введите вашу фамилию:").title()
# print(f"Привет, меня зовут, {name}  {surname}")

# Создать переменную a, значение которой определяется через ввод данных с клавиатуры.
# Создать переменную b, значение которой определяется через ввод данных с клавиатуры.
# Вывести на экран сумму двух введенных чисел, если для a было введено 123, а для b 431, должно быть выведено 554.

# a = int(input("Введите число 1: "))
# b = int(input("Введите число 2: "))
# print("Сумма чисел а+б =", a + b)

#=====================================================================
# orld = "Космонафт"
# print(world[::-1])
# print(world[1:])
# print(world[2:6])
# ==============================================================================================
# Домашнее задание (занятие 3)
#  1 Четное или нечетное?
# n = int(input("Введите число: "))  #  Получаем число от пользователя и переводим число.
# if n % 2 == 0:                  # проверяем остаток от деления на 2
#         print("Четное")
# else:
#         print("Нечетное")

# 2. Какой сегодня день?
# day = input(f'введите название дня недели: ').lower()
# if  day == "суббота" or day == "воскресенье":
#     print("Сегодня выходной!")
# elif day == "среда":
#     print("Мне сегодня к стоматологу в 15:30")
# else:
#     print("Сегодня обычный день.")

# 3. Задание  Эхо
# n = int(input("Введите число: "))
# text = input("Введите текст: ")
# for _ in range(n):
#     print(text)

# -------------4. Задание. Сколько гласных букв?----------------------------------------

# message = input("Введите текст: ")
# vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
# count = 0            #счетчик
# for char in message.lower():     # приводим все символы к нижнему регистру
#     if char in vowels:
#         count += 1
# print(count)
# 5 Задание. Сумма чисел.

# total_sum = 0
# while True:
#     number = int(input("Введите целое число: "))
#     if number < 0:
#         break
#     total_sum += number
# print(total_sum)
# =============================================================================================
#   Домашнее задание (занятие 4)
# Сгенерируйте список numbers, состоящий из чисел в диапазоне от 0 до 100 включительно, которые делятся без остатка как на 2, так и на 3.
# Выведите список numbers на экран.
#
# Ответ: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
# # Решите эту задачу в 2 способа - с помощью генератора списков и без него.

# numbers = []
# for i in range(101):
#     if i % 6 == 0 :
#         numbers.append(i)
# print(numbers)

# numbers = [b for b in range(101) if b % 6 ==0]
# print(numbers)

# 2 задание
# Фильтр.
# Имеется список items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# Составьте новый список numbers, который содержит только целые числа (int) и вещественные числа (float) из списка items.
# Выведите на экран сумму чисел в numbers.
#
# Ответ:  291.52

# items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# # numbers = []
# # for i in items:
# #     if isinstance(i, (int, float)):
# #         numbers.append(i)
#
# # numbers = [x for x in items if isinstance(x, (int, float))]   --- второй вариант в одну строку
# print(sum(numbers))

#  ------------------3 задание

# messages = []
# while True:
#     message = input("Введите сообщение: ")
#     messages.append(message)
#     if len(messages) > 5:     # Удаляем первое сообщение, если список превышает 5 элементов
#         messages.pop(0)
#     if message == "Пока":
#         print("Ну ладно, пока!")
#         print(messages)
#         break
# =================================================================================