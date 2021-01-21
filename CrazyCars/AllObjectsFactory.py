import sys
import random
import time
import multiprocessing
import threading


import PyQt5
from PyQt5.QtCore import QCoreApplication, QRect, QSize
from PyQt5.QtGui import QIcon, QCursor, QPainter, QPen, QBrush, QColor, QPixmap, QImage, QPalette
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QLabel, QListWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore
from Avatar import AvatarFactory
from Coin import CoinFactory

a=1

class ObjectFactory():
    def __init__(self, screen: QWidget,  x: int = 250):
        self.screen = screen
        self.a=x

    def createObject(self):
        self.avatarFac= AvatarFactory(self.screen)
        self.coinFac = CoinFactory(self.screen)

        #self.objType = random.randint(0,1)



        if self.a%4==0:

            self.a = self.coinFac.createRandomCoin()

        else:
            self.a = self.avatarFac.createRandomAvatar()

        return  self.a

class TimerObjects:
    def __init__(self, screen: QWidget):
        self.screen = screen
        self.list = QListWidget()
        self.cnt = 0
        self.l=[]
        self.mrs=1
        self.mrs=1

    #prvi nacin
    def generateObjectWithTimer(self):
        self.ajmoTimer = PyQt5.QtCore.QTimer()
        self.ajmoTimer.timeout.connect(self.createObject)
        self.ajmoTimer.start(2000)

    def createObject(self):
        self.mrs=self.mrs+1
        self.f1 = ObjectFactory(self.screen,self.mrs)
        #self.o1 = self.f1.createObject()
        #self.list.insertItem(self.cnt,self.o1)
        self.l.append(self.f1.createObject())
        for item in self.l:
            item.moveMeDown()





    #drugi nacin
    def pokreniThread(self):

        for _ in range(10):
            time.sleep(1)
            t1 = threading.Thread(target=self.napraviObjekat)
            t1.start()


    def napraviObjekat(self):
        self.f1 = ObjectFactory(self.screen)
        self.o1 = self.f1.createObject()

    #treci nacin
    def generateObjectWithoutTimer(self):
        self.f1 = ObjectFactory(self.screen)
        for _ in range(10):
            self.o1 = self.f1.createObject()
            time.sleep(1)


    def moveMe(self,a):
        a.moveMeDown()








    def pomerajMe(self,ja):
        ja.moveMeDown()

