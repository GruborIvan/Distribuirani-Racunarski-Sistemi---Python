import sys

from PyQt5.QtCore import QCoreApplication, QRect, QSize, QThread, QProcess
from PyQt5.QtGui import QIcon, QCursor, QPainter, QPen, QBrush, QColor, QPixmap, QImage, QPalette
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore

from Avatar import Avatar
from Avatar import AvatarFactory
from Scores import Scores
from ScoresMulti import ScoresMulti
from ScoresMulti import ScoresChampSF2
from ScoresMulti import ScoresChampF
from Coin import Coin
from Coin import CoinFactory
from AllObjectsFactory import ObjectFactory
from AllObjectsFactory import TimerObjects
from AllObjectsFactory import TimerObjectsMulti
from AllObjectsFactory import TimerObjectsChampSF1
from AllObjectsFactory import TimerObjectsChampSF2
from AllObjectsFactory import TimerObjectsChampF


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))
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

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(0, 110, 561, 361))
        label.setMinimumSize(QtCore.QSize(550, 0))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_lightning-mcqueen-cars.jpg"))
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
        label_3.setPixmap(QtGui.QPixmap("Slike/output-onlinepngtools (4).png"))
        label_3.setObjectName("label_3")

        label_4 = QtWidgets.QLabel(self)
        label_4.setGeometry(QtCore.QRect(10, 30, 51, 71))
        label_4.setText("")
        label_4.setPixmap(QtGui.QPixmap("Slike/output-onlinepngtools (4).png"))
        label_4.setObjectName("label_4")

        playButton = QtWidgets.QPushButton(self)
        playButton.setGeometry(QtCore.QRect(290, 500, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        playButton.setFont(font)
        playButton.setStyleSheet("background-color:orange")

        #dugme za multiplejer
        playButtonMulti = QtWidgets.QPushButton(self)
        playButtonMulti.setGeometry(QtCore.QRect(50, 500, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        playButtonMulti.setFont(font)
        playButtonMulti.setStyleSheet("background-color:orange")

        # dugme za turnir
        playButtonChamp = QtWidgets.QPushButton(self)
        playButtonChamp.setGeometry(QtCore.QRect(50, 600, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        playButtonChamp.setFont(font)
        playButtonChamp.setStyleSheet("background-color:orange")


        exitButton = QtWidgets.QPushButton(self)
        exitButton.setGeometry(QtCore.QRect(290, 600, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        exitButton.setFont(font)
        exitButton.setStyleSheet("background-color:orange")

        playButton.setText("Single player")
        playButtonMulti.setText("Multiplayer")
        playButtonChamp.setText("Championship")
        exitButton.setText("QUIT")

        exitButton.clicked.connect(QCoreApplication.instance().quit)
        playButton.clicked.connect(self.uputstvoScreen)
        playButtonMulti.clicked.connect(self.uputstvoScreenMulti)
        playButtonChamp.clicked.connect(self.uputstvoScreenChamp)

    def playScreen(self):
        self.w = PlayWindow()
        self.w.show()
        self.hide()

    def uputstvoScreen(self):
        self.w = UputstvoWindow()
        self.w.show()
        self.hide()

    def uputstvoScreenMulti(self):
        self.w = UputstvoWindowMulti()
        self.w.show()
        self.hide()

    def uputstvoScreenChamp(self):
        self.w = UputstvoWindowChampSF1()
        self.w.show()
        self.hide()

    def playScreenMulti(self):
        self.w = PlayWindowMulti()
        self.w.show()
        self.hide()

class PlayWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))

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
        exit_button.setIcon(QIcon('Slike/pause3.png'))
        exit_button.setStyleSheet("border: 0px solid black")
        exit_button.setToolTip("Pause game")
        exit_button.setFixedWidth(50)
        exit_button.setFixedHeight(50)
        oImage = QImage("Slike/put2.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(exit_button)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


        self.process=QProcess(self)
        self.process.started.connect(lambda: self.paintEvent(self))
        self.process.start()
        #self.paintEvent(self)


        #scores
        self.score = Scores(self)

        #avatars
        self.a = Avatar(self)


        self.tO= TimerObjects(self,self.a, self.score)

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.tO.generateObjectWithTimer)
        self.thread.start()


        #Pokretanje sa tajmerom-Prvi nacin
        #self.tO.generateObjectWithTimer()

        #Pokretanje drugi nacin
        #self.tO.pokreniThread()

        #Pokretanje treci nacin
        #self.tO.generateObjectWithoutTimer()

        exit_button.clicked.connect(self.pauseScreen)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            self.a.moveMeLeft()
            #self.score.changeScore()
            #self.score.loseLife()
        if event.key() == QtCore.Qt.Key_D:
            self.a.moveMeRight()
            #self.score.changeLevel()



    def pauseScreen(self):
        self.wp = PauseWindow()
        self.wp.show()
        self.hide()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(155, 0, 155, 700)
        qp.drawLine(235, 0, 235, 700)
        qp.drawLine(315, 0, 315, 700)
        qp.drawLine(395, 0, 395, 700)


class PlayWindowMulti(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))

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
        exit_button.setIcon(QIcon('Slike/pause3.png'))
        exit_button.setStyleSheet("border: 0px solid black")
        exit_button.setToolTip("Pause game")
        exit_button.setFixedWidth(50)
        exit_button.setFixedHeight(50)
        oImage = QImage("Slike/put2.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(exit_button)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


        self.process=QProcess(self)
        self.process.started.connect(lambda: self.paintEvent(self))
        self.process.start()
        #self.paintEvent(self)


        #scores
        self.score = ScoresMulti(self)

        #avatars
        self.a1 = Avatar(self,170)
        #self.a1.x=150
        self.a2 = Avatar(self,330)
        #self.a2.x=350

        self.tO= TimerObjectsMulti(self,self.a1,self.a2, self.score)

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.tO.generateObjectWithTimer)
        self.thread.start()


        #Pokretanje sa tajmerom-Prvi nacin. bez Thread-a
        #self.tO.generateObjectWithTimer()

        exit_button.clicked.connect(self.pauseScreen)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            self.a1.moveMeLeft()
        if event.key() == QtCore.Qt.Key_D:
            self.a1.moveMeRight()
        if event.key() == QtCore.Qt.Key_J:
            self.a2.moveMeLeft()
        if event.key() == QtCore.Qt.Key_L:
            self.a2.moveMeRight()



    def pauseScreen(self):
        self.wp = PauseWindow()
        self.wp.show()
        self.hide()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(155, 0, 155, 700)
        qp.drawLine(235, 0, 235, 700)
        qp.drawLine(315, 0, 315, 700)
        qp.drawLine(395, 0, 395, 700)


class PauseWindow(QWidget):

    def __init__(self, rez:int):
        super().__init__()
        self.rez=rez
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Pause Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))
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
        exitButton.setGeometry(QtCore.QRect(160, 580, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        exitButton.setFont(font)
        exitButton.setStyleSheet("background-color:orange")
        exitButton.setObjectName("exitButton")
        exitButton.setText("HOME PAGE ")




        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(0, 110, 531, 361))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_pausepic.png"))
        label.setObjectName("label")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(180, 500, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Your score: "+self.rez.__str__())


        label_2 = QtWidgets.QLabel(self)
        label_2.setGeometry(QtCore.QRect(190, 30, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(36)
        label_2.setFont(font)
        label_2.setObjectName("label_2")
        label_2.setText("Game over!")

        exitButton.clicked.connect(self.mainScreen)


    def mainScreen(self):
        self.wm = MainWindow()
        self.wm.show()
        self.hide()

    def playScreen(self):
        self.wp = PlayWindow()
        self.wp.show()
        self.hide()


class PauseWindowMulti(QWidget):

    def __init__(self,p1:str,p2:str):
        super().__init__()

        self.p1=p1
        self.p2=p2
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Pause Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))
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

        #novo
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 200, 80, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Winner:")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 250, 80, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(self.p1)

        self.labelGorep2 = QtWidgets.QLabel(self)
        self.labelGorep2.setGeometry(QtCore.QRect(10, 320, 80, 30))
        self.labelGorep2.setFont(font)
        self.labelGorep2.setText("Loser:")

        self.labelGorep2 = QtWidgets.QLabel(self)
        self.labelGorep2.setGeometry(QtCore.QRect(10, 370, 80, 30))
        self.labelGorep2.setFont(font)
        self.labelGorep2.setText(self.p2)



        font = QtGui.QFont()
        font.setPointSize(24)

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(110, 200, 350, 240))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_1rsz_pausepic.png"))
        label.setObjectName("label")

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
        exitButton.setText("HOME PAGE ")






        label_2 = QtWidgets.QLabel(self)
        label_2.setGeometry(QtCore.QRect(190, 30, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(36)
        label_2.setFont(font)
        label_2.setObjectName("label_2")
        label_2.setText("Game over!")

        exitButton.clicked.connect(self.mainScreen)


    def mainScreen(self):
        self.wm = MainWindow()
        self.wm.show()
        self.hide()

    def playScreen(self):
        self.wp = PlayWindow()
        self.wp.show()
        self.hide()


class PauseWindowChampSF1(QWidget):

    def __init__(self,p1:str):
        super().__init__()

        self.p1=p1

        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Pause Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))
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

        #novo
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 200, 80, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Winner:")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 250, 80, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(self.p1)




        font = QtGui.QFont()
        font.setPointSize(24)

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(110, 200, 350, 240))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_1rsz_pausepic.png"))
        label.setObjectName("label")

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
        exitButton.setText("NEXT MATCH")


        label_2 = QtWidgets.QLabel(self)
        label_2.setGeometry(QtCore.QRect(190, 30, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(36)
        label_2.setFont(font)
        label_2.setObjectName("label_2")
        label_2.setText("Game over!")

        exitButton.clicked.connect(self.playWindowChamp)

    def playWindowChamp(self):
        self.wm = UputstvoWindowChampSF2(self.p1)
        self.wm.show()
        self.hide()

class PauseWindowChampSF2(QWidget):

    def __init__(self,p1:str,p2:str=""):
        super().__init__()

        self.p1=p1
        self.p2=p2
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Pause Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))
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

        #novo
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 200, 80, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Winner:")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 250, 80, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(self.p1)




        font = QtGui.QFont()
        font.setPointSize(24)

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(110, 200, 350, 240))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_1rsz_pausepic.png"))
        label.setObjectName("label")

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
        exitButton.setText("NEXT MATCH")


        label_2 = QtWidgets.QLabel(self)
        label_2.setGeometry(QtCore.QRect(190, 30, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(36)
        label_2.setFont(font)
        label_2.setObjectName("label_2")
        label_2.setText("Game over!")

        exitButton.clicked.connect(self.playWindowChamp)

    def playWindowChamp(self):
        self.wm = UputstvoWindowChampF(self.p2,self.p1)
        self.wm.show()
        self.hide()


class PauseWindowChampF(QWidget):

    def __init__(self,p1:str):
        super().__init__()

        self.p1=p1

        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Pause Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))
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

        #novo
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 200, 140, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("CHAMPION IS:")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 250, 80, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(self.p1)




        font = QtGui.QFont()
        font.setPointSize(24)

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(140, 200, 350, 240))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_1rsz_pausepic.png"))
        label.setObjectName("label")

        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: white")
        exitButton = QtWidgets.QPushButton(self)
        exitButton.setGeometry(QtCore.QRect(190, 550, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        exitButton.setFont(font)
        exitButton.setStyleSheet("background-color:orange")
        exitButton.setObjectName("exitButton")
        exitButton.setText("HOME PAGE")


        label_2 = QtWidgets.QLabel(self)
        label_2.setGeometry(QtCore.QRect(190, 30, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(36)
        label_2.setFont(font)
        label_2.setObjectName("label_2")
        label_2.setText("Game over!")

        label_22 = QtWidgets.QLabel(self)
        label_22.setGeometry(QtCore.QRect(120, 450, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        label_22.setFont(font)
        label_22.setObjectName("label_2")
        label_22.setText("AWARD: 1 extra point on exam!")

        exitButton.clicked.connect(self.playWindowChamp)

    def playWindowChamp(self):
        self.wm = MainWindow()
        self.wm.show()
        self.hide()


class UputstvoWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
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
        exitButton.setGeometry(QtCore.QRect(160, 480, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        exitButton.setFont(font)
        exitButton.setStyleSheet("background-color:orange")
        exitButton.setText("GOT IT, PLAY")


        exitButton.clicked.connect(self.playScreen)

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(220, 40, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("RULES:")

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(170, 110,25, 25))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_mrs.png"))
        label.setObjectName("label")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(200, 110, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(":    + Life")

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(170,180, 25, 25))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_1coin.png"))
        label.setObjectName("label")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(200, 180, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(":    Score + 100")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(149, 250, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Crash:")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(253, 250, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("-  Life")


    def playScreen(self):
        self.wm = PlayWindow()
        self.wm.show()
        self.hide()


class UputstvoWindowMulti(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
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
        exitButton.setGeometry(QtCore.QRect(160, 480, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        exitButton.setFont(font)
        exitButton.setStyleSheet("background-color:orange")
        exitButton.setText("GOT IT, PLAY")

        exitButton.clicked.connect(self.playScreen)

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(220, 40, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("RULES:")

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(170, 110, 25, 25))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_mrs.png"))
        label.setObjectName("label")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(200, 110, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(":    + Life")


        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(149, 160, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Crash:")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(253, 160, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("-  Life")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(63, 220, 450, 100))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Winner is the one who stays alive longer!")

    def playScreen(self):
        self.wm = PlayWindowMulti()
        self.wm.show()
        self.hide()


class UputstvoWindowChampSF2(QWidget):
    def __init__(self, pob1:str=""):
        super().__init__()
        self.pob1=pob1
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
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
        exitButton.setGeometry(QtCore.QRect(160, 480, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        exitButton.setFont(font)
        exitButton.setStyleSheet("background-color:orange")
        exitButton.setText("GOT IT, PLAY")

        exitButton.clicked.connect(self.playScreen)

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(220, 40, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("RULES:")

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(170, 110, 25, 25))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_mrs.png"))
        label.setObjectName("label")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(200, 110, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(":    + Life")


        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(149, 160, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Crash:")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(253, 160, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("-  Life")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(63, 220, 450, 150))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Winner is the one who stays alive longer!")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(63, 320, 450, 100))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Player 3 vs Player 4")

    def playScreen(self):
        self.wm = PlayWindowChampSF2(self.pob1)
        self.wm.show()
        self.hide()


class UputstvoWindowChampF(QWidget):
    def __init__(self,pob1:str="", pob2:str=""):
        super().__init__()
        self.pob1=pob1
        self.pob2=pob2
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
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
        exitButton.setGeometry(QtCore.QRect(160, 480, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        exitButton.setFont(font)
        exitButton.setStyleSheet("background-color:orange")
        exitButton.setText("GOT IT, PLAY")

        exitButton.clicked.connect(self.playScreen)

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(220, 40, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("RULES:")

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(170, 110, 25, 25))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_mrs.png"))
        label.setObjectName("label")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(200, 110, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(":    + Life")


        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(149, 160, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Crash:")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(253, 160, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("-  Life")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(63, 220, 450, 150))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Winner is the one who stays alive longer!")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(63, 320, 450, 100))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(self.pob1+" vs "+self.pob2)

    def playScreen(self):
        self.wm = PlayWindowChampF(self.pob1,self.pob2)
        self.wm.show()
        self.hide()


class UputstvoWindowChampSF1(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
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
        exitButton.setGeometry(QtCore.QRect(160, 480, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(24)
        exitButton.setFont(font)
        exitButton.setStyleSheet("background-color:orange")
        exitButton.setText("GOT IT, PLAY")

        exitButton.clicked.connect(self.playScreen)

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(220, 40, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("RULES:")

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(170, 110, 25, 25))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Slike/rsz_mrs.png"))
        label.setObjectName("label")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(200, 110, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(":    + Life")


        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(149, 160, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Crash:")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(253, 160, 200, 30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("-  Life")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(63, 220, 450, 150))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Winner is the one who stays alive longer!")

        self.labelGorep1 = QtWidgets.QLabel(self)
        self.labelGorep1.setGeometry(QtCore.QRect(63, 320, 450, 100))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Player 1 vs Player 2")

    def playScreen(self):
        self.wm = PlayWindowChampSF1()
        self.wm.show()
        self.hide()


class PlayWindowChampSF1(QWidget):
    def __init__(self, pob:str=""):
        super().__init__()
        self.pobednik=pob
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))

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
        exit_button.setIcon(QIcon('Slike/pause3.png'))
        exit_button.setStyleSheet("border: 0px solid black")
        exit_button.setToolTip("Pause game")
        exit_button.setFixedWidth(50)
        exit_button.setFixedHeight(50)
        oImage = QImage("Slike/put2.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(exit_button)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


        self.process=QProcess(self)
        self.process.started.connect(lambda: self.paintEvent(self))
        self.process.start()
        #self.paintEvent(self)


        #scores
        self.score = ScoresMulti(self)

        #avatars
        self.a1 = Avatar(self,170)
        #self.a1.x=150
        self.a2 = Avatar(self,330)
        #self.a2.x=350

        self.tO= TimerObjectsChampSF1(self,self.a1,self.a2, self.score)

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.tO.generateObjectWithTimer)
        self.thread.start()


        #Pokretanje sa tajmerom-Prvi nacin. bez Thread-a
        #self.tO.generateObjectWithTimer()

        exit_button.clicked.connect(self.pauseScreen)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            self.a1.moveMeLeft()
        if event.key() == QtCore.Qt.Key_D:
            self.a1.moveMeRight()
        if event.key() == QtCore.Qt.Key_J:
            self.a2.moveMeLeft()
        if event.key() == QtCore.Qt.Key_L:
            self.a2.moveMeRight()



    def pauseScreen(self):
        self.wp = PauseWindow()
        self.wp.show()
        self.hide()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(155, 0, 155, 700)
        qp.drawLine(235, 0, 235, 700)
        qp.drawLine(315, 0, 315, 700)
        qp.drawLine(395, 0, 395, 700)


class PlayWindowChampSF2(QWidget):
    def __init__(self, pob:str=""):
        super().__init__()
        self.pobednik=pob
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))

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
        exit_button.setIcon(QIcon('Slike/pause3.png'))
        exit_button.setStyleSheet("border: 0px solid black")
        exit_button.setToolTip("Pause game")
        exit_button.setFixedWidth(50)
        exit_button.setFixedHeight(50)
        oImage = QImage("Slike/put2.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(exit_button)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


        self.process=QProcess(self)
        self.process.started.connect(lambda: self.paintEvent(self))
        self.process.start()
        #self.paintEvent(self)


        #scores
        self.score = ScoresChampSF2(self)

        #avatars
        self.a1 = Avatar(self,170)
        #self.a1.x=150
        self.a2 = Avatar(self,330)
        #self.a2.x=350

        self.tO= TimerObjectsChampSF2(self,self.a1,self.a2, self.score, self.pobednik)

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.tO.generateObjectWithTimer)
        self.thread.start()


        #Pokretanje sa tajmerom-Prvi nacin. bez Thread-a
        #self.tO.generateObjectWithTimer()

        exit_button.clicked.connect(self.pauseScreen)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            self.a1.moveMeLeft()
        if event.key() == QtCore.Qt.Key_D:
            self.a1.moveMeRight()
        if event.key() == QtCore.Qt.Key_J:
            self.a2.moveMeLeft()
        if event.key() == QtCore.Qt.Key_L:
            self.a2.moveMeRight()



    def pauseScreen(self):
        self.wp = PauseWindow()
        self.wp.show()
        self.hide()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(155, 0, 155, 700)
        qp.drawLine(235, 0, 235, 700)
        qp.drawLine(315, 0, 315, 700)
        qp.drawLine(395, 0, 395, 700)


class PlayWindowChampF(QWidget):
    def __init__(self, pob1:str="",pob2:str=""):
        super().__init__()
        self.pobednik1=pob1
        self.pobednik2=pob2
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon('Slike/toy-red-car-isolated-on-white-background-donald-erickson.jpg'))

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
        exit_button.setIcon(QIcon('Slike/pause3.png'))
        exit_button.setStyleSheet("border: 0px solid black")
        exit_button.setToolTip("Pause game")
        exit_button.setFixedWidth(50)
        exit_button.setFixedHeight(50)
        oImage = QImage("Slike/put2.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(exit_button)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


        self.process=QProcess(self)
        self.process.started.connect(lambda: self.paintEvent(self))
        self.process.start()
        #self.paintEvent(self)


        #scores
        self.score = ScoresChampF(self, self.pobednik1, self.pobednik2)

        #avatars
        self.a1 = Avatar(self,170)
        #self.a1.x=150
        self.a2 = Avatar(self,330)
        #self.a2.x=350

        self.tO= TimerObjectsChampF(self,self.a1,self.a2, self.score, self.pobednik1,self.pobednik2)

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.tO.generateObjectWithTimer)
        self.thread.start()


        #Pokretanje sa tajmerom-Prvi nacin. bez Thread-a
        #self.tO.generateObjectWithTimer()

        exit_button.clicked.connect(self.pauseScreen)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_A:
            self.a1.moveMeLeft()
        if event.key() == QtCore.Qt.Key_D:
            self.a1.moveMeRight()
        if event.key() == QtCore.Qt.Key_J:
            self.a2.moveMeLeft()
        if event.key() == QtCore.Qt.Key_L:
            self.a2.moveMeRight()



    def pauseScreen(self):
        self.wp = PauseWindow()
        self.wp.show()
        self.hide()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(155, 0, 155, 700)
        qp.drawLine(235, 0, 235, 700)
        qp.drawLine(315, 0, 315, 700)
        qp.drawLine(395, 0, 395, 700)

