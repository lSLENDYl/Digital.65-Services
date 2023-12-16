spec = [
    ["сноуборд", "активный спорт", 8, 18, "нет", "очное", "шахтёрск", 2000],
    ["бпла", "айти", 14, 21, "да", "очное", "москва", 4500],
    ["математика", "учёба", 7, 18, "да", "очное", "корсаков", 1500],
    ["english", "учёба", 15, 20, "нет", "очное", "южный", 6000]
]

result = []
kol = 0

def specs(args):                        # фильтр по специальности
    if len(args) == 0:
        args=[i[1] for i in spec]
    args = list(set(args))
    global kol
    kol+=1
    for i in spec:
        for r in args:
            try:
                if i.index(r):
                    result.append(i)
            except: pass

def age(nage):                          # фильтр по возрасту
    if len(nage) == 0:
        nage = -1
    nage = int(nage)
    global kol
    kol+=1
    if nage == -1:
        for i in spec:
            result.append(i)
    else:
        for i in spec:
            if i[2] <= nage <= i[3]:
                result.append(i)

def ovz(ans):                           # фильтр по овз
    if len(ans) == 0:
        ans=["да", "нет"]
    ans = list(set(ans))
    global kol
    kol+=1
    for i in spec:
        for r in ans:
            try:
                if i.index(r):
                    result.append(i)
            except: pass

def ochn(anss):                         # фильтр по очное\заочное
    if len(anss) == 0:
        anss=["очное", "заочное"]
    anss = list(set(anss))
    global kol
    kol+=1
    for i in spec:
        for r in anss:
            try:
                if i.index(r):
                    result.append(i)
            except: pass

def location(loc):                      # фильтр по локации
    if len(loc) == 0:
        loc=[i[6] for i in spec]
    loc = list(set(loc))
    global kol
    kol+=1
    for i in spec:
        for r in loc:
            try:
                if i.index(r):
                    result.append(i)
            except: pass

def price(price):                       # фильтр по цене
    if len(price) == 0:
        price = -1
    price = int(price)
    global kol
    kol+=1
    if price == -1:
        for i in spec:
            result.append(i)
    else:
        for i in spec:
            if i[7] <= price:
                result.append(i)

specs(input().split())
age(input())
ovz(input().split())
ochn(input().split())
location(input().split())
price(input())

for i in spec:
    if result.count(i) == kol:
        print(i)