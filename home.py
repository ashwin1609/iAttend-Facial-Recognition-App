from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import *
from register import RegisterWindow

def goToRegister(stacked_widget):
    stacked_widget.setCurrentIndex(1)
    stacked_widget.show()

def goToLogin(stacked_widget):
    stacked_widget.setCurrentIndex(2)
    stacked_widget.show()

def goToHome(stacked_widget):
    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()

# Main Page
class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "App"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitUI()

    def InitUI(self):
        self.resize(750, 525)
        self.setAutoFillBackground(True)
        self.setWindowTitle("iAttend App")
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
    widget = QStackedWidget()
    widget.addWidget(homeWindow)
    widget.addWidget(registerWindow)

    # set up the navigation buttons
    homeWindow.register.clicked.connect(lambda: widget.setCurrentIndex(1))

    widget.resize(750, 525)
    widget.show()
    sys.exit(app.exec_())




