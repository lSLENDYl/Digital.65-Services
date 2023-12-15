dost = [                    # достопримечательности
    ("музей", 2),
    ("лягушка", 4),
    ("столб", 1),
    ("яма", 0),
    ("музей негров", 9),
    ("казахи сила", 9)]
choice = int(input("1. показать популярное, 2 - найти достопримечательности, 3 - показать всё "))

class pop:                  # популярные
    def __init__(self):
        dost.sort(key=lambda d: d[1], reverse=True)
        for i in dost[0:3]:
            print("{}, посещаемость сайта за день: {}".format(i[0], i[1]))

class search:               # поиск
    def __init__(self):
        searched = []       # найденные
        poisk = str(input()).lower()
        for i in dost:
            timewords = i[0].split() #делим название по пробелу
            for k in timewords:
                k = str(k)
                kol = 0
                for r in range(len(poisk)): # поиск по буквам
                    try:
                        if k.index(poisk[r]) >= 0:
                            if kol >= 1:
                                if k[k.index(poisk[r-1]) + 1] == poisk[r]:
                                    kol += 1
                            else: kol += 1
                    except: pass
                if kol == len(poisk):
                    print(i[0]) #вывод найденого
                    searched.append(i)

class all:                  # все
    def __init__(self) -> None:
        for i in dost:
            print(i[0])

match choice:
    case 1:
        pop()
    case 2:
        search()
    case 3:
        all()