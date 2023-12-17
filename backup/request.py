import urllib.request, json

def request():
    with urllib.request.urlopen("https://api.pfdo.ru/v2/main-page/search/es-programs?sort=&per-page=123&operator=31&expand=program_nok_rating,duration_string") as url:
        data = json.load(url)
        # print(data)
        with open(r'C:\res\data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    # 48    
def for_matrix():
    f = open(r'C:\res\data.txt','w', encoding='utf-8')
    f.write('')

    with open(r"C:\res\data.json", "r", encoding="utf-8") as f:
        data_l = f.read()

        data = json.loads(data_l)

        base = []
        matrix = []
        k = 1
    for i in data["data"]:
        print(k)
        k+=1
        base.append([i["name"], i['direction']['name'], int(i['age_min'])//12, int(i['age_max'])//12, i['ovz'], i['form'], i['duration_string'],])
    for ii in base:
        f = open(r'C:\res\data.txt','a', encoding='utf-8')
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
        f.write('\n')
        f.close
request()
for_matrix()
# with open(r'D:\System\Destktop\hakaton\data.txt','r', encoding='utf-8') as f:
#             start = f.readlines()
#             for i in start:
#                 timemas = i.split('<=>')
#                 spec.append([timemas[0],timemas[1],timemas[2],timemas[3],timemas[4],timemas[5],timemas[6][:-2]])