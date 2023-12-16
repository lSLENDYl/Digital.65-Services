from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, \
    QLineEdit, QComboBox, QDialog
from PyQt5.QtGui import QPixmap


def dialog_win_1():
    dialog = QDialog()
    dialog.resize(300, 150)
    dialog_layout = QVBoxLayout()
    dialog.setWindowTitle('Увлечения')
    dialog_line = QLineEdit()
    ready_button = QPushButton('Принять')
    dialog_layout.addWidget(dialog_line, alignment=Qt.AlignCenter)
    dialog_layout.addWidget(ready_button, alignment=Qt.AlignCenter)
    dialog.setLayout(dialog_layout)

    def change_text():
        criter_button_1.setText(dialog_line.text())
        dialog.close()

    ready_button.clicked.connect(change_text)
    dialog.show()
    dialog.exec_()


def dialog_win_2():
    dialog = QDialog()
    dialog.resize(300, 150)
    dialog_layout = QVBoxLayout()
    dialog.setWindowTitle('Возраст')
    dialog_line = QLineEdit()
    ready_button = QPushButton('Принять')
    dialog_layout.addWidget(dialog_line, alignment=Qt.AlignCenter)
    dialog_layout.addWidget(ready_button, alignment=Qt.AlignCenter)
    dialog.setLayout(dialog_layout)

    def change_text():
        criter_button_2.setText(dialog_line.text())
        dialog.close()

    ready_button.clicked.connect(change_text)
    dialog.show()
    dialog.exec_()


def dialog_win_3():
    dialog = QDialog()
    dialog.resize(300, 150)
    dialog_layout = QVBoxLayout()
    dialog.setWindowTitle('Цена')
    dialog_line = QLineEdit()
    ready_button = QPushButton('Принять')
    dialog_layout.addWidget(dialog_line, alignment=Qt.AlignCenter)
    dialog_layout.addWidget(ready_button, alignment=Qt.AlignCenter)
    dialog.setLayout(dialog_layout)

    def change_text():
        criter_button_6.setText(dialog_line.text())
        dialog.close()

    ready_button.clicked.connect(change_text)
    dialog.show()
    dialog.exec_()


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('')

picture = QLabel('*Здесь будет картинка*')
poisk_line = QLineEdit()
poisk_line.setFixedWidth(550)
poisk_button = QPushButton('Поиск')
criter_button_1 = QPushButton('Увлечения')
criter_button_2 = QPushButton('Возраст')
criter_button_3 = QComboBox()
criter_button_3.addItem('ОВЗ')
criter_button_3.addItem('Да')
criter_button_3.addItem('Нет')
criter_button_4 = QComboBox()
criter_button_4.addItem('Форма обучения')
criter_button_4.addItem('Очная')
criter_button_4.addItem('Очно-заочная')
criter_button_4.addItem('Заочная')
criter_button_6 = QPushButton('Цена')
use_filter_button = QPushButton('Применить фильтры')

main_layout = QVBoxLayout()
poisk_layout = QHBoxLayout()
criter_layout = QHBoxLayout()
poisk_layout.addWidget(poisk_line, alignment=Qt.AlignRight)
poisk_layout.addWidget(poisk_button, alignment=Qt.AlignLeft)
criter_layout.addWidget(criter_button_1, alignment=Qt.AlignCenter)
criter_layout.addWidget(criter_button_2, alignment=Qt.AlignCenter)
criter_layout.addWidget(criter_button_3, alignment=Qt.AlignCenter)
criter_layout.addWidget(criter_button_4, alignment=Qt.AlignCenter)
criter_layout.addWidget(criter_button_6, alignment=Qt.AlignCenter)
criter_layout.addWidget(use_filter_button, alignment=Qt.AlignCenter)
main_layout.addWidget(picture, alignment=Qt.AlignCenter)
main_layout.addLayout(poisk_layout)
main_layout.addLayout(criter_layout)

criter_button_1.clicked.connect(dialog_win_1)
criter_button_2.clicked.connect(dialog_win_2)
criter_button_6.clicked.connect(dialog_win_3)

# label = QLabel(main_win)
# pixmap = QPixmap(r'C:\Users\nikit\Desktop\картинки для сайта\Пикча 16 на 9.jpeg')
# label.setPixmap(pixmap)

main_win.setLayout(main_layout)
main_win.show()
app.exec_()
