import sys
from math import sin, cos, pi
from random import randint
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setMouseTracking(True)
        self.pushButton.clicked.connect(self.drawf)
        self.qp = QPainter()
        self.flag = False
        self.status = None

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        coords_ = [randint(10, 350), randint(10, 300)]
        D = randint(20, 100)
        R = D / 2
        self.qp.setBrush(QColor(*[255, 255, 0]))
        self.qp.drawEllipse(int(coords_[0] - R), int(coords_[1] - R), D, D)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Рисование')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec_())

