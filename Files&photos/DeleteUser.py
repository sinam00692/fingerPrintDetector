import os

from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
import adminMainApp
import db

Form = uic.loadUiType(os.path.join(os.getcwd(), 'Deleteuser.ui'))[0]


class delete(Form, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Delete.clicked.connect(self.delete)
        self.Back.clicked.connect(self.back)
        self.username = None

    def getusername(self, user):
        self.username = user

    def back(self):
        self.close()
        self.window = QDialog()
        self.ui = adminMainApp.MainApp()
        self.ui.setModal(True)
        self.ui.exec()

    def delete(self):
        self.username = self.NameTextLogin.text()
        hasVal = True
        if self.username is '':
            hasVal = False
        if hasVal:
            db1 = db.DBHandler()
            exist = db1.deleteUser(self.username)
            print(exist)
            if not exist:
                QMessageBox.critical(self, "ERROR", "This username doesn't exist!")
            else:
                self.close()
                self.window = QDialog()
                self.ui = adminMainApp.MainApp()
                self.ui.setModal(True)
                self.ui.exec()

