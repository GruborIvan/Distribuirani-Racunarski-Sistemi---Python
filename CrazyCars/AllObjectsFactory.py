import sys
import random
import time
import multiprocessing
import threading
import winsound

import PyQt5
from PyQt5.QtCore import QCoreApplication, QRect, QSize
from PyQt5.QtGui import QIcon, QCursor, QPainter, QPen, QBrush, QColor, QPixmap, QImage, QPalette
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QLabel, QListWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore
from Avatar import AvatarFactory
from Coin import CoinFactory
from Zivot import SrceFactory
from Bomba import BombaFactory
import Avatar
import Scores
import ScoresMulti
import window
import Coin
import Zivot
import Bomba

class ObjectFactory():
    def __init__(self, screen: QWidget,  x: int = 250):
        self.screen = screen
        self.a=x

    def createObject(self):
        self.avatarFac= AvatarFactory(self.screen)
        self.coinFac = CoinFactory(self.screen)
        self.zivotFac = SrceFactory(self.screen)

        #self.objType = random.randint(0,1)



        if self.a%4==0:

            self.a = self.coinFac.createRandomCoin()

        elif self.a%5==0:
            self.a = self.zivotFac.createRandomSrce()
        else:
            self.a = self.avatarFac.createRandomAvatar()

        return  self.a

class ObjectFactoryMulti():
    def __init__(self, screen: QWidget,  x: int = 250):
        self.screen = screen
        self.a=x

    def createObject(self):
        self.avatarFac= AvatarFactory(self.screen)
        self.zivotFac = SrceFactory(self.screen)
        self.bombaFac = BombaFactory(self.screen)

        #self.objType = random.randint(0,1)


        if self.a%5==0:
            self.a = self.zivotFac.createRandomSrce()
        elif self.a%9==0:
            self.a=self.bombaFac.createRandomBomba()
        else:
            self.a = self.avatarFac.createRandomAvatar()

        return  self.a
