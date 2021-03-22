
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *
#from main import face_recog
import os

# Register Page
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle("Register")
        self.initUI()
        self.setStyleSheet("background : #006699;")

   # def openLogin(self):
  #      face_recog()

    def initUI(self):
        # text box
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('ENTER YOUR NAME :')
        self.nameLabel.resize(215,40)
        self.nameLabel.setFont(QFont('Times', 13))
        self.nameLabel.move(270,80)
        self.textbox = QLineEdit(self)
        self.textbox.resize(250, 40)
        self.textbox.move(500, 80)

        # log in button
        self.login_button = QPushButton(self)
        self.login_button.setText('LOG IN')
        self.login_button.move(445, 735)
        self.login_button.resize(100, 40)
        self.login_button.setStyleSheet("background-color: #b3e6ff;")
        #self.login_button.click.connect(self,openLogin)

        #shadow effect for the label
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)

        self.nameLabel.setGraphicsEffect(shadow)
        self.textbox.setStyleSheet("background-color: #b3e6ff;"
                                   "border-style: outset;"
                                   "border-width: 2px;"
                                   "border-color: beige;")


        capture_button = QAction("CAPTURE", self)
        capture_button.triggered.connect(self.click_photo)
        capture_button.setFont(QFont('Times', 10))

        # camera code
        # finds available camera
        self.available_cameras = QCameraInfo.availableCameras()
        if not self.available_cameras:
            capture_button.setDisabled(True)
            self.viewfinder = QLabel()
            self.viewfinder.setText("No cameras were found")
            self.viewfinder.setAlignment(Qt.AlignCenter)
            self.viewfinder.show()
            self.setCentralWidget(self.viewfinder)
            #sys.exit()
        else:
            #change image path
            self.save_path = "img/images"
            self.viewfinder = QCameraViewfinder()

            self.viewfinder.show()

            self.setCentralWidget(self.viewfinder)
            self.select_camera(0)

        # creating a tool bar
        toolbar = QToolBar("Camera Tool Bar")
        self.addToolBar(toolbar)
        toolbar.addAction(capture_button)

        toolbar.setStyleSheet("background :#FCDBA9;")
        toolbar.setFixedHeight(60)

        camera_selector = QComboBox()

        camera_selector.addItems([camera.description()
                                  for camera in self.available_cameras])

        camera_selector.currentIndexChanged.connect(self.select_camera)

        toolbar.addWidget(camera_selector)
        self.show()

    def select_camera(self, i):

        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.start()

        self.capture = QCameraImageCapture(self.camera)
        self.current_camera_name = self.available_cameras[i].description()

    def click_photo(self):

        self.capture.capture(os.path.join(self.save_path, "%s.jpg" % (self.textbox.text())))
        self.textbox.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win2 = MyWindow()
    sys.exit(app.exec_())





