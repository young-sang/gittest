import sys
from PyQt5.QtWidgets import *

print(sys.argv)
app = QApplication(sys.argv)
label = QLabel("Hello PyQt")
label.show()
app.exec_()