tour_lst = []  # Массив с названиями туров
excursion_lst = []  # Массив с названиями экскурсий
tour_description_lst = []  # Массив с описаниями туров
excursion_description_lst = []  # Массив с описаниями экскурсий

while True:
    print('1-Список туров и экскурсий, 2-Поиск тура/экскурсии, 3-Рекомендация тура/экскурсии')

    choice = int(input())
    if choice == 1:
        num = 1
        print('1-Туры, 2-Экскурсии')
        choice_1 = int(input())
        if choice_1 == 1:
            print('Туры по Сахалину')
            for el in tour_lst:
                print(str(num) + '.', el)  # Вывод списка туров
                num += 1
        elif choice_1 == 2:
            print('Экскурсии по Сахалину')
            for el in excursion_lst:
                print(str(num) + '.', el)  # Вывод списка экскурсий
                num += 1

    elif choice == 2:
        found = [] # Список найденых туров/экскурсий
        print('Найти: 1-Тур, 2-Экскурсия')
        choice_2 = int(input())
        if choice_2 == 1:
            print('Поиск Тура')
            my_request = input().lower() # Слово для поиска
            for el in tour_lst:
                request_splt = el.split()  # Разделение названия по пробелу
                for i in request_splt:
                    if my_request == i.lower():
                        print(el)  # Если что то найдено в названии, выводим это
                        found.append(el)  # Добавление найденного тура в список
            for des in tour_description_lst:
                des_splt = des.split()  # Деление описания по пробелам
                for i in des_splt:
                    if i.lower() == my_request and tour_lst[tour_description_lst.index(des)] not in found:
                        print(tour_lst[tour_description_lst.index(des)]) # Если что то найдено, вывод названия тура
        elif choice_2 == 2:
            my_request = input().lower()  # Ниже то же самое, что и с поиском тура
            for el in excursion_lst:
                request_splt = el.split()
                for i in request_splt:
                    if my_request == i.lower():
                        print(el)
                        found.append(el)
            for des in excursion_description_lst:
                des_splt = des.split()
                for i in des_splt:
                    if i.lower() == my_request and excursion_lst[excursion_description_lst.index(des)] not in found:
                        print(excursion_lst[excursion_description_lst.index(des)])

    elif choice == 3:
        print('В разработке')  # (Надо добавить парсинг)
