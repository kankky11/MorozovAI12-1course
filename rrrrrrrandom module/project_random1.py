import random
dragon_hp = 1000
while True:
    print("====== Добро пожаловать в Dragon Dice Game! ======")
    print("\n^^^ Хотите начать игру? ^^^")
    print("\n### Введите Да или Нет. ###\n")
    start = input().strip().lower()
    if start != "нет" and start != "да":
        print("Ошибка ввода.")
        continue
    elif start == "нет":
        print("\nДо свидания!")
        exit()
    elif start == "да":
        print("\nОтлично! Тебе предстоит сразиться с драконом, путем броска 2х кубиков,")
        print("суммируя их значение и умножая на 2, получив окончательный урон!")
        print("Базовое здоровье дракона: 1000 hp")
        print("\nНачнем же?")
        print("\n== Введите Да или Нет. ==\n")
        start_game = input().strip().lower()
        if start_game == "нет":
            print("Ждем вас позже!")
            exit()
        elif start_game == "да":
            while True:
                dice1 = random.randint(1, 20)
                dice2 = random.randint(1, 20)
                total = dice1 + dice2
                if dice1 == dice2 and dice1 == 20:
                    print(f"Выпало {dice1} и {dice2}. Критический успех! Дракон повержен!")
                    break
                elif dice1 == dice2 and dice1 == 1:
                    print(f"Выпало {dice1} и {dice2}. Критический провал! Вы попадаете в ловушку!")
                    break
                elif total == 40 or total == 3:
                    print(f"Выпало {dice1} и {dice2}. Легендарный бросок!")
                    print("Здоровье дракона уменьшено вдвое!")
                    dragon_hp //= 2
                    print(f"Здоровье дракона = {dragon_hp}")
                    if dragon_hp <= 0:
                        print("Дракон повержен! Вы прошли игру!")
                        break
                else:
                    print(f"Выпало {dice1} и {dice2}. Сумма урона (Сумма кубиков x2) = {total * 2}")
                    print(f"Здоровье дракона равно {dragon_hp - (total * 2)}")
                    dragon_hp -= total * 2
                    if dragon_hp <= 0:
                        print("Дракон повержен! Вы прошли игру!")
                        break
                while True:
                    continuation = input("\nБросить еще? Да/Нет: ").strip().lower()
                    if continuation == "да":
                        break
                    elif continuation == "нет":
                        print("Спасибо за игру!")
                        exit()
                    else:
                        print("Ошибка ввода. Введите 'Да' или 'Нет'.")