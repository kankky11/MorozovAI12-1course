print("=== Читательский дневник ===")
books = []
name = input("Введите имя: ")

while True:
    print(f"\n=== Здравствуйте, {name}! ===")
    print("\n1 - Добавить книгу")
    print("2 - Показать все книги")
    print("3 - Показать последние 5 прочитанных")
    print("4 - Заменить название по номеру")
    print("5 - Поиск по названию")
    print("6 - Статистика")
    print("0 - Выход")

    mode = input("\nВыберите режим: ")

    if mode not in ['1', '2', '3', '4', '5', '6', '0']:
        print("\nНеверный ввод. Попробуйте ещё раз.")
        input("\nНажмите Enter, чтобы продолжить...")
        continue

    if mode == '1':
        book_name = input("\nВведите название книги: ").strip()
        if book_name:
            books.append(book_name)
            print("\nКнига добавлена.")
        else:
            print("\nНеверный ввод")

    elif mode == '2':
        print(f"В дневнике {len(books)} книг.")
        if len(books) == 0:
            print("Дневник пустой.")
        else:
            for i in range(len(books)):
                print(f"{i + 1}. {books[i]}")

    elif mode == '3':
        if len(books) == 0:
            print("Список пустой")
        elif len(books) != 0:
            last_books = books[-5:]
            print(f"Последние 5 прочитанных: " + ", ".join(last_books))
        elif len(books) < 5:
            print(books)

    elif mode == '0':
        print("До свидания!")
        break
    input("\nНажмите Enter, чтобы вернуться в меню...")