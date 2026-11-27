import random
while True:
    dice1 = random.randint(1, 20)
    dice2 = random.randint(1, 20)
    total = dice1 + dice2
    if dice1 == dice2 and dice1 == 20:
        print(f"Выпало {dice1} и {dice2}. Критический успех! Дракон повержен!")
    elif dice1 == dice2 and dice1 == 1:
        print(f"Выпало {dice1} и {dice2}. Критический провал! Вы попадаете в ловушку!")
    elif total == 40 or total == 3:
        print(f"Выпало {dice1} и {dice2}. Легендарный бросок!")
    else:
        print(f"Выпало {dice1} и {dice2}. Сумма урона = {total}")
    continuation = input("Бросить еще? Да/Нет: ").strip().lower()
    if continuation == "да":
        continue
    elif continuation == "нет":
        print("Спасибо за игру!")
        break
    else:
        print("Ошибка ввода. Введите 'Да' или 'Нет'")
        continue