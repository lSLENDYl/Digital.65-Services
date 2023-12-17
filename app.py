from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, \
    QLineEdit, QComboBox, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap
import urllib.request, json


def use_filter():
    form = [1, 2, 3]
    ovz = [0, 1]
    nazvanie = criter_button_1.text()
    category = criter_button_2.text()
    vozrast = criter_button_3.text()
    if criter_button_4.currentText() == 'Да':
        ovz = [1]
    elif criter_button_4.currentText() == 'Нет':
        ovz = [0]
    if criter_button_5.currentText() == 'Очная':
        form = [1]
    elif criter_button_5.currentText() == 'Очно-заочная':
        form = [2]
    elif criter_button_5.currentText() == 'Заочная':
        form = [3]
    specs(category.lower().split())
    age(vozrast)
    ovz1(ovz)
    ochn(form)
    res41 = []
    for i in spec:
        if result.count(i) == kol:
            res41.append(i)
    res41 = [i[0] for i in res41]
    print_info = QMessageBox()
    print_info.setWindowTitle('Фильтры')
    print_info.setText('вот что удалось найти: ' + '\n' + str(res41))
    print_info.exec_()

spec = []

with open(r"C:\Users\User\Desktop\dopobr\data.json", "r", encoding="utf-8") as f:
    data_l = f.read()

data = json.loads(data_l)

for i in data["data"]:
    spec.append([i["name"], i["direction"]["name"].lower(), int(i["age_min"]) // 12, int(i["age_max"]) // 12, i["ovz"], i["form"]])

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
                if i.index(r) == 1:
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

def ovz1(ans):                           # фильтр по овз
    if len(ans) == 0:
        ans=[0, 1]
    ans = list(set(ans))
    ans = [int(i) for i in ans]
    global kol
    kol+=1
    for i in spec:
        for r in ans:
            try:
                if i.index(r) == 4:
                    result.append(i)
            except: pass

def ochn(anss):                         # фильтр по очное\заочное
    if len(anss) == 0:
        anss=[1, 2, 3]
    anss = list(set(anss))
    anss = [int(i) for i in anss]
    global kol
    kol+=1
    for i in spec:
        for r in anss:
            try:
                if i.index(r) == 5:
                    result.append(i)
            except: pass

# def location(loc):                      # фильтр по локации
#     if len(loc) == 0:
#         loc=[i[6] for i in spec]
#     loc = list(set(loc))
#     global kol
#     kol+=1
#     for i in spec:
#         for r in loc:
#             try:
#                 if i.index(r):
#                     result.append(i)
#             except: pass

# location(input().split())

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('')
main_win.setGeometry(400, 400, 800, 200)

picture = QLabel('*Здесь будет картинка*')
poisk_line = QLineEdit()
poisk_line.setFixedWidth(550)
poisk_button = QPushButton('Поиск')
criter_name_1 = QLabel('Название')
criter_name_2 = QLabel('Категория')
criter_name_3 = QLabel('Возраст')
criter_name_4 = QLabel('ОВЗ')
criter_name_5 = QLabel('Форма обучения')
criter_button_1 = QLineEdit()
criter_button_2 = QLineEdit()
criter_button_3 = QLineEdit()
criter_button_4 = QComboBox()
criter_button_4.addItem('')
criter_button_4.addItem('Да')
criter_button_4.addItem('Нет')
criter_button_5 = QComboBox()
criter_button_5.addItem('')
criter_button_5.addItem('Очная')
criter_button_5.addItem('Очно-заочная')
criter_button_5.addItem('Заочная')
use_filter_button = QPushButton('Применить фильтры')

main_layout = QVBoxLayout()
poisk_layout = QHBoxLayout()
criter_layout_H = QHBoxLayout()
criter_layout_V1 = QVBoxLayout()
criter_layout_V2 = QVBoxLayout()
criter_layout_V3 = QVBoxLayout()
criter_layout_V4 = QVBoxLayout()
criter_layout_V5 = QVBoxLayout()
poisk_layout.addWidget(poisk_line, alignment=Qt.AlignRight)
poisk_layout.addWidget(poisk_button, alignment=Qt.AlignLeft)
criter_layout_V1.addWidget(criter_name_1, alignment=Qt.AlignCenter)
criter_layout_V1.addWidget(criter_button_1, alignment=Qt.AlignCenter)
criter_layout_V2.addWidget(criter_name_2, alignment=Qt.AlignCenter)
criter_layout_V2.addWidget(criter_button_2, alignment=Qt.AlignCenter)
criter_layout_V3.addWidget(criter_name_3, alignment=Qt.AlignCenter)
criter_layout_V3.addWidget(criter_button_3, alignment=Qt.AlignCenter)
criter_layout_V4.addWidget(criter_name_4, alignment=Qt.AlignCenter)
criter_layout_V4.addWidget(criter_button_4, alignment=Qt.AlignCenter)
criter_layout_V5.addWidget(criter_name_5, alignment=Qt.AlignCenter)
criter_layout_V5.addWidget(criter_button_5, alignment=Qt.AlignCenter)
criter_layout_H.addLayout(criter_layout_V1)
criter_layout_H.addLayout(criter_layout_V2)
criter_layout_H.addLayout(criter_layout_V3)
criter_layout_H.addLayout(criter_layout_V4)
criter_layout_H.addLayout(criter_layout_V5)
main_layout.addWidget(picture, alignment=Qt.AlignCenter)
main_layout.addLayout(poisk_layout)
main_layout.addLayout(criter_layout_H)
main_layout.addWidget(use_filter_button, alignment=Qt.AlignCenter)

use_filter_button.clicked.connect(use_filter)

main_win.setLayout(main_layout)
main_win.show()
app.exec_()