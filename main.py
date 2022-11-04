from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QButtonGroup
import sys
from random import shuffle

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
    check_answer()
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

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = [
    Question('Какая функция преобразовывает число в строку', 'str()', 'int()', 'srt()', 'pit()')
    Question('Что такое блок-схема?', 'это графическое представление программы', 'это логическое представление программы', 'это схема программы', 'это функция')
    Question('Что такое алгоритм?', 'это конечный набор шагов, которые решают задачу', 'это действия программы', 'это код', 'это набор шагов, которые решают задачу')
    Question('Что такое переменные?', 'это именованные ячейки памяти', 'это ячейки', 'это именованные строки программы', 'я не знаю что такое переменные')
    Question('что такое список в python?', 'это упорядоченные изменяемые наборы объектов', 'это место хранения объектов', 'это словарь', 'это упорядоченные наборы объектов')
    Question('Какой функцией преобразовать число в строку', 'str()', 'int()', 'srt()', 'pit()')
    Question('Функция print() нужна', 'для печати на экран того, что находятся внутри скобок' 'для определения типа данных', 'для передачи в программу данных от пользователя', 'для преобразования строки в число')
    Question('Словарь в языке Python', 'хранит коллекцию элементов', 'место хранения объектов', 'список', 'упорядоченные наборы объектов'
]
v_line_main.addLayout(h_line_main_1, stretch=2)
v_line_main.addLayout(h_line_main_2, stretch=8)
v_line_main.addStretch(1)
v_line_main.addLayout(h_line_main_3, stretch=1)
v_line_main.addStretch(1)

answer = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q):
    lbl_gues.setText(q.question)
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)

def check_answer():
    if answer[0].isChecked():
        lbl_r_a.setText('поздравляю ты прав')
        grbox_result.setStyleSheet('QGroupBox {border: 2px solid #69f369; border-radius: 8%;}')
    else:
        lbl_r_a.setText('ты не прав. \n Правильный ответ: '+ answer[0].text())
        grbox_result.setStyleSheet('QGroupBox {border: 2px solid #ee4433; border-radius: 8%;}')

ask(question_list[0])

grbox_result.hide()
window.setLayout(v_line_main)
window.show()
app.exec()
