spec = []
searched = []
with open(r'C:\res\data.txt','r', encoding='utf-8') as f:
    start = f.readlines()
    for i in start:
        timemas = i.split('<=>')
        spec.append([timemas[0],timemas[1],timemas[2],timemas[3],timemas[4],timemas[5],timemas[6][:-2]])
class search:               # поиск
    def __init__(self):
               # найденные
        poisk = str(input()).lower()
        for i in spec:
            timewords = i[0].lower().replace('"','')[42:].split() #делим название по пробелу
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

search()