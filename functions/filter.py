
def filter(base):
    hek = 0
    result = []
    param = []
    print('1 - спец, 2 - возраст, 3 - ОВЗ, 4- очно - заочно, 5- локация, 6 - цена')
    param1 = input().split()
    param1.sort()
    if param1[0] == '2':
        l = int(input())
        for k in base:
            num1, num2 = base[k][1].split('-')
            print(num1, num2)
            if int(num1) <= l <= int(num2):
                    result.append(k)
    else:
        for i in param1:
            if i == '1':
                print('введите спец')
                param.append(input())
            if i == '2':
                print('введите возраст')
                l = int(input())
                for k in base:
                    num1, num2 = base[k][1].split('-')
                    if int(num1) <= l <= int(num2):
                        hek+=1
            if i == '3':
                print('Есть ли ОВЗ')
                ao = input()
                if ao.lower() == 'да':
                    param.append('да')
                else:
                    param.append('нет')
            if i == '4':
                print('Очно или заочно?')
                param.append(input())
        print(param)
        if hek != 0:
            for k in base:
                if set(param).issubset(base[k]):
                    result.append(k)
    return list(result)
