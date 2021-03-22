from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import *

# Main Page
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(750, 525)
        self.setAutoFillBackground(True)
        self.setStyleSheet("QMainWindow {\n"
"     background-color: #006699; border: 1px solid black;\n"
"     border-radius: 5px;\n" "}\n"
"QPushButton {\n"
"     background-color: #b3e6ff; border: 1px solid black;\n"
"     border-radius: 5px; font: bold 16px;\n }\n"
"QTextBrowser {\n"
"     background-color: #b3e6ff;; border: 1px solid black;\n"
"     border-radius: 5px; font-size: 10pt; font-weight:400; font-style:normal;  \n" "}")
        # Logo
        self.logo = QLabel(self)
        self.pixmap = QPixmap('C:/Users/ashwi/PycharmProjects/AI Project/3.png')
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(200, 200)
        self.logo.move(270, 10)

        # Message Box
        self.message = QtWidgets.QTextBrowser(self)
        self.message.resize(500, 120)
        self.message.move(130, 220)
        self.message.setText("Welcome to iAttend, a facial recognition based attendance system created by group 23. "
                             "Please click the register button, add your name and click the capture button to take a picture and save your name."
                             " Once the registration is completed, click the login button to take your attendance.")
        # Register Button
        self.register = QPushButton(self)
        self.register.resize(271, 71)
        self.register.move(90, 380)
        self.register.setText("REGISTER")

        # Log In button
        self.login = QPushButton(self)
        self.login.resize(271, 71)
        self.login.move(400, 380)
        self.login.setText("LOG IN")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win1 = MainWindow()
    win1.show()
    sys.exit(app.exec_())




