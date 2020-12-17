from PyQt5.QtGui import QBrush, QColor, QPen, QPainter, QPixmap, QImage, QPaintEvent
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QLabel, QWidget, QFrame, QLayout
from PyQt5 import QtCore,QtGui, QtWidgets

class Avatar:
    def __init__(self, screen: QWidget, x: int = 250, y: int=620, width: int=50, height: int=80, img: str='rsz_f47de7fd81202f36e8fc39bf2a5f296f.jpg'):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img

        self.label = QLabel(screen)
        self.image_pixmap = QPixmap(self.img)
        self.label.setPixmap(self.image_pixmap)
        self.label.setGeometry(self.x, self.y, self.width, self.height)


'''
    def keyPressEvent(self, event):


        if event.key() == QtCore.Qt.Key_A:
            self.x = self.x -5

        elif event.key() == QtCore.Qt.Key_D:
            self.x = self.x - 5

'''











'''
 def paintEvent(self, e):
        qp = QPainter()
        qp.begin(e)
        self.drawImage(qp)
        qp.end()

    def drawImage(self, qp):
        qp.drawImage(QRect(250, 600, 50, 100), QImage('rsz_f47de7fd81202f36e8fc39bf2a5f296f.jpg'))

'''
