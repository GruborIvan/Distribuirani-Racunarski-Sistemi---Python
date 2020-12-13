import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QCursor, QPainter, QPen, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QLabel
from PyQt5.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)

        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon('car.png'))
        #self.setStyleSheet("background-color:Blue")

        self.center()
        self.mainScreen()

        #self.opt_w=Option()
        #self.setCentralWidget(self.opt_w)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mainScreen(self):
        start_button = QPushButton("Start game!!!")
        exit_button = QPushButton("Exit")

        vbox = QVBoxLayout()
        vbox.addWidget(start_button)
        vbox.addWidget(exit_button)
        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        self.setLayout(hbox)

        exit_button.clicked.connect(QCoreApplication.instance().quit)

        start_button.clicked.connect(self.playScreen)

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
        self.setWindowIcon(QIcon('car.png'))
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

        exit_button.clicked.connect(self.playScreen)


    def playScreen(self):
        self.w = MainWindow()
        self.w.show()
        self.hide()

    def paintEvent(self,e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangle(qp)
        self.drawLines(qp)
        qp.end()


    def drawRectangle(self,qp):
        col = QColor(0,0,0)
        col.setNamedColor("Black")
        qp.setPen(col)
        qp.setBrush(QBrush(Qt.gray,Qt.SolidPattern))
        qp.drawRect(75, 0, 400, 700)

    def drawLines(self,qp):
        pen = QPen(Qt.white, 2, Qt.SolidLine)

        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(155, 0, 155, 700)
        qp.drawLine(235, 0, 235, 700)
        qp.drawLine(315, 0, 315, 700)
        qp.drawLine(395, 0, 395, 700)

    def setCar(self):
        label = QLabel(self)
        pixmap = QPixmap('rsz_car1.jpg')


        label.setPixmap(pixmap)
        label.setGeometry(250,600,50,100)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    prozor = MainWindow()

    sys.exit(app.exec_())
