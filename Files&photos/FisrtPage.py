import os

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
import Login
import adminLogin

Form = uic.loadUiType(os.path.join(os.getcwd(), 'FirstPage.ui'))[0]


class fisrtpage(Form, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.simpleUser.clicked.connect(self.simple)
        self.Admin.clicked.connect(self.admin)

    def simple(self):
        self.close()
        self.window = QDialog()
        self.ui = Login.login()
        self.ui.setModal(True)
        self.ui.exec()

    def admin(self):
        self.close()
        self.window = QDialog()
        self.ui = adminLogin.login()
        self.ui.setModal(True)
        self.ui.exec()
