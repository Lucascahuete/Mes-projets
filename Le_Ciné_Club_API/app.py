from PySide2 import QtWidgets, QtCore
from movie import Movie, get_movies

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.le_nameOfFilm = QtWidgets.QLineEdit()
        self.btn_addFilm = QtWidgets.QPushButton("Ajouter un film")
        self.lst_liste = QtWidgets.QListWidget()
        self.lst_liste.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_deleteFilm = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.le_nameOfFilm)
        self.layout.addWidget(self.btn_addFilm)
        self.layout.addWidget(self.lst_liste)
        self.layout.addWidget(self.btn_deleteFilm)

    def setup_connections(self):
        self.btn_addFilm.clicked.connect(self.add_movie)
        self.btn_deleteFilm.clicked.connect(self.remove_movie)
        self.le_nameOfFilm.returnPressed.connect(self.add_movie)

    def populate_movies(self):
        for i in get_movies():
            lw_item = QtWidgets.QListWidgetItem(i.titre)
            lw_item.setData(QtCore.Qt.UserRole, i)
            self.lst_liste.addItem(lw_item)

    def add_movie(self):
        titre = self.le_nameOfFilm.text()
        if not titre:
            return False
        m = Movie(titre)
        if m.add_to_movies():
            lw_item = QtWidgets.QListWidgetItem(m.titre)
            lw_item.setData(QtCore.Qt.UserRole, m.titre)
            self.lst_liste.addItem(lw_item)
        
        self.le_nameOfFilm.setText("")

    def remove_movie(self):
        for selected_item in self.lst_liste.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lst_liste.takeItem(self.lst_liste.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()

