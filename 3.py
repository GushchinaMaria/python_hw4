"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

#version1
def my_func_1(num1, num2, num3):
    arr = [num1,num2,num3]
    arr.sort()
    return arr[1] + arr[2]


# version2
def my_func_2(num1, num2, num3):
    arr = [num1, num2, num3]
    max1 = max(arr)
    arr.remove(max1)
    max2 = max(arr)
    return max1+max2


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
print(f"C функцией sort(): {my_func_1(num1, num2, num3)}")
print(f"Без функции sort(): {my_func_2(num1, num2, num3)}")