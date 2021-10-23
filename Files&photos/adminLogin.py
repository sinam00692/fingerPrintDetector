import os
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox
from ipywidgets import Password

import db
import adminMainApp
import FisrtPage

Form = uic.loadUiType(os.path.join(os.getcwd(), 'adminLogin.ui'))[0]


class login(Form, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.login)
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
            if self.username != 'Admin':
                QMessageBox.critical(self, "ERROR", "Username or password is incorrect")
            elif self.password != 'admin':
                QMessageBox.critical(self, "ERROR", "Username or password is incorrect")
            else:
                self.close()
                self.window = QDialog()
                self.ui = adminMainApp.MainApp()
                self.ui.setModal(True)
                self.ui.exec()

    def Back(self):
        self.close()
        self.window = QDialog()
        self.ui = FisrtPage.fisrtpage()
        self.ui.setModal(True)
        self.ui.exec()
