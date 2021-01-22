import sys

from PyQt5.QtCore import QCoreApplication, QRect, QSize
from PyQt5.QtGui import QIcon, QCursor, QPainter, QPen, QBrush, QColor, QPixmap, QImage, QPalette
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore

class Scores:
    def __init__(self, screen: QWidget):

        # score label
        self.label = QtWidgets.QLabel(screen)
        self.label.setGeometry(QtCore.QRect(10, 20, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("SCORE:")

        self.scoreValue=0
        self.label_2 = QtWidgets.QLabel(screen)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setNum(self.scoreValue)

        # level label
        self.label_3 = QtWidgets.QLabel(screen)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("LEVEL:")

        self.levelValue = 1
        self.label_4 = QtWidgets.QLabel(screen)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setNum(self.levelValue)

        # life label
        self.label_5 = QtWidgets.QLabel(screen)
        self.label_5.setGeometry(QtCore.QRect(480, 20, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("LIFE:")

        self.lifeCount = 3
        self.label_6 = QtWidgets.QLabel(screen)
        self.label_6.setGeometry(QtCore.QRect(480, 50, 55, 21))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setNum(self.lifeCount)

    def changeScore(self):
        self.scoreValue = self.scoreValue+100
        self.label_2.setNum(self.scoreValue)

    def changeLevel(self):
        self.levelValue = self.levelValue+1
        self.label_4.setNum(self.levelValue)

    def loseLife(self):
        if self.lifeCount>0:
            self.lifeCount = self.lifeCount-1
            self.label_6.setNum(self.lifeCount)

    def incrementLife(self):
        self.lifeCount=self.lifeCount+1
        self.label_6.setNum(self.lifeCount)
