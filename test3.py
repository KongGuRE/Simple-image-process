from typing import Type

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from matplotlib import pyplot as plt

import numpy as np
import cv2

from easy_file_control import *

'''Define main window'''


class myWindow(QWidget):
    endMousePosition: object
    preMousePosition: Type[QPoint]

    imgPixmap: QPixmap
    drawing_image: QImage
    scaledImg: QPixmap

    move_image_offset: QPoint
    singleOffset: QPoint
    lastPoint: QPoint

    def __init__(self):
        super(myWindow, self).__init__()
        self.resize(500, 500)
        self.setWindowTitle("Picture manipulation")

        self.mouse_left_click: bool = False
        self.mouse_raight_click: bool = False
        self.mouse_middle_click: bool = False

        self.drawing: bool = True

        self.image_input_bool: bool = False

        self.cv_img: np.array = None
        self.drawing_img: np.array = None
        self.conv_image: np.array = None

        self.drawing_start_point: QPoint = QPoint(0, 0)
        self.drawing_end_point: QPoint = QPoint(0, 0)

        self.drawing_color: tuple = (100, 100, 100)
        self.scaleFactor = 1.0

        self.drawing_size = 1

        self.drawing_btn_ck: bool = False
        self.flood_fill_btn_ck: bool = False


    def input_image(self, path):
        self.scaleFactor = 1.0
        self.drawing_start_point: QPoint = QPoint(0, 0)
        self.drawing_end_point: QPoint = QPoint(0, 0)
        self.singleOffset = QPoint(0, 0)

        # print(path)
        try:
            # opencv 이미지 불러오기
            self.cv_img = cv2.imread(path)
            # 라벨 이미지 데이터 만들기

            # print(myWindow.x)


            h, w, c = self.cv_img.shape

            self.drawing_img = np.full((h, w, c), (0, 0, 0), dtype=np.uint8)
            # self.drawing_img[100:200, :, 0] = 255

            cv2.imshow("color_img", self.drawing_img)
            # 데이터 채널 확인
            if len(self.cv_img.shape) < 3:
                self.conv_image = cv2.cvtColor(self.cv_img, cv2.COLOR_GRAY2RGB)
            else:
                self.conv_image = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2RGB)
            # frame = self.cv_img
            self.conv_image = cv2.addWeighted(self.conv_image, 1, self.drawing_img, 1, 0)

            h, w = self.cv_img.shape[:2]
            bytesPerLine = 3 * w
            image = QImage(self.conv_image.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)

            myWindow.imgPixmap = QPixmap.fromImage(image)  # Load Images
            # myWindow.imgPixmap = QPixmap(path)  # Load Images

            self.image_input_bool = True
            myWindow.scaledImg = myWindow.imgPixmap.scaled(myWindow.imgPixmap.width(), myWindow.imgPixmap.height())
            # Initialize zoom

            self.singleOffset = QPoint(0, 0)  # Initialize offset value
            self.move_image_offset = QPoint(0, 0)  # Initialize offset value

        except OSError as err:
            print("ERROR :\033[38;5;9m {} \033[0m".format(err))

    @staticmethod
    def Test_print():
        print("\033[38;5;9mok\033[0m")

    def test_reprint(self):
        self.repaint()

    def conv(self):
        color_img = np.zeros((240, 320, 3), dtype=np.uint8)
        cv2.imshow('color_img', color_img)

    def save_macked_file(self):
        createFolder("python_")
        cv2.imwrite('python_/grayIronMan.jpg', self.drawing_img)

    def change_drawing_color(self, _color: tuple):
        self.drawing_color = _color

    def change_drawing_size(self, _size: int):
        self.drawing_size = _size

    def paintEvent(self, event):
        if self.image_input_bool:
            self.displayImgPainter()

    # def floodFill(self):
    #     self.drawing_img
    #     cv2.floodFill()

    def displayImgPainter(self):
        print("def Start: \033[38;5;13m {} \033[0m Times : \033[38;5;14m {} \033[0m".format(
            "display_imgPainter", "0"))

        self.conv_image = cv2.addWeighted(self.cv_img, 1, self.drawing_img, 0.8, 0)

        h, w = self.cv_img.shape[:2]
        bytesPerLine = 3 * w
        image = QImage(self.conv_image.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)

        myWindow.imgPixmap = QPixmap.fromImage(image)  # Load Images
        # myWindow.imgPixmap = QPixmap(path)  # Load Images

        self.image_input_bool = True
        myWindow.scaledImg = myWindow.imgPixmap.scaled(round(myWindow.imgPixmap.width() * self.scaleFactor),
                                                       round(myWindow.imgPixmap.height() * self.scaleFactor))
        # Initialize zoom

        """
        img_Painter 를 class variable, class instance 로 선언하면 from size 변경시 
        program 이 정지하는 문제가 있음 따라서 QPainter 는 지역 변수로 잡아놓고 사용.
        """
        img_Painter = QPainter()
        # img_drawing_Painter = QPainter()

        img_Painter.begin(self)
        img_Painter.drawPixmap(self.singleOffset, myWindow.scaledImg)

        print("def End: \033[38;5;13m {} \033[0m Times : \033[38;5;14m {} \033[0m".format(
            "display_imgPainter", "1"))

    '''Reload mouse down event(Single click)'''

    def mousePressEvent(self, event):
        # print("event.buttons: \033[38;5;14m {} \033[0m".format(event.buttons()))
        # print("QtCore.Qt.LeftButton: \033[38;5;14m {} \033[0m".format(QtCore.Qt.LeftButton))
        # print("QtCore.Qt.RightButton: \033[38;5;14m {} \033[0m".format(QtCore.Qt.RightButton))
        # print("QtCore.Qt.MidButton: \033[38;5;14m {} \033[0m".format(QtCore.Qt.MidButton))

        if event.buttons() == QtCore.Qt.LeftButton:
            print("Left click")  # Response test statement
            self.mouse_left_click = True
            self.mouse_raight_click = False
            self.mouse_middle_click = False

            self.drawing = True
            self.lastPoint = event.pos()

        elif event.buttons() == QtCore.Qt.RightButton:
            print("Right click")  # Response test statement
            self.mouse_left_click = False
            self.mouse_raight_click = True
            self.mouse_middle_click = False

        elif event.buttons() == QtCore.Qt.MidButton:
            print("Middle click")  # Response test statement
            self.mouse_left_click = False
            self.mouse_raight_click = False
            self.mouse_middle_click = True
            self.preMousePosition = event.pos()

        elif event.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.RightButton:
            print("Click left and right at the same time")  # Response test statement
        elif event.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.MidButton:
            print("Middle left click")  # Response test statement
        elif event.buttons() == QtCore.Qt.MidButton | QtCore.Qt.RightButton:
            print("Middle right click")  # Response test statement
        elif event.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.MidButton \
                | QtCore.Qt.RightButton:
            print("Left middle right click at the same time")

    '''Reload the scroll event'''

    def wheelEvent(self, event):
        angle = event.angleDelta() / 8
        angleX = angle.x()
        angleY = angle.y()

        if angleY > 0:
            print("Middle mouse button up")
            self.scaleFactor *= 1.1
            newWidth = event.x() - (self.scaledImg.width() * (event.x()-self.singleOffset.x())) \
                        / (self.scaledImg.width()-self.scaleFactor)
            newHeight = event.y() - (self.scaledImg.height() * (event.y()-self.singleOffset.y())) \
                        / (self.scaledImg.height()-self.scaleFactor)
            self.singleOffset = QPoint(newWidth, newHeight)
            self.repaint()
        else:
            print("Middle mouse button down")
            self.scaleFactor *= 0.9
            # newWidth = event.x() - (myWindow.scaledImg.width() * (event.x() - self.singleOffset.x())) \
            #            / (myWindow.scaledImg.width() + self.scaleFactor)
            # newHeight = event.y() - (myWindow.scaledImg.height() * (event.y() - self.singleOffset.y())) \
            #             / (myWindow.scaledImg.height() + self.scaleFactor)
            # self.singleOffset = QPoint(newWidth, newHeight)
            self.repaint()

    '''Reload mouse button to expose events'''

    def mouseReleaseEvent(self, event):
        # print("event.button: \033[38;5;14m {} \033[0m".format(event.button))
        # print("Qt.LatinButton: \033[38;5;14m {} \033[0m".format(QtCore.Qt.LeftButton))
        # print("Qt.RightButton: \033[38;5;14m {} \033[0m".format(Qt.RightButton))
        # print(QtCore.Qt.LeftButton)
        # print(event.buttons())
        if event.button == Qt.LeftButton:
            self.drawing = False
            self.mouse_left_click = False
            print("Release the left mouse button")
        elif event.button == Qt.RightButton:
            # self.singleOffset = QPoint(0, 0)
            # myWindow.scaledImg = myWindow.imgPixmap.scaled(self.size())
            self.repaint()
            print("Right click to release")

    '''Reload mouse move event'''

    def mouseMoveEvent(self, event):

        if self.mouse_left_click and self.drawing:
            self.drawing_start_point = self.lastPoint - self.singleOffset
            self.drawing_end_point = event.pos() - self.singleOffset

            print("S X:\033[38;5;14m {} \033[0m, S Y:\033[38;5;14m {} \033[0m ".format(
                self.drawing_start_point.x(), self.drawing_start_point.y()))
            print("E X:\033[38;5;14m {} \033[0m, E Y:\033[38;5;14m {} \033[0m ".format(
                self.drawing_end_point.x(), self.drawing_end_point.y()))

            cv2.line(self.drawing_img,
                     (round(self.drawing_start_point.x()/self.scaleFactor),
                      round(self.drawing_start_point.y()/self.scaleFactor)),
                     (round(self.drawing_end_point.x()/self.scaleFactor),
                      round(self.drawing_end_point.y()/self.scaleFactor)),
                     self.drawing_color, self.drawing_size, cv2.LINE_AA)

            self.lastPoint = event.pos()
            cv2.imshow("color_img", self.drawing_img)
            self.repaint()

        if self.mouse_middle_click:
            print("Press the left mouse button to move the mouse")
            myWindow.endMousePosition = event.pos() - self.preMousePosition
            self.singleOffset = self.singleOffset + myWindow.endMousePosition
            self.preMousePosition = event.pos()
            self.repaint()


#    '' reload double click event ''
#    def mouseDoubieCiickEvent(self, event):
#        if event.buttons() == QtCore.Qt.LeftButton:                           # Left key press
#            self.setText ("double left mouse button function: self defined")
#
#
#    '' reload mouse to enter control event ''
#    def enterEvent(self, event):
#
#
#    '' reload mouse out control event ''
#    def leaveEvent(self, event):
#
#
#    '' reload mouse to enter control event ''
#    def enterEvent(self, event):
#
#
#    '' reload mouse out control event ''
#    def leaveEvent(self, event):
#

# '''Main function'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myWindow()
    myshow.input_image("2.jpg")
    myshow.change_drawing_color((100, 100, 0))
    # myshow.save_macked_file()
    # myshow.conv()

    myshow.show()
    sys.exit(app.exec_())
