from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox,QButtonGroup
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 400)
window.setWindowTitle('card')

btn_ok = QPushButton('Ответить')
lbl_gues = QLabel('Вопрос?')
radio_group = QButtonGroup()
groubox_answer = QGroupBox('Варианты')
rbtn1 = QRadioButton('1')
rbtn2 = QRadioButton('2')
rbtn3 = QRadioButton('3')
rbtn4 = QRadioButton('4')

radio_group.addButton(rbtn1)
radio_group.addButton(rbtn2)
radio_group.addButton(rbtn3)
radio_group.addButton(rbtn4)

def show_question():
    grbox_result.hide()
    groubox_answer.show()
    btn_ok.setText('Ответить')
    btn_ok.clicked.connect(show_result)
    radio_group.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    radio_group.setExclusive(True)

def show_result():
    groubox_answer.hide()
    grbox_result.show()
    btn_ok.setText('Сдедующий вопрос')
    btn_ok.clicked.connect(show_question)

btn_ok.clicked.connect(show_result)
grbox_result = QGroupBox('резлультат')
lbl_r_a = QLabel('парвильно')
v_line_result = QVBoxLayout()
v_line_result.addWidget(lbl_r_a, alignment=Qt.AlignCenter)
grbox_result.setLayout(v_line_result)

h_line_ans = QHBoxLayout()
v_line_ans1 = QVBoxLayout()
v_line_ans2 = QVBoxLayout()

v_line_ans1.addWidget(rbtn1)
v_line_ans1.addWidget(rbtn2)
v_line_ans2.addWidget(rbtn3)
v_line_ans2.addWidget(rbtn4)
h_line_ans.addLayout(v_line_ans1)
h_line_ans.addLayout(v_line_ans2)

groubox_answer.setLayout(h_line_ans)

v_line_main = QVBoxLayout()
h_line_main_1 = QHBoxLayout()
h_line_main_2 = QHBoxLayout()
h_line_main_3 = QHBoxLayout()

h_line_main_1.addWidget(lbl_gues, alignment=Qt.AlignCenter)
h_line_main_2.addWidget(groubox_answer)
h_line_main_2.addWidget(grbox_result)
h_line_main_3.addStretch(1)
h_line_main_3.addWidget(btn_ok, stretch=2)
h_line_main_3.addStretch(1)

v_line_main.addLayout(h_line_main_1, stretch=2)
v_line_main.addLayout(h_line_main_2, stretch=8)
v_line_main.addStretch(1)
v_line_main.addLayout(h_line_main_3, stretch=1)
v_line_main.addStretch(1)

grbox_result.hide()
window.setLayout(v_line_main)
window.show()
app.exec()
