import sys
import random

from PyQt5.QtCore import QCoreApplication, QRect, QSize
from PyQt5.QtGui import QIcon, QCursor, QPainter, QPen, QBrush, QColor, QPixmap, QImage, QPalette
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore


class Zivot:

    #Constructor
    def __init__(self, screen: QWidget, x: int = 110, y: int=0, width: int=25, height: int=25, img: str='Slike/rsz_mrs.png'):

        #Koordinate.
        self.x = x
        self.y = y

        self.width = width
        self.height = height    #Sirina i visina.
        self.img = img
        self.crko=False

        self.label = QLabel(screen)
        self.image_pixmap = QPixmap(self.img)
        self.label.setPixmap(self.image_pixmap)
        self.label.setGeometry(self.x, self.y, self.width, self.height)
        self.label.show()

    def moveMeDown(self):
        self.y = self.y+20
        self.label.setGeometry(self.x,self.y,self.width,self.height)

    def getCoords(self):
        return self.x,self.y

    def hideZivot(self):
        self.label.hide()


class SrceFactory():

    #Constructor
    def __init__(self, screen: QWidget):
        self.y=0
        self.width=25
        self.height=25
        self.screen=screen


    #Generisanje Random srca (zivot)
    def createRandomSrce(self):
        x_values=[110,183,263,343,414]
        self.x = x_values[random.randint(0,4)]
        self.srce=Zivot(self.screen, self.x,self.y,self.width,self.height)
        return self.srce