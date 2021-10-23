import os
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox

import db
import Login

Form = uic.loadUiType(os.path.join(os.getcwd(), 'Register.ui'))[0]


class register(Form, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.RegisterButton.clicked.connect(self.register)
        self.back.clicked.connect(self.Back)

    def register(self):
        self.name = self.Name.text()
        self.phone = self.Phone.text()
        self.username = self.NameText.text()
        self.password = self.PassText.text()
        hasVal = True
        print(self.name)
        if self.name is '':
            hasVal = False
        elif not self.name.isalpha():
            hasVal = False
        elif self.phone is '':
            hasVal = False
        elif not self.phone.isdigit():
            hasVal = False
        elif self.username is '':
            hasVal = False
        elif self.username.isdigit():
            hasVal = False
        elif self.password is '':
            hasVal = False
        if not hasVal:
            QMessageBox.critical(self, "ERROR", "Invalid values\nplease try again")
        if hasVal:
            db1 = db.DBHandler()
            e = db1.insertUsers(self.name, self.phone, self.username, self.password)
            if e:
                QMessageBox.critical(self, "ERROR", "This username/phone number exists\nplease try again")
                self.close()
                self.window = QDialog()
                self.ui = register()
                self.ui.setModal(True)
                self.ui.exec()
            else:
                self.close()
                self.window = QDialog()
                self.ui = Login.login()
                self.ui.setModal(True)
                self.ui.exec()

    def Back(self):
        self.close()
        self.window = QDialog()
        self.ui = Login.login()
        self.ui.setModal(True)
        self.ui.exec()
