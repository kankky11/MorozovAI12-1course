print("Калькулятор путешественника")
name = input("Введите имя: ")
while True:
    print("\n=== Здравствуйте, " + name + "!" + "===")
    print("\nВыберите режим: ")
    print("\n1 - Классический калькулятор")
    print("\n2 - Финансовый калькулятор")
    print("\n0 - Завершить программу.")
    mode = input("\nВыберите режим: ")
    if mode not in ['1', '2', '0']:
        print("\nНеверный ввод. Попробуйте ещё раз.")
        continue
    elif mode == "0":
        print("\nДо свидания, " + name + "!")
        exit()
    elif mode == "1":
        print("\n== Классические операции: ==")
        print("\nСложение (+)")
        print("Вычитание (-)")
        print("Деление (/)")
        print("Умножение (*)")
        print("Деление нацело (//)")
        print("Остаток от деления (%)")
        print("Возведение в степень (**)")
        print("________________")
        print("\n0 - Завершить программу.")
        print("________________")
    elif mode == "2":
        print("\n== Финансовые операции: ==")
        print("\n1 - Сумма расходов")
        print("2 - Стоимость поездки в день")
        print("3 - Остаток бюджета")
        print("________________")
        print("\n0 - Завершить программу.")
        print("________________")
    # классические операции
    operation = input("Введите операцию: ")
    if operation == '0':
        print("\nДо свидания, " + name + "!")
        exit()
    if operation not in ['0', '+', '-', '/', '//', '%', '**', '*', '1', '2', '3']:
        print("Неверный ввод.")
        exit()
    if operation in ['+', '-', '/', '//', '%', '**', '*']:
        name1 = float(input("Введите первое число: "))
        name2 = float(input("Введите второе число: "))
        if operation == '+':
            result = name1 + name2
            print(f"\nОтвет:  {result:.2f}")
        elif operation == '-':
            result = name1 - name2
            print(f"\nОтвет:  {result:.2f}")
        elif operation == '*':
            result = name1 * name2
            print(f"\nОтвет:  {result:.2f}")
        elif operation == '/':
            if name2 == 0:
                print("\nОшибка деления. На ноль делить нельзя.")
            result = name1 / name2
            print(f"\nОтвет:  {result:.2f}")
        elif operation == '//':
            if name2 == 0:
                print("\nОшибка деления. На ноль делить нелья.")
            result = name1 // name2
            print(f"\nОтвет:  {result:.2f}")
        elif operation == '%':
            if name2 == 0:
                print("\nОшибка деления. Делить на ноль нельзя.")
            result = name1 % name2
            print(f"\nОтвет:  {result:.2f}")
        elif operation == '**':
            result = name1 ** name2
            print(f"\nОтвет:  {result:.2f}")
    # финансовые операции
    if operation not in ['1', '2', '3']:
        if operation in ['1', '2', '3']:
            if operation == '1':
                total = 0
                print("Вводите суммы расходов по одной. Чтобы закончить, просто нажмите Enter (оставьте строку пустой).")
                while True:
                    expenses = input("Введите расходы: ")
                    if expenses == "":
                        break
                    amount = float(expenses)
                    total += amount
                print(f'\nСумма ваших расходов равна: {total:.2f}')
            elif operation == '2':
                budget = float(input("Введите бюджет: "))
                days = float(input("Введите дни: "))
                result = budget / days
                print(f'\nВаша стоимость поездки на день: {result:.2f}')
            elif operation == '3':
                budget = float(input("Введите бюджет: "))
                expenses = float(input("Введите расходы: "))
                result = budget - expenses
                print(f'\nВаш оставшийся бюджет: {result:.2f}')
    input("\nНажмите Enter, чтобы продолжить...")