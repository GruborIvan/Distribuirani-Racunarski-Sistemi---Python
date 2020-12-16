from PyQt5.QtGui import QBrush, QColor, QPen, QPainter, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QFrame


class Car(QFrame):
    def __init__(self):
        super().__init__()
        self.setCar()
    def setCar(self):
        label = QLabel(self)
        pixmap = QPixmap('rsz_car1.jpg')

        label.setPixmap(pixmap)
        label.setGeometry(250, 600, 50, 100)
        self.show()
