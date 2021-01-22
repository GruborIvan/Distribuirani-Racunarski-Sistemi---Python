import random
import sys

from PyQt5.QtGui import QBrush, QColor, QPen, QPainter, QPixmap, QImage, QPaintEvent
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QLabel, QWidget, QFrame, QLayout
from PyQt5 import QtCore,QtGui, QtWidgets



class Avatar:
    def __init__(self, screen: QWidget, x: int = 250, y: int=620, width: int=50, height: int=80, img: str='Slike/crvenii.png'):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.crko=False
        self.tip = 'Auto'


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

    def moveMeDown(self):
        self.y = self.y +28
        self.label.setGeometry(self.x,self.y,self.width,self.height)

    def getCoords(self):
        return self.x, self.y

    def skloniMeMolimTe(self):
        self.label.hide()




class AvatarFactory():
    def __init__(self, screen: QWidget):
        self.screen = screen
        self.y=0
        self.width = 50
        self.height = 80
        self.img = "police.png"

    def createRandomAvatar(self):
        x_values=[97,167,247,327,399]
        img_values = ['Slike/sivi.png','Slike/zuti.png','Slike/zeleni.png','Slike/ambulance.png','Slike/police.png','Slike/selfMade.png']
        self.x=x_values[random.randint(0,4)]
        self.img = img_values[random.randint(0,5)]
        self.a = Avatar(self.screen, self.x, self.y, self.width, self.height,self.img)
        return self.a