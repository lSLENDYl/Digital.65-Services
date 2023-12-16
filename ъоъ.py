import urllib.request, json
    # def format(base):
    #     count = 0
    #     for i in range(len(base)):
    #         base['data'+str(i)] = base.pop(list(base.keys())[i])
    #         print(i)
def request():
    with urllib.request.urlopen("https://api.pfdo.ru/v2/main-page/search/es-programs?sort=&per-page=123&operator=31&expand=program_nok_rating,duration_string") as url:
        data = json.load(url)
        # print(data)
        with open(r'D:\System\Destktop\hakaton\data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    # 48    
def for_matrix():
    f = open(r'D:\System\Destktop\hakaton\data.txt','w', encoding='utf-8')
    f.write('')

    # timemat = [[]]
    # count = 0
    # while True:
    #     f = open(r'D:\System\Destktop\hakaton\data.txt', 'a')
    #     strurl  = 'https://api.pfdo.ru/v2/main-page/search/es-programs?page='+str(count)+'&per-page=24&operator=31&expand=program_nok_rating,duration_string'
    #     with urllib.request.urlopen(strurl) as url:
    #         data = json.load(url)
    #         if data['data'] != []:
    #             timemat[count][0] = data['data']['short_name']
    #         else:break
    # print(timemat)
    with open(r"D:\System\Destktop\hakaton\data.json", "r", encoding="utf-8") as f:
        data_l = f.read()

        data = json.loads(data_l)

        base = []
        matrix = []
        k = 1
    for i in data["data"]:
        print(k)
        k+=1
        base.append([i["name"], i['direction']['name'], int(i['age_min'])//12, int(i['age_max'])//12, i['ovz'], i['form'], i['address']['lat'], i['address']['lon'], i['duration_string']])
    for ii in base:
        f = open(r'D:\System\Destktop\hakaton\data.txt','a', encoding='utf-8')
        f.write(ii[0])
        f.write('<=>')
        f.write(ii[1])
        f.write('<=>')
        f.write(str(ii[2]))
        f.write('<=>')
        f.write(str(ii[3]))
        f.write('<=>')
        f.write(str(ii[4]))
        f.write('<=>')
        f.write(str(ii[5]))
        f.write('<=>')
        f.write(str(ii[6]))
        f.write('<=>')
        f.write(ii[7])
        f.write('\n')
        f.close
request()
for_matrix()