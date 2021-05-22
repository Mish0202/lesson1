age = int(input("Введите ваш возраст:"))
def life_stage(x):
    if age < 7:
        text = "Вам следует посещать детский сад"
    if age >= 7 and age <=17:
        text = "Вам следует учиться в школе"
    if age > 17 and age <=22:
        text = "Вам следует учиться в ВУЗе"
    if age > 22 and age <= 65:
        text = "Вам следует работать"
    if age > 65:
        text = "Вы на заслуженном отдыхе!"
    return text

print(life_stage(age))