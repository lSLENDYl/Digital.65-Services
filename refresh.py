from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def refresh():
    # Функция 1
    # Функция 2

app = QApplication([])
win = QWidget()

button = QPushButton('Обновить')
button.setStyleSheet('background-color : red')

layout = QVBoxLayout()
layout.addWidget(button, alignment=Qt.AlignCenter)
win.setLayout(layout)

button.clicked.connect(refresh)

win.show()
app.exec_()
