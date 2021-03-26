import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import *
from register import RegisterWindow
from login import LoginWindow

def goToRegister(stacked_widget, registerPage):
    stacked_widget.setCurrentIndex(1)
    registerPage.initUI()

def goToLogin(stacked_widget, loginPage):
    stacked_widget.setCurrentIndex(2)
    loginPage.start()


def goToHome(stacked_widget):
    stacked_widget.setCurrentIndex(0)



# Main Page
class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "App"
        self.InitUI()
        self.height = 525
        self.width = 750

    def InitUI(self):
        self.setAutoFillBackground(True)
        self.setWindowTitle("iAttend App")
        self.setStyleSheet("QMainWindow {\n"
                           "     background-color: #006699;\n}\n"
                           "QPushButton {\n"
                           "     background-color: #b3e6ff; border: 1px solid black;\n"
                           "     border-radius: 5px; font: bold 16px;\n }\n"
                           "QTextBrowser {\n"
                           "     background-color: #b3e6ff;; border: 1px solid black;\n"
                           "     border-radius: 5px; font-size: 10pt; font-weight:400; font-style:normal;  \n" "}")

        # Logo
        self.logo = QLabel(self)
        self.pixmap = QPixmap('logo/iAttend.png')
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(200, 200)
        self.logo.move(270, 10)

        # Message Box
        self.message = QtWidgets.QTextBrowser(self)
        self.message.resize(500, 90)
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
    homeWindow = HomeWindow()
    registerWindow = RegisterWindow()
    loginWindow = LoginWindow()
    widget = QStackedWidget()
    widget.addWidget(homeWindow)
    widget.addWidget(registerWindow)
    widget.addWidget(loginWindow)
    # set up the navigation buttons
    homeWindow.register.clicked.connect(lambda: goToRegister(widget, registerWindow))
    homeWindow.login.clicked.connect(lambda: goToLogin(widget, loginWindow))

    widget.setFixedSize(750, 525)
    widget.show()
    sys.exit(app.exec_())






