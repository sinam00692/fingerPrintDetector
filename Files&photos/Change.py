import os
import sqlite3

from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox
from PyQt5 import uic
import MainApp
import db

Form = uic.loadUiType(os.path.join(os.getcwd(), 'Change.ui'))[0]


class change(Form, QDialog):
    def __init__(self, username, password):
        super().__init__()
        self.setupUi(self)
        self.Submit.clicked.connect(self.info)
        self.OldPass.setEchoMode(QLineEdit.Password)
        self.NewPass.setEchoMode(QLineEdit.Password)
        self.NewPass2.setEchoMode(QLineEdit.Password)
        self.password = password
        self.username = username
        self.conn = sqlite3.connect('db.sqlite')

    def info(self):
        if self.OldPass.text() != self.password:
            QMessageBox.critical(self, "ERROR", "Password is incorrect")
        elif self.NewPass.text() != self.NewPass2.text():
            QMessageBox.critical(self, "ERROR", "Please retype new password correctly")
        else:
            db1 = db.DBHandler()
            user_id = db1.findId(self.username, self.password)
            self.password = self.NewPass.text()
            db1.update(user_id[0], self.password)
            self.close()
            self.window = QDialog()
            self.ui = MainApp.MainApp(self.username, self.password)
            self.ui.setModal(True)
            self.ui.exec()
