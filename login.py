
import sys
import time

import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets, QtCore


import main
import os

class WorkerThread(QtCore.QObject):

    def __init__(self, updatefunc):
        super().__init__()
        self.update = updatefunc

    @QtCore.pyqtSlot()
    def run(self):
        while True:
            # Long running task ...
            self.update()
            time.sleep(1)

# Register Page
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.initUI()
        self.setStyleSheet("background : #006699;")
        self.height = 525
        self.width = 750

    def initUI(self):
        self.image_frame = QLabel(self)
        self.image_frame.setAlignment(Qt.AlignCenter)
        self.image_frame.resize(750, 525)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_frame)
        self.setLayout(self.layout)

        main.getImages('img/images')
        main.encodings = main.getEncodings(main.images)


    def start(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.worker = WorkerThread(lambda: self.display())
        self.workerThread = QtCore.QThread()
        self.workerThread.started.connect(self.worker.run)
        self.worker.moveToThread(self.workerThread)
        self.workerThread.start()
        

    def display(self):
        
       # if not self.cap.isOpened():
            #self.cap.open(0)
        ret, cam_img = self.cap.read()
        uiImage = main.face_recog(cam_img)
        # number of bytes per line (total size of image / height in px)
        bytesWidth = uiImage.size * uiImage.itemsize / uiImage.shape[0]
        self.image = QtGui.QImage(uiImage.data, 750, 525, bytesWidth, QtGui.QImage.Format_BGR888)
        self.image_frame.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win2 = LoginWindow()
    sys.exit(app.exec_())