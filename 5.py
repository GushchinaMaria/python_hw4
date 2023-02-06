"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""
# version1
import timeit


def my_func_1(num1, num2, num3):
    arr = [num1, num2, num3]
    arr.sort()
    return arr[1] + arr[2]


# version2
def my_func_2(num1, num2, num3):
    arr = [num1, num2, num3]
    max1 = max(arr)
    arr.remove(max1)
    max2 = max(arr)
    return max1 + max2


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

print("Производительность функции при повторе 10000 раз: ")
print("При использовании функции sort():")
print(timeit.timeit("my_func_1(num1,num2,num3)", globals=globals(), number=10000))
print("Без использования функции sort():")
print(timeit.timeit("my_func_2(num1,num2,num3)", globals=globals(), number=10000))

print(
    "Замеры времени показали, что при использовании встроенной функции sort() время выполнения программы меньше, чем при использовании написанной вручную функции."
)
