# Задача№1
# Дан список целых чисел numbers.
# Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания.
# Можно использовать любой алгоритм сортировки

def sort_list_imperative(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


numbers = [64, 34, 25, 12, 22, 11, 90]
sort_list_imperative(numbers)
print("Отсортированный список в порядке убывания:", numbers)


# Задача№2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    numbers.sort(reverse=True)


numbers = [64, 34, 25, 12, 22, 11, 90]
sort_list_declarative(numbers)
print("Отсортированный список в порядке убывания:", numbers)
