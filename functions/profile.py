def prof():
    rebenok = [] # Профиль ребенка

    interes = input('Интересы ребёнка: ').lower()
    vozrast = input('Возраст ребенка: ')
    ask_ovz = int(input('Есть ли у ребенка ОВЗ? (1-Да, 2-Нет): ')) # Ввод информации о ребенке
    if ask_ovz == 1:
        ovz = True
    elif ask_ovz == 2:
        ovz = False
    ask_form_obuch = int(input('Предпочтительная форма обучения (1-Очная, 2-Очно-заочная, 3-Заочная): '))
    if ask_form_obuch == 1:
        form_obuch = 'очная'
    elif ask_form_obuch == 2:
        form_obuch = 'очно-заочная'
    elif ask_form_obuch == 3:
        form_obuch = 'заочная'
    mesto = input('Муниципалитет: ').lower()

    rebenok.append(interes) # Добавление информации о ребенке в профиль
    rebenok.append(vozrast)
    rebenok.append(ovz)
    rebenok.append(form_obuch)
    rebenok.append(mesto)
    return rebenok