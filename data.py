import json

with open(r"C:\Users\User\Desktop\dopobr\data.json", "r", encoding="utf-8") as f:
    data_l = f.read()

data = json.loads(data_l)

base = []

for i in data["data"]:
    base.append([i["name"], i["ovz"]])
print(base)