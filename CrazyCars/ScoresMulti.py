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

        # score label player1
        self.label = QtWidgets.QLabel(screen)
        self.label.setGeometry(QtCore.QRect(10, 90, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("SCORE:")

        self.scoreValue=0
        self.label_2 = QtWidgets.QLabel(screen)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setNum(self.scoreValue)

        # score label player2
        self.labelp2 = QtWidgets.QLabel(screen)
        self.labelp2.setGeometry(QtCore.QRect(470, 90, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.labelp2.setFont(font)
        self.labelp2.setObjectName("label")
        self.labelp2.setText("SCORE:")

        self.scoreValuep2 = 0
        self.label_2p2 = QtWidgets.QLabel(screen)
        self.label_2p2.setGeometry(QtCore.QRect(470, 120, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_2p2.setFont(font)
        self.label_2p2.setObjectName("label_2")
        self.label_2p2.setNum(self.scoreValue)


        # life label player 1
        self.label_5 = QtWidgets.QLabel(screen)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("LIFE:")

        self.lifeCount = 3
        self.label_6 = QtWidgets.QLabel(screen)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setNum(self.lifeCount)

        # life label player 2
        self.label_5p2 = QtWidgets.QLabel(screen)
        self.label_5p2.setGeometry(QtCore.QRect(470, 160, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_5p2.setFont(font)
        self.label_5p2.setObjectName("label_5")
        self.label_5p2.setText("LIFE:")

        self.lifeCountp2 = 3
        self.label_6p2 = QtWidgets.QLabel(screen)
        self.label_6p2.setGeometry(QtCore.QRect(470, 190, 55, 21))
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
