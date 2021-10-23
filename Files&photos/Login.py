import os
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox

import db
import MainApp
import Register
import FisrtPage

Form = uic.loadUiType(os.path.join(os.getcwd(), 'Login.ui'))[0]


class login(Form, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.login)
        self.RegisterButtonM.clicked.connect(self.Register)
        self.back.clicked.connect(self.Back)
        self.PassTextLogin.setEchoMode(QLineEdit.Password)
        self.username = None
        self.password = None

    def login(self):
        self.username = self.NameTextLogin.text()
        self.password = self.PassTextLogin.text()
        print(self.username)
        hasVal = True
        if self.username is '':
            hasVal = False
        elif self.password is '':
            hasVal = False
        if hasVal:
            db1 = db.DBHandler()
            user_Id = db1.findId(self.username)
            if user_Id is None:
                QMessageBox.critical(self, "ERROR", "Username or password is incorrect")
            if user_Id is not None:
                user_Id = int(user_Id[0])
                db1.readUser(user_Id)
                self.close()
                self.window = QDialog()
                self.ui = MainApp.MainApp(self.username, self.password)
                self.ui.setModal(True)
                self.ui.exec()

    def Register(self):
        self.close()
        self.window = QDialog()
        self.ui = Register.register()
        self.ui.setModal(True)
        self.ui.exec()

    def Back(self):
        self.close()
        self.window = QDialog()
        self.ui = FisrtPage.fisrtpage()
        self.ui.setModal(True)
        self.ui.exec()
