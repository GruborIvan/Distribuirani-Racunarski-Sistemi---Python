import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QApplication)

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        vbox = QVBoxLayout()
        vbox.stretch(1)
        vbox.addWidget(okButton)
        vbox.addWidget(cancelButton)

        hbox = QHBoxLayout()
        hbox.stretch(1)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
