import sys
from PyQt5.QtWidgets import QApplication
import db
import FisrtPage

app = QApplication(sys.argv)
db.DBHandler()
w = FisrtPage.fisrtpage()
w.show()
sys.exit(app.exec())
