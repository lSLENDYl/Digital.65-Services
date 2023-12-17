from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, \
    QLineEdit, QComboBox, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap
import urllib.request, json


def use_filter():
    nazvanie = criter_button_1.text()
    category = criter_button_2.text()
    vozrast = criter_button_3.text()
    ovz = criter_button_4.currentText()
    edu_form = criter_button_5.currentText()
    info_massage_text = nazvanie + '\n' + category + '\n' + vozrast + '\n' + ovz + '\n' + edu_form
    print_info = QMessageBox()
    print_info.setWindowTitle('Фильтры')
    print_info.setText('Вы выбрали: ' + '\n' + info_massage_text)
    print_info.exec_()


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

# def request():
#     with urllib.request.urlopen(
#             "https://api.pfdo.ru/v2/main-page/search/es-programs?sort=&per-page=123&operator=31&expand=program_nok_rating,duration_string") as url:
#         data = json.load(url)
#         # print(data)
#         with open(r'C:\Users\nikit\Desktop\Хакатон\data.json', 'w', encoding='utf-8') as f:
#             json.dump(data, f, ensure_ascii=False)
#
#     # 48
#
#
# def for_matrix():
#     f = open(r'C:\Users\nikit\Desktop\Хакатон\data.txt', 'w', encoding='utf-8')
#     f.write('')
#
#     with open(r"D:\System\Destktop\hakaton\data.json", "r", encoding="utf-8") as f:
#         data_l = f.read()
#
#         data = json.loads(data_l)
#
#         base = []
#         matrix = []
#         k = 1
#     for i in data["data"]:
#         print(k)
#         k += 1
#         base.append(
#             [i["name"], i['direction']['name'], int(i['age_min']) // 12, int(i['age_max']) // 12, i['ovz'], i['form'],
#              i['duration_string'], ])
#     for ii in base:
#         f = open(r'D:\System\Destktop\hakaton\data.txt', 'a', encoding='utf-8')
#         f.write(ii[0])
#         f.write('<=>')
#         f.write(ii[1])
#         f.write('<=>')
#         f.write(str(ii[2]))
#         f.write('<=>')
#         f.write(str(ii[3]))
#         f.write('<=>')
#         f.write(str(ii[4]))
#         f.write('<=>')
#         f.write(str(ii[5]))
#         f.write('<=>')
#         f.write(str(ii[6]))
#         f.write('\n')
#         f.close()


# label = QLabel(main_win)
# pixmap = QPixmap(r'C:\Users\nikit\Desktop\картинки для сайта\Пикча 16 на 9.jpeg')
# label.setPixmap(pixmap)
# request()
# for_matrix()
# spec = []
# with open(r'D:\System\Destktop\hakaton\data.txt','r', encoding='utf-8') as f:
#             start = f.readlines()
#             for i in start:
#                 timemas = i.split('<=>')
#                 spec.append([timemas[0],timemas[1],timemas[2],timemas[3],timemas[4],timemas[5],timemas[6][:-2]])
main_win.setLayout(main_layout)
main_win.show()
app.exec_()
