import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5 import QtCore

import numpy as np


class QImageViewer(QMainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.drawing = False
        self.lastPoint = QPoint()
        self.image = QPixmap("1.jpg")

        print(type(self.image))

        self.setGeometry(100, 100, 600, 600)
        self.resize(self.image.width(), self.image.height())

        self.resized.connect(self.someFunction)

        self.show()

    def someFunction(self):
        print("someFunction")

    def resizeEvent(self, event):
        self.resized.emit()
        return super(QImageViewer, self).resizeEvent(event)

    def paintEvent(self, event):
        print("paintEvent: type(self.image) -> {}".format(type(self.image)))
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    def mousePressEvent(self, event):
        print(event.pos())
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):

        if event.buttons() and Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(QColor(255, 0, 0, 90), 5, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = QImageViewer()
    sys.exit(app.exec_())
