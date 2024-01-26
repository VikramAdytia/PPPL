"""
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами).
"""
import numpy as np
import matplotlib.pyplot as plt
'''
+1 - Полная положительная корреляция
+0,8 - Сильная положительная корреляция
+0.6 - Умеренная положительная корреляция
0 - никакой корреляции
-0.6 - Умеренная отрицательная корреляция
-0,8 - Сильная отрицательная корреляция
-1 - Полная отрицательная корреляция
'''


def calc_correl(arr1: list[int], arr2: list[int]) -> float:
    avg_arr1 = np.mean(arr1)
    avg_arr2 = np.mean(arr2)

    dev_x = arr1 - avg_arr1
    dev_y = arr1 - avg_arr2

    covariance = np.sum(dev_x * dev_y)

    std_x = np.sqrt(np.sum(dev_x ** 2))
    std_y = np.sqrt(np.sum(dev_y ** 2))

    if std_x != 0 and std_y != 0:
        correlation = covariance / (std_x * std_y)
    else:
        correlation = 0

    plt.scatter(arr1, arr2)
    plt.title('Корреляция Пирсона')
    plt.xlabel('Первый массив')
    plt.ylabel('Второй массив')
    plt.show()

    return correlation

if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5, 12, 22, 32, 44, 55]
    array2 = [2, 4, 6, 8, 10, 20, 40, 60, 80, 100]

    print(f"Корреляция Пирсона: {calc_correl(array1, array2)}")
