# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4
print('Задача-1')
while True:
    number = int(input('Введите число: '))
    if 0 < number < 10:
        print('Верно')
        result = number ** 2
        print('Ваше число в степени 2 равно: ', result)
        break
    else:
        print('Данное число неверно. Введите число от 1 до 9 включительно')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
print()
print('Задача-2')
number1 = int(input('Введите первое значение: '))
number2 = int(input('Введите второе значение: '))
print('Первое значение', number1)
print('Второе значение', number2)
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print()
print('Первое значение', number1)
print('Второе значение', number2)