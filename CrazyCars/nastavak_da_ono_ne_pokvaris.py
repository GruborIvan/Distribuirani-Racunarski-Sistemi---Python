import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QCursor, QPainter, QPen, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore
from GameSetup import Car


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon('toy-red-car-isolated-on-white-background-donald-erickson.jpg'))
        self.setStyleSheet("background-color:white")
        # self.setStyleSheet("background-color:Blue")
        self.center()
        self.mainScreen()
        # self.opt_w=Option()
        # self.setCentralWidget(self.opt_w)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mainScreen(self):
        #start_button = QPushButton("Start game!!!")
        #exit_button = QPushButton("Exit")
        #vbox = QVBoxLayout()
        #vbox.addWidget(start_button)
        #vbox.addWidget(exit_button)
        #hbox = QHBoxLayout()
        #hbox.addLayout(vbox)
        #self.setLayout(hbox)

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(0, 110, 561, 361))
        label.setMinimumSize(QtCore.QSize(550, 0))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("rsz_lightning-mcqueen-cars.jpg"))
        label.setObjectName("label")

        label_2 = QtWidgets.QLabel(self)
        label_2.setGeometry(QtCore.QRect(70, 40, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(36)
        label_2.setFont(font)
        label_2.setTextFormat(QtCore.Qt.AutoText)
        label_2.setObjectName("label_2")
        label_2.setText("Welcome to CRAZY CARS!!!")

        label_3 = QtWidgets.QLabel(self)
        label_3.setGeometry(QtCore.QRect(490, 30, 51, 71))
        label_3.setText("")
        label_3.setPixmap(QtGui.QPixmap("output-onlinepngtools (4).png"))
        label_3.setObjectName("label_3")

        label_4 = QtWidgets.QLabel(self)
        label_4.setGeometry(QtCore.QRect(10, 30, 51, 71))
        label_4.setText("")
        label_4.setPixmap(QtGui.QPixmap("D:/Downloads/output-onlinepngtools (4).png"))
        label_4.setObjectName("label_4")

        playButton = QtWidgets.QPushButton(self)
        playButton.setGeometry(QtCore.QRect(160, 500, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        playButton.setFont(font)
        playButton.setStyleSheet("background-color:orange")

        exitButton = QtWidgets.QPushButton(self)
        exitButton.setGeometry(QtCore.QRect(160, 600, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        exitButton.setFont(font)
        exitButton.setStyleSheet("background-color:orange")

        playButton.setText("START")
        exitButton.setText("QUIT")

        exitButton.clicked.connect(QCoreApplication.instance().quit)
        playButton.clicked.connect(self.playScreen)

    def playScreen(self):
        self.w = PlayWindow()
        self.w.show()
        self.hide()


class PlayWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon('toy-red-car-isolated-on-white-background-donald-erickson.jpg'))
        self.setStyleSheet("background-color:lightblue")

        self.center()
        self.mainScreen()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mainScreen(self):
        exit_button = QPushButton("")
        exit_button.setIcon(QIcon('pause3.png'))
        exit_button.setStyleSheet("border: 0px solid black")
        exit_button.setToolTip("Pause game")
        exit_button.setFixedWidth(50)
        exit_button.setFixedHeight(50)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(exit_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.paintEvent(self)

        self.setCar()

        exit_button.clicked.connect(self.pauseScreen)

    def pauseScreen(self):
        self.wp = PauseWindow()
        self.wp.show()
        self.hide()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangle(qp)
        self.drawLines(qp)
        qp.end()

    def drawRectangle(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor("Black")
        qp.setPen(col)
        qp.setBrush(QBrush(Qt.gray, Qt.SolidPattern))
        qp.drawRect(75, 0, 400, 700)

    def drawLines(self, qp):
        pen = QPen(Qt.white, 2, Qt.SolidLine)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(155, 0, 155, 700)
        qp.drawLine(235, 0, 235, 700)
        qp.drawLine(315, 0, 315, 700)
        qp.drawLine(395, 0, 395, 700)

    def setCar(self):
        label = QLabel(self)
        pixmap = QPixmap('rsz_car1Ok.png')

        label.setPixmap(pixmap)
        label.setGeometry(250, 600, 50, 100)


class PauseWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Pause Crazy Cars')
        self.setWindowIcon(QIcon('toy-red-car-isolated-on-white-background-donald-erickson.jpg'))
        self.setStyleSheet("background-color:grey")

        self.center()

        self.setScreen()

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setScreen(self):

        font = QtGui.QFont()
        font.setPointSize(24)

        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: white")
        exitButton = QtWidgets.QPushButton(self)
        exitButton.setGeometry(QtCore.QRect(160, 500, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        exitButton.setFont(font)
        exitButton.setStyleSheet("background-color:orange")
        exitButton.setObjectName("exitButton")
        exitButton.setText("LEAVE GAME")

        resumeButton = QtWidgets.QPushButton(self)
        resumeButton.setGeometry(QtCore.QRect(160, 600, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        resumeButton.setFont(font)
        resumeButton.setStyleSheet("background-color:orange")
        resumeButton.setObjectName("resumeButton")
        resumeButton.setText("RESUME GAME")

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(0, 110, 531, 361))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("rsz_pausepic.png"))
        label.setObjectName("label")

        label_2 = QtWidgets.QLabel(self)
        label_2.setGeometry(QtCore.QRect(190, 30, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(36)
        label_2.setFont(font)
        label_2.setObjectName("label_2")
        label_2.setText("Game paused!")

        exitButton.clicked.connect(self.mainScreen)
        resumeButton.clicked.connect(self.playScreen)

    def mainScreen(self):
        self.wm = MainWindow()
        self.wm.show()
        self.hide()

    def playScreen(self):
        self.wp = PlayWindow()
        self.wp.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    prozor = MainWindow()

    sys.exit(app.exec_())
