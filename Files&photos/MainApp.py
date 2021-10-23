import os

from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt5 import uic
import Change
import FisrtPage
import db

Form = uic.loadUiType(os.path.join(os.getcwd(), 'MainApp.ui'))[0]


class MainApp(Form, QDialog):
    def __init__(self, username, password):
        super().__init__()
        self.setupUi(self)
        self.addFinger.clicked.connect(self.add)
        self.infoChange.clicked.connect(self.change)
        self.Quit.clicked.connect(self.quit)
        self.username = username
        self.password = password

    def getusername(self, user):
        self.username = user

    def add(self):
        path = QFileDialog.getOpenFileName(self, 'Open file',
                                           'c:\\', 'Image files (*.jpg *.png)')
        db1 = db.DBHandler()
        userID = db1.findId(self.username)
        exist = db1.insertFinger(userID[0], path[0])
        if exist:
            QMessageBox.critical(self, "ERROR", "You have added your fingerprint before")

    def change(self):
        self.close()
        self.window = QDialog()
        self.ui = Change.change(self.username, self.password)
        self.ui.setModal(True)
        self.ui.exec()

    def quit(self):
        self.close()
        self.window = QDialog()
        self.ui = FisrtPage.fisrtpage()
        self.ui.setModal(True)
        self.ui.exec()
