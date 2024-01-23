#Таблица умножения
#На вход подается число n.
#Написать скрипт в любой парадигме,
#который выводит на экран таблицу
#умножения всех чисел от 1 до n.
#Обоснуйте выбор парадигм

#Процедурный стиль

def multiplication_table(n):
    for i in range(1, n + 1):
        print_table_row(i)

def print_table_row(row_number):
    for j in range(1, 10):
        result = row_number * j
        print(f"{row_number} * {j} = {result}")

n = int(input("Введите число n: "))
multiplication_table(n)
