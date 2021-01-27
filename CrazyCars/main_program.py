
import sys
from PyQt5.QtWidgets import QApplication
from window import MainWindow



if __name__ == '__main__':
    app = QApplication(sys.argv)
    prozor = MainWindow()  #Poziv glavnog menija.

    sys.exit(app.exec_())