import sys

from PyQt5.QtCore import QCoreApplication, QRect, QSize
from PyQt5.QtGui import QIcon, QCursor, QPainter, QPen, QBrush, QColor, QPixmap, QImage, QPalette
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore

class ScoresMulti:
    def __init__(self, screen: QWidget):
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)

        self.labelGorep1 = QtWidgets.QLabel(screen)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 30, 70,30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Player 1:")

        self.labelGorep2 = QtWidgets.QLabel(screen)
        self.labelGorep2.setGeometry(QtCore.QRect(470, 30, 70, 30))
        self.labelGorep2.setFont(font)
        self.labelGorep2.setText("Player 2:")

        # life label player 1
        self.label_5 = QtWidgets.QLabel(screen)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("LIFE:")

        self.lifeCount = 3
        self.label_6 = QtWidgets.QLabel(screen)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setNum(self.lifeCount)

        # life label player 2
        self.label_5p2 = QtWidgets.QLabel(screen)
        self.label_5p2.setGeometry(QtCore.QRect(470, 110, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_5p2.setFont(font)
        self.label_5p2.setObjectName("label_5")
        self.label_5p2.setText("LIFE:")

        self.lifeCountp2 = 3
        self.label_6p2 = QtWidgets.QLabel(screen)
        self.label_6p2.setGeometry(QtCore.QRect(470, 140, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_6p2.setFont(font)
        self.label_6p2.setNum(self.lifeCount)


    def changeScoreP1(self):
        self.scoreValue = self.scoreValue+100
        self.label_2.setNum(self.scoreValue)

    def changeScoreP2(self):
        self.scoreValuep2 = self.scoreValuep2+100
        self.label_2p2.setNum(self.scoreValuep2)


    def loseLifeP1(self):
        if self.lifeCount>0:
            self.lifeCount = self.lifeCount-1
            self.label_6.setNum(self.lifeCount)

    def loseLifeP2(self):
        if self.lifeCountp2>0:
            self.lifeCountp2 = self.lifeCountp2-1
            self.label_6p2.setNum(self.lifeCountp2)

    def incrementLifeP1(self):
        self.lifeCount=self.lifeCount+1
        self.label_6.setNum(self.lifeCount)




    def incrementLifeP2(self):
        self.lifeCountp2=self.lifeCountp2+1
        self.label_6p2.setNum(self.lifeCountp2)


    def decLifeP1(self):
        self.lifeCount=self.lifeCount-1
        self.label_6.setNum(self.lifeCount)

    def decLifeP2(self):
        self.lifeCountp2=self.lifeCountp2-1
        self.label_6p2.setNum(self.lifeCountp2)



class ScoresChampSF2:
    def __init__(self, screen: QWidget):
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)

        self.labelGorep1 = QtWidgets.QLabel(screen)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 30, 70,30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText("Player 3:")

        self.labelGorep2 = QtWidgets.QLabel(screen)
        self.labelGorep2.setGeometry(QtCore.QRect(470, 30, 70, 30))
        self.labelGorep2.setFont(font)
        self.labelGorep2.setText("Player 4:")


        # life label player 1
        self.label_5 = QtWidgets.QLabel(screen)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("LIFE:")

        self.lifeCount = 3
        self.label_6 = QtWidgets.QLabel(screen)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setNum(self.lifeCount)

        # life label player 2
        self.label_5p2 = QtWidgets.QLabel(screen)
        self.label_5p2.setGeometry(QtCore.QRect(470, 110, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_5p2.setFont(font)
        self.label_5p2.setObjectName("label_5")
        self.label_5p2.setText("LIFE:")

        self.lifeCountp2 = 3
        self.label_6p2 = QtWidgets.QLabel(screen)
        self.label_6p2.setGeometry(QtCore.QRect(470, 140, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_6p2.setFont(font)
        self.label_6p2.setNum(self.lifeCount)


    def changeScoreP1(self):
        self.scoreValue = self.scoreValue+100
        self.label_2.setNum(self.scoreValue)

    def changeScoreP2(self):
        self.scoreValuep2 = self.scoreValuep2+100
        self.label_2p2.setNum(self.scoreValuep2)


    def loseLifeP1(self):
        if self.lifeCount>0:
            self.lifeCount = self.lifeCount-1
            self.label_6.setNum(self.lifeCount)

    def loseLifeP2(self):
        if self.lifeCountp2>0:
            self.lifeCountp2 = self.lifeCountp2-1
            self.label_6p2.setNum(self.lifeCountp2)

    def incrementLifeP1(self):
        self.lifeCount=self.lifeCount+1
        self.label_6.setNum(self.lifeCount)


    def incrementLifeP2(self):
        self.lifeCountp2=self.lifeCountp2+1
        self.label_6p2.setNum(self.lifeCountp2)

    def decLifeP1(self):
        self.lifeCount=self.lifeCount-1
        self.label_6.setNum(self.lifeCount)

    def decLifeP2(self):
        self.lifeCountp2=self.lifeCountp2-1
        self.label_6p2.setNum(self.lifeCountp2)


class ScoresChampF:
    def __init__(self, screen: QWidget, pobSF1:str="", pobSF2:str=""):

        self.pob1=pobSF1
        self.pob2=pobSF2

        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)

        self.labelGorep1 = QtWidgets.QLabel(screen)
        self.labelGorep1.setGeometry(QtCore.QRect(10, 30, 70,30))
        self.labelGorep1.setFont(font)
        self.labelGorep1.setText(self.pob1)

        self.labelGorep2 = QtWidgets.QLabel(screen)
        self.labelGorep2.setGeometry(QtCore.QRect(470, 30, 70, 30))
        self.labelGorep2.setFont(font)
        self.labelGorep2.setText(self.pob2)


        # life label player 1
        self.label_5 = QtWidgets.QLabel(screen)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("LIFE:")

        self.lifeCount = 3
        self.label_6 = QtWidgets.QLabel(screen)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setNum(self.lifeCount)

        # life label player 2
        self.label_5p2 = QtWidgets.QLabel(screen)
        self.label_5p2.setGeometry(QtCore.QRect(470, 110, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_5p2.setFont(font)
        self.label_5p2.setObjectName("label_5")
        self.label_5p2.setText("LIFE:")

        self.lifeCountp2 = 3
        self.label_6p2 = QtWidgets.QLabel(screen)
        self.label_6p2.setGeometry(QtCore.QRect(470, 140, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_6p2.setFont(font)
        self.label_6p2.setNum(self.lifeCount)


    def changeScoreP1(self):
        self.scoreValue = self.scoreValue+100
        self.label_2.setNum(self.scoreValue)

    def changeScoreP2(self):
        self.scoreValuep2 = self.scoreValuep2+100
        self.label_2p2.setNum(self.scoreValuep2)


    def loseLifeP1(self):
        if self.lifeCount>0:
            self.lifeCount = self.lifeCount-1
            self.label_6.setNum(self.lifeCount)

    def loseLifeP2(self):
        if self.lifeCountp2>0:
            self.lifeCountp2 = self.lifeCountp2-1
            self.label_6p2.setNum(self.lifeCountp2)

    def incrementLifeP1(self):
        self.lifeCount=self.lifeCount+1
        self.label_6.setNum(self.lifeCount)


    def incrementLifeP2(self):
        self.lifeCountp2=self.lifeCountp2+1
        self.label_6p2.setNum(self.lifeCountp2)

    def decLifeP1(self):
        self.lifeCount=self.lifeCount-1
        self.label_6.setNum(self.lifeCount)

    def decLifeP2(self):
        self.lifeCountp2=self.lifeCountp2-1
        self.label_6p2.setNum(self.lifeCountp2)
