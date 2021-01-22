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
import Avatar
import Scores
import window
import Coin

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
    def __init__(self, screen: QWidget, av:Avatar, sc:Scores):
        self.screen = screen
        self.list = QListWidget()
        self.cnt = 0
        self.l=[]
        self.mrs=1
        self.napravi=1
        self.av=av
        self.sco=sc
        self.brojCoina=0
        self.idemoBrzinaBre=500
        self.brojPuta=1

    #prvi nacin
    def generateObjectWithTimer(self):
        self.ajmoTimer = PyQt5.QtCore.QTimer()
        self.ajmoTimer.timeout.connect(self.createObject)


        self.ajmoTimer.start(self.idemoBrzinaBre)

    def createObject(self):

        self.x1, self.y1 = self.av.getCoords()
        self.krajnjaLevaMoj = self.x1 - 25
        self.krajnjaDesnaMoj = self.x1 + 25
        self.krajnjaGornjaMoj = self.y1 - 40
        #self.o1 = self.f1.createObject()
        #self.list.insertItem(self.cnt,self.o1)

        if self.napravi%3==0:
            self.f1 = ObjectFactory(self.screen, self.mrs)
            self.l.append(self.f1.createObject())
            self.mrs = self.mrs + 1

        for item in self.l:
            tempX,tempY=item.getCoords()
            tempYK=tempY+20

            if type(item) == Avatar.Avatar:
                if (tempX>self.krajnjaLevaMoj and tempX<self.krajnjaDesnaMoj and (tempYK<=self.krajnjaGornjaMoj+20 and tempYK>=self.krajnjaGornjaMoj )):
                    if item.crko==False:
                        self.sco.loseLife()
                        item.crko=True
                        if self.sco.lifeCount==0:
                            self.ajmoTimer.stop()
                            self.wp = window.PauseWindow()
                            self.wp.show()
                            self.screen.close()
                    item.skloniMeMolimTe()
            elif type(item) == Coin.Coin:
                tempYK = tempY-20
                if (tempX > self.krajnjaLevaMoj and tempX < self.krajnjaDesnaMoj and (tempYK <= self.krajnjaGornjaMoj +20 and tempYK >= self.krajnjaGornjaMoj)):
                    if item.crko == False:
                        item.crko = True
                        self.sco.changeScore()
                        self.brojCoina = self.brojCoina + 1
                        if self.brojCoina==3:
                            self.sco.changeLevel()
                            self.idemoBrzinaBre=self.idemoBrzinaBre-200
                            self.ajmoTimer.stop()
                            self.generateObjectWithTimer()
                        if self.brojCoina > 3:
                            self.brojCoina = 1
                    item.skloniMeMolimTe()

            item.moveMeDown()

        self.napravi = self.napravi + 1





