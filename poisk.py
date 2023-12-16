dost = {
    "кванториум": [1, 2],
    "сноуборд": [1, 2],
    "футболл": [1, 2]
}

class search:               # поиск
    def __init__(self):
        searched = []       # найденные
        poisk = str(input()).lower()
        for k in dost:
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
                print(k) #вывод найденого
                searched.append(k)

search()