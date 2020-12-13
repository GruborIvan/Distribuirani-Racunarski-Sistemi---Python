import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout \



class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 700)

        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon('car.png'))

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
        exit_button = QPushButton("Exit")

        vbox = QVBoxLayout()
        vbox.addWidget(exit_button)
        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        self.setLayout(hbox)
        exit_button.resize(30,30)
        exit_button.clicked.connect(self.playScreen)


    def playScreen(self):
        self.w = MainWindow()
        self.w.show()
        self.hide()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    prozor = MainWindow()



    sys.exit(app.exec_())
