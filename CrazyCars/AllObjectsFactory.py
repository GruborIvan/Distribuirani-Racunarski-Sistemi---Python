import sys
import random

from PyQt5.QtCore import QCoreApplication, QRect, QSize
from PyQt5.QtGui import QIcon, QCursor, QPainter, QPen, QBrush, QColor, QPixmap, QImage, QPalette
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore
from Avatar import AvatarFactory
from Coin import CoinFactory


class ObjectFactory:
    def __init__(self, screen: QWidget):
        self.screen = screen

    def createObject(self):
        self.avatarFac= AvatarFactory(self.screen)
        self.coinFac = CoinFactory(self.screen)
        self.objType = random.randint(0,1)

        if self.objType == 0:
            self.a=self.avatarFac.createRandomAvatar()

        if self.objType == 1:
            self.c=self.coinFac.createRandomCoin()
