import random
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QSizePolicy, \
    QComboBox, QLineEdit, QListWidget
from pathlib import Path
import main


class MenuWindow (QWidget):
    def __init__(self):
        super().__init__()

        stacked_widget.setWindowTitle("ConfessBouff")
        stacked_widget.setFixedSize(500, 300)
        self.setFixedSize(500, 300)
        modify_style()

        self.main_layout = QVBoxLayout(self)
        self.titre = QLabel("ConfessBouff")
        self.titre.setAlignment(QtCore.Qt.AlignHCenter)
        self.titre.setMinimumSize(50, 50)

        self.main_layout.addWidget(self.titre)

        self.second_layout = QHBoxLayout(self)
        self.btn_player = QPushButton("Je me conffesse")
        self.btn_player.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_quiz = QPushButton("Quizz")
        self.btn_quiz.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.second_layout.addWidget(self.btn_player)
        self.second_layout.addWidget(self.btn_quiz)

        self.main_layout.addLayout(self.second_layout)

        self.btn_player.clicked.connect(self.next_window)
        self.btn_quiz.clicked.connect(self.quizz_window)

    def next_window(self):
        stacked_widget.setCurrentWidget(window2)

    def quizz_window(self):
        stacked_widget.setCurrentWidget(window3)


def modify_style():
    qss_file = Path.cwd() / "data" / "style.qss"
    with open(qss_file, "r") as f:
        stacked_widget.setStyleSheet(f.read())


class Confesse_Window (QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 300)
        modify_style()

        self.main_layout = QVBoxLayout(self)
        self.titre = QLabel("Je me confesse")
        self.titre.setAlignment(QtCore.Qt.AlignHCenter)
        self.first_line_layout = QHBoxLayout()
        self.btn_back = QPushButton("<--")
        self.cbb_choice_player = QComboBox()
        self.le_new_player = QLineEdit("Nouveau Joueur")
        self.btn_add_player = QPushButton("+")
        self.lst_confesse = QListWidget()
        self.le_new_fact = QLineEdit("Raconte moi ...")
        self.btn_add_fact = QPushButton("ajouter")
        self.btn_delete_fact = QPushButton("supprimer")
        self.last_line_layout = QHBoxLayout()

        self.main_layout.addWidget(self.titre)
        self.main_layout.addLayout(self.first_line_layout)
        self.first_line_layout.addWidget(self.btn_back)
        self.first_line_layout.addWidget(self.le_new_player)
        self.first_line_layout.addWidget(self.btn_add_player)
        self.main_layout.addWidget(self.cbb_choice_player)
        self.main_layout.addWidget(self.lst_confesse)
        self.main_layout.addWidget(self.le_new_fact)
        self.main_layout.addLayout(self.last_line_layout)
        self.last_line_layout.addWidget(self.btn_add_fact)
        self.last_line_layout.addWidget(self.btn_delete_fact)

        self.btn_back.clicked.connect(self.main_Window)
        self.btn_add_player.clicked.connect(self.add_new_player)
        self.cbb_choice_player.currentIndexChanged.connect(self.list_confesse)
        self.btn_add_fact.clicked.connect(self.add_new_fact)
        self.btn_delete_fact.clicked.connect(self.delete_fact)

        for i in main.get_users():
            self.cbb_choice_player.addItem(str(i))

    def add_new_player(self):
        if self.le_new_player.text() != "" " ":
            player = main.User(self.le_new_player.text())
            self.cbb_choice_player.clear()
            for i in main.get_users():
                self.cbb_choice_player.addItem(str(i))
            self.cbb_choice_player.setCurrentText(player.name)
        else:
            pass

    def list_confesse(self):
        player = main.User(self.cbb_choice_player.currentText())
        self.lst_confesse.clear()
        try:
            for i in player._get_facts():
                self.lst_confesse.addItem(i)
        except:
            print("liste vide")

    def add_new_fact(self):
        if self.le_new_fact.text() != "":
            player = main.User(self.cbb_choice_player.currentText())
            player.write_fact(self.le_new_fact.text())
            self.le_new_fact.clear()
            self.list_confesse()

    def delete_fact(self):
        player = main.User(self.cbb_choice_player.currentText())
        for selected_item in self.lst_confesse.selectedItems():
            fact = selected_item.text()
            player.remove_fact(fact)
        self.list_confesse()



    def main_Window(self):
        stacked_widget.setCurrentWidget(window1)

class QuizzWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quizz")
        self.setFixedSize(500, 300)
        self.resize(500, 300)
        self.score = 0


        self.main_layout = QVBoxLayout(self)
        self.titre = QLabel("Quizz")
        self.titre.setAlignment(QtCore.Qt.AlignHCenter)
        self.btn_back = QPushButton("<--")
        self.btn_back.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_back.setFixedSize(QtCore.QSize(100, 50))
        self.btn_new_question = QPushButton("Nouvelle question")
        self.btn_new_question.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_new_question.setFixedSize(QtCore.QSize(200, 50))
        self.first_line_layout = QHBoxLayout()
        self.ql_score = QLabel(str(self.score))
        self.question = QLabel()
        self.btn_answer1 = QPushButton("Premier réponse")
        self.btn_answer2 = QPushButton("Deuxieme réponse")
        self.btn_answer3 = QPushButton("Troisieme réponse")
        self.btn_answer4 = QPushButton("Quatrieme réponse")
        self.last_line_layout = QHBoxLayout()

        self.main_layout.addWidget(self.titre)
        self.main_layout.addLayout(self.first_line_layout)
        self.first_line_layout.addWidget(self.btn_back)
        self.first_line_layout.addWidget(self.ql_score)
        self.first_line_layout.addWidget(self.btn_new_question)
        self.main_layout.addWidget(self.question)
        self.main_layout.addLayout(self.last_line_layout)
        self.last_line_layout.addWidget(self.btn_answer1)
        self.last_line_layout.addWidget(self.btn_answer2)
        self.last_line_layout.addWidget(self.btn_answer3)
        self.last_line_layout.addWidget(self.btn_answer4)

        self.btn_back.clicked.connect(self.main_Window)
        self.btn_new_question.clicked.connect(self.new_question)
        self.btn_answer1.clicked.connect(self.reponce)
        self.btn_answer2.clicked.connect(self.reponce)
        self.btn_answer3.clicked.connect(self.reponce)
        self.btn_answer4.clicked.connect(self.reponce)

    def main_Window(self):
        stacked_widget.setCurrentWidget(window1)

    def new_question(self):
        self.reset_style_button()
        self.enable_button()
        self.good_answer = main.Quiz.random_user(self)
        question = main.Quiz.random_fact(self, self.good_answer)
        self.question.setText(question)
        self.bad_answer = main.get_users()
        self.bad_answer.remove(self.good_answer)
        choice = []
        choice.append(self.good_answer)
        i = 1
        while i < 4:
            user_select = random.choice(self.bad_answer)
            self.bad_answer.remove(user_select)
            choice.append(user_select)
            i = i+1

        random.shuffle(choice)
        self.answer = [self.btn_answer1, self.btn_answer2, self.btn_answer3, self.btn_answer4]
        for i, j in zip(self.answer, choice):
            i.setText(str(j))

    def reponce(self):
        button = self.sender()
        if button.text() == self.good_answer:
            button.setStyleSheet("background-color: #008000")
            self.score += 1
            self.ql_score.setText(str(self.score))
            self.disable_button()

        else:
            button.setStyleSheet("background-color: #FF0000")
            self.disable_button()
            for i in self.answer:
                if i.text() == self.good_answer:
                    i.setStyleSheet("background-color: #008000")
                else:
                    pass

    def reset_style_button(self):
        self.btn_answer1.setStyleSheet("background-color: #FFFF00")
        self.btn_answer2.setStyleSheet("background-color: #FFFF00")
        self.btn_answer3.setStyleSheet("background-color: #FFFF00")
        self.btn_answer4.setStyleSheet("background-color: #FFFF00")

    def enable_button(self):
        self.btn_answer1.setEnabled(True)
        self.btn_answer2.setEnabled(True)
        self.btn_answer3.setEnabled(True)
        self.btn_answer4.setEnabled(True)

    def disable_button(self):
        self.btn_answer1.setEnabled(False)
        self.btn_answer2.setEnabled(False)
        self.btn_answer3.setEnabled(False)
        self.btn_answer4.setEnabled(False)












app = QApplication()
stacked_widget = QtWidgets.QStackedWidget()
window1 = MenuWindow()
window2 = Confesse_Window()
window3 = QuizzWindow()
stacked_widget.addWidget(window1)
stacked_widget.addWidget(window2)
stacked_widget.addWidget(window3)
stacked_widget.setCurrentWidget(window1)
stacked_widget.show()
app.exec()