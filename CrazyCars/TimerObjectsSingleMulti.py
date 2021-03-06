
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
from AllObjectsFactory import ObjectFactory
from AllObjectsFactory import ObjectFactoryMulti






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

    def muzikaAvatar(self):
        filename = "Slike/krs1.wav"
        winsound.PlaySound(filename, winsound.SND_ASYNC)

    def muzikaCoin(self):
        filename = "Slike/coin.wav"
        winsound.PlaySound(filename, winsound.SND_ASYNC)

    def muzikaLife(self):
        filename = "Slike/life.wav"
        winsound.PlaySound(filename, winsound.SND_ASYNC)

    def gasiMuziku(self):
        winsound.PlaySound(None,winsound.SND_PURGE)


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
            tempYK=tempY+40

            if type(item) == Avatar.Avatar:
                if (tempX>self.krajnjaLevaMoj and tempX<self.krajnjaDesnaMoj and (tempYK<=self.krajnjaGornjaMoj+120 and tempYK>=self.krajnjaGornjaMoj )):
                    if item.crko==False:
                        self.muzikaAvatar()
                        self.sco.loseLife()
                        item.crko=True
                        if self.sco.lifeCount==0:
                            self.ajmoTimer.stop()
                            self.wp = window.PauseWindow(self.sco.scoreValue)
                            self.wp.show()
                            self.screen.close()

                    item.skloniMeMolimTe()
                    #self.gasiMuziku()

            elif type(item) == Coin.Coin:
                tempYK = tempY-20
                if (tempX > self.krajnjaLevaMoj and tempX < self.krajnjaDesnaMoj and (tempYK <= self.krajnjaGornjaMoj +80 and tempYK >= self.krajnjaGornjaMoj)):
                    if item.crko == False:
                        self.muzikaCoin()
                        item.crko = True
                        self.sco.changeScore()
                        self.brojCoina = self.brojCoina + 1
                        if self.brojCoina==3:
                            self.sco.changeLevel()
                            if self.idemoBrzinaBre>100:
                                self.idemoBrzinaBre=self.idemoBrzinaBre-100
                            elif self.idemoBrzinaBre>50:
                                self.idemoBrzinaBre=self.idemoBrzinaBre-50
                            else:
                                self.idemoBrzinaBre=20
                            self.ajmoTimer.stop()
                            self.generateObjectWithTimer()
                        if self.brojCoina > 3:
                            self.brojCoina = 1
                    item.skloniMeMolimTe()
            elif type(item) == Zivot.Zivot:
                tempYK = tempY-20
                if (tempX > self.krajnjaLevaMoj and tempX < self.krajnjaDesnaMoj and (tempYK <= self.krajnjaGornjaMoj +80 and tempYK >= self.krajnjaGornjaMoj)):
                    if item.crko == False:
                        self.muzikaLife()
                        item.crko = True
                        self.sco.incrementLife()

                    item.skloniMeMolimTe()


            item.moveMeDown()

        self.napravi = self.napravi + 1

class TimerObjectsMulti:
    def __init__(self, screen: QWidget, av1:Avatar,av2:Avatar, sc:ScoresMulti):
        self.screen = screen
        self.list = QListWidget()
        self.cnt = 0
        self.l=[]
        self.mrs=1
        self.napravi=1
        #2 igraca
        self.av1=av1
        self.av2=av2
        self.sco=sc
        self.brojCoina=0
        self.idemoBrzinaBre=500
        self.brojPuta=1

    def muzikaAvatar(self):
        filename = "Slike/krs1.wav"
        winsound.PlaySound(filename, winsound.SND_ASYNC)

    def muzikaBomba(self):
        filename = "Slike/boomba.wav"
        winsound.PlaySound(filename, winsound.SND_ASYNC)

    def muzikaLife(self):
        filename = "Slike/life.wav"
        winsound.PlaySound(filename, winsound.SND_ASYNC)

    #prvi nacin
    def generateObjectWithTimer(self):
        self.ajmoTimer = PyQt5.QtCore.QTimer()
        self.ajmoTimer.timeout.connect(self.createObject)

        #if (self.idemoBrzinaBre<50):
            #self.idemoBrzinaBre=50

        self.ajmoTimer.start(self.idemoBrzinaBre)

    def createObject(self):
        #2 igraca
        self.x1, self.y1 = self.av1.getCoords()
        self.krajnjaLevaMoj1 = self.x1 - 25
        self.krajnjaDesnaMoj1 = self.x1 + 25
        self.krajnjaGornjaMoj1 = self.y1 - 40

        self.x2, self.y2 = self.av2.getCoords()
        self.krajnjaLevaMoj2 = self.x2 - 25
        self.krajnjaDesnaMoj2 = self.x2 + 25
        self.krajnjaGornjaMoj2 = self.y2 - 40

        #self.o1 = self.f1.createObject()
        #self.list.insertItem(self.cnt,self.o1)

        if self.napravi%3==0:
            self.f1 = ObjectFactoryMulti(self.screen, self.mrs)
            self.l.append(self.f1.createObject())
            self.mrs = self.mrs + 1

        if self.napravi % 30 == 0:
            if self.idemoBrzinaBre>50:
                self.idemoBrzinaBre = self.idemoBrzinaBre - 50
            else:
                self.idemoBrzinaBre=20
            self.ajmoTimer.stop()
            self.generateObjectWithTimer()

        for item in self.l:
            tempX,tempY=item.getCoords()
            tempYK=tempY+20

            #za igraca1
            if type(item) == Avatar.Avatar:
                if (tempX>self.krajnjaLevaMoj1 and tempX<self.krajnjaDesnaMoj1 and (tempYK<=self.krajnjaGornjaMoj1+120 and tempYK>=self.krajnjaGornjaMoj1 )):
                    if item.crko==False:
                        self.muzikaAvatar()
                        self.sco.loseLifeP1()
                        item.crko=True
                        if self.sco.lifeCount==0:
                            self.ajmoTimer.stop()
                            self.wp = window.PauseWindowMulti("Player 2","Player 1")
                            self.wp.show()
                            self.screen.close()
                    item.skloniMeMolimTe()
            elif type(item) == Coin.Coin:
                tempYK = tempY-20
                if (tempX > self.krajnjaLevaMoj1 and tempX < self.krajnjaDesnaMoj1 and (tempYK <= self.krajnjaGornjaMoj1 +80 and tempYK >= self.krajnjaGornjaMoj1)):
                    if item.crko == False:
                        item.crko = True
                        self.sco.changeScoreP1()
                        self.brojCoina = self.brojCoina + 1
                    item.skloniMeMolimTe()
            elif type(item) == Zivot.Zivot:
                tempYK = tempY-20
                if (tempX > self.krajnjaLevaMoj1 and tempX < self.krajnjaDesnaMoj1 and (tempYK <= self.krajnjaGornjaMoj1 +80 and tempYK >= self.krajnjaGornjaMoj1)):
                    if item.crko == False:
                        self.muzikaLife()
                        item.crko = True
                        self.sco.incrementLifeP1()

                    item.skloniMeMolimTe()
            elif type(item) == Bomba.Bomba:
                tempYK = tempY-20
                if (tempX > self.krajnjaLevaMoj1 and tempX < self.krajnjaDesnaMoj1 and (tempYK <= self.krajnjaGornjaMoj1 +80 and tempYK >= self.krajnjaGornjaMoj1)):
                    if item.crko == False:
                        self.muzikaBomba()
                        item.crko = True
                        self.sco.decLifeP2()
                        if self.sco.lifeCountp2==0:
                            self.ajmoTimer.stop()
                            self.wp = window.PauseWindowMulti("Player 1","Player 2")
                            self.wp.show()
                            self.screen.close()
                    item.skloniMeMolimTe()





            #za igraca2
            if type(item) == Avatar.Avatar:
                if (tempX>self.krajnjaLevaMoj2 and tempX<self.krajnjaDesnaMoj2 and (tempYK<=self.krajnjaGornjaMoj2+120 and tempYK>=self.krajnjaGornjaMoj2 )):
                    if item.crko==False:
                        self.muzikaAvatar()
                        self.sco.loseLifeP2()
                        item.crko=True
                        if self.sco.lifeCountp2==0:
                            self.ajmoTimer.stop()
                            self.wp = window.PauseWindowMulti("Player 1", "Player 2")
                            self.wp.show()
                            self.screen.close()
                    item.skloniMeMolimTe()
            elif type(item) == Coin.Coin:
                tempYK = tempY-20
                if (tempX > self.krajnjaLevaMoj2 and tempX < self.krajnjaDesnaMoj2 and (tempYK <= self.krajnjaGornjaMoj2 +80 and tempYK >= self.krajnjaGornjaMoj2)):
                    if item.crko == False:
                        item.crko = True
                        self.sco.changeScoreP2()
                        self.brojCoina = self.brojCoina + 1
                    item.skloniMeMolimTe()
            elif type(item) == Zivot.Zivot:
                tempYK = tempY-20
                if (tempX > self.krajnjaLevaMoj2 and tempX < self.krajnjaDesnaMoj2 and (tempYK <= self.krajnjaGornjaMoj2 +80 and tempYK >= self.krajnjaGornjaMoj2)):
                    if item.crko == False:
                        self.muzikaLife()
                        item.crko = True
                        self.sco.incrementLifeP2()

                    item.skloniMeMolimTe()

            elif type(item) == Bomba.Bomba:
                tempYK = tempY-20
                if (tempX > self.krajnjaLevaMoj2 and tempX < self.krajnjaDesnaMoj2 and (tempYK <= self.krajnjaGornjaMoj2 +80 and tempYK >= self.krajnjaGornjaMoj2)):
                    if item.crko == False:
                        self.muzikaBomba()
                        item.crko = True
                        self.sco.decLifeP1()
                        if self.sco.lifeCount==0:
                            self.ajmoTimer.stop()
                            self.wp = window.PauseWindowMulti("Player 2","Player 1")
                            self.wp.show()
                            self.screen.close()
                    item.skloniMeMolimTe()

            item.moveMeDown()


        self.napravi = self.napravi + 1
