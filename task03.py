# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

name = input("Введите Ваше имя: ")
surname = input("Введите Вашу фамилию: ")
age = int(input("Введите Ваш возраст: "))
weight = int(input("Введите Ваш вес: "))

print(name, end=" ")
print(surname, end=", ")
print(age, "год", end=", ")
print("вес", weight, "кг", end=" - ")

if age <= 30 and 50 <= weight <= 120:
    print('у Вас хорошее состояние здоровья!')
elif (30 < age <= 40) and (weight < 50 or weight > 120):
    print('Вам следует заняться собой!')
elif age > 40 and (weight < 50 or weight > 120):
    print('Вам необходимо обратиться к врачу!')
else:
    print('Ваше состояние хорошее, но стоит следить за собой!')
