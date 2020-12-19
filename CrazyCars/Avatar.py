from PyQt5.QtGui import QBrush, QColor, QPen, QPainter, QPixmap, QImage, QPaintEvent
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QLabel, QWidget, QFrame, QLayout
from PyQt5 import QtCore,QtGui, QtWidgets

class Avatar:
    def __init__(self, screen: QWidget, x: int = 250, y: int=620, width: int=50, height: int=80, img: str='crvenii.png'):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img

        self.label = QLabel(screen)
        self.image_pixmap = QPixmap(self.img)
        self.label.setPixmap(self.image_pixmap)
        self.label.setGeometry(self.x, self.y, self.width, self.height)
        self.label.show()

    def moveMeLeft(self):
        if self.x >90:
            self.x = self.x-10
            self.label.setGeometry(self.x, self.y, self.width, self.height)


    def moveMeRight(self):
        if self.x <410:
            self.x = self.x+10
            self.label.setGeometry(self.x, self.y, self.width, self.height)

