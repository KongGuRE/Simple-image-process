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

        self.drawing_color: tuple = (100, 100, 100)
        self.scaleFactor = 1.0

        self.drawing_size = 1

        self.drawing_btn_ck: bool = False
        self.flood_fill_btn_ck: bool = False

    def inputImage(self, path):
        self.scaleFactor = 1.0
        self.singleOffset = QPoint(0, 0)

        try:
            self.cv_img = cv2.imread(path)  # opencv 이미지 불러오기
            h, w, c = self.cv_img.shape  # 이미지 사이즈 계산
            self.drawing_img = np.full((h, w, c), (0, 0, 0), dtype=np.uint8)  # 이미지 사이즈로 라벨 이미지 데이터 만들기 검은바탕
            cv2.imshow("color_img", self.drawing_img)  # 라벨 이미지 확인
            if len(self.cv_img.shape) < 3:  # 데이터 채널 확인
                self.conv_image = cv2.cvtColor(self.cv_img, cv2.COLOR_GRAY2RGB)
            else:
                self.conv_image = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2RGB)
            self.conv_image = cv2.addWeighted(self.conv_image, 1, self.drawing_img, 1, 0)
            bytesPerLine = 3 * w
            image = QImage(self.conv_image.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)

            myWindow.imgPixmap = QPixmap.fromImage(image)  # Load Images
            # myWindow.imgPixmap = QPixmap(path)  # Load Images

            self.image_input_bool = True
            myWindow.scaledImg = myWindow.imgPixmap.scaled(myWindow.imgPixmap.width(), myWindow.imgPixmap.height())
            # Initialize zoom

            self.singleOffset = QPoint(0, 0)  # Initialize offset value

        except OSError as err:
            print("ERROR :\033[38;5;9m {} \033[0m".format(err))

    @staticmethod
    def Test_print():
        print("\033[38;5;9mok\033[0m")

    def imageInputBox(self):
        pass

    def imageReprint(self):
        self.repaint()

    def conv(self):
        color_img = np.zeros((240, 320, 3), dtype=np.uint8)
        cv2.imshow('color_img', color_img)

    def saveMackedFile(self):
        createFolder("python_")
        cv2.imwrite('python_/grayIronMan.jpg', self.drawing_img)

    def changeDrawingColor(self, _color: tuple):
        self.drawing_color = _color

    def changeDrawingSize(self, _size: int):
        self.drawing_size = _size

    def changeImageTool(self, _tool: str):
        """ Image Tool 변경 값을 위젯에 적용시키기 위한 함수.

        Args:
            _tool: 선택한 Tool 값
                    "drawing" : 이미지 그리기
                    "flood fill" : 이미지 체우기
        Returns:
            delete failed file path list
        """
        if _tool == "drawing":
            self.drawing_btn_ck = True
            self.flood_fill_btn_ck = False
        elif _tool == "flood fill":
            self.drawing_btn_ck = False
            self.flood_fill_btn_ck = True

    def paintEvent(self, event):
        if self.image_input_bool:
            self.displayImgPainter()
            cv2.imshow("color_img", self.drawing_img)

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

    def coordinatesFloodFill(self, _coordinates: QPoint):
        print(
            "S X:\033[38;5;14m {} \033[0m, S Y:\033[38;5;14m {} \033[0m ".format(_coordinates.x(), _coordinates.y()))

        loc_x = round((_coordinates.x() - self.singleOffset.x()) / self.scaleFactor)
        loc_y = round((_coordinates.y() - self.singleOffset.y()) / self.scaleFactor)

        h, w, c = self.drawing_img.shape
        if loc_x >= w:
            loc_x = w-1
        elif loc_x < 0:
            loc_x = 0

        if loc_y >= h:
            loc_y = h-1
        elif loc_y < 0:
            loc_y = 0

        print("loc X:\033[38;5;14m {} \033[0m, loc Y:\033[38;5;14m {} \033[0m ".format(loc_x, loc_y))

        mask = np.zeros((h + 2, w + 2), np.uint8)

        mask[0:3, :] = 255
        mask[:, 0:3] = 255
        mask[:, w-1: w + 2] = 255
        mask[h-1:h+2, :] = 255

        print(self.drawing_img.shape)
        print(mask.shape)
        # mask = np.full((h+2, w+2), (0, 0), dtype=np.uint8)

        loDiff, upDiff = (0, 0, 0), (100, 100, 100)
        seed = (loc_x, loc_y)
        print(seed)


        # retval, self.drawing_img, mask, rect = cv2.floodFill(self.drawing_img, mask, seed, self.drawing_color, loDiff, upDiff)
        cv2.floodFill(self.drawing_img, mask, seed,
                      (self.drawing_color[2], self.drawing_color[1], self.drawing_color[0]),
                      loDiff, upDiff)

        cv2.imshow("mask", mask)
        # cv2.imshow("drawing_img", drawing_img)

    '''Reload mouse down event(Single click)'''

    def mousePressEvent(self, event):
        # print("event.buttons: \033[38;5;14m {} \033[0m".format(event.buttons()))
        # print("QtCore.Qt.LeftButton: \033[38;5;14m {} \033[0m".format(QtCore.Qt.LeftButton))
        # print("QtCore.Qt.RightButton: \033[38;5;14m {} \033[0m".format(QtCore.Qt.RightButton))
        # print("QtCore.Qt.MidButton: \033[38;5;14m {} \033[0m".format(QtCore.Qt.MidButton))

        if event.buttons() == QtCore.Qt.LeftButton:
            print("Left click")  # Response test statement
            self.lastPoint = event.pos()

            self.mouse_left_click = True
            self.mouse_raight_click = False
            self.mouse_middle_click = False

            if self.flood_fill_btn_ck:
                self.coordinatesFloodFill(self.lastPoint)

                self.drawing_btn_ck = not self.drawing_btn_ck
                self.flood_fill_btn_ck = not self.flood_fill_btn_ck
                self.repaint()


        elif event.buttons() == QtCore.Qt.RightButton:
            print("Right click")  # Response test statement
            self.mouse_left_click = False
            self.mouse_raight_click = True
            self.mouse_middle_click = False

            self.drawing_btn_ck = not self.drawing_btn_ck
            self.flood_fill_btn_ck = not self.flood_fill_btn_ck

            self.saveMackedFile()

            print(self.drawing_btn_ck)


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
            newWidth = event.x() - (self.scaledImg.width() * (event.x() - self.singleOffset.x())) \
                       / (self.scaledImg.width() - self.scaleFactor)
            newHeight = event.y() - (self.scaledImg.height() * (event.y() - self.singleOffset.y())) \
                        / (self.scaledImg.height() - self.scaleFactor)
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
            self.mouse_left_click = False

            # print("Release the left mouse button")
        elif event.button == Qt.RightButton:
            # self.singleOffset = QPoint(0, 0)
            # myWindow.scaledImg = myWindow.imgPixmap.scaled(self.size())
            self.repaint()
            # print("Right click to release")

    '''Reload mouse move event'''

    def mouseMoveEvent(self, event):
        if self.mouse_left_click and self.drawing_btn_ck:
            drawing_start_point = self.lastPoint - self.singleOffset
            drawing_end_point = event.pos() - self.singleOffset

            drawing_start_x = drawing_start_point.x() / self.scaleFactor
            drawing_start_y = drawing_start_point.y() / self.scaleFactor
            drawing_end_x = drawing_end_point.x() / self.scaleFactor
            drawing_end_y = drawing_end_point.y() / self.scaleFactor

            h, w, c = self.drawing_img.shape
            if drawing_end_x > w:
                drawing_end_x = w
            elif drawing_end_x < 0:
                drawing_end_x = 0

            if drawing_end_y > h:
                drawing_end_y = h
            elif drawing_end_y < 0:
                drawing_end_y = 0

            if drawing_start_x > w:
                drawing_start_x = w
            elif drawing_start_x < 0:
                drawing_start_x = 0

            if drawing_start_y > h:
                drawing_start_y = h
            elif drawing_start_y < 0:
                drawing_start_y = 0

            print(
                "O X:\033[38;5;14m {} \033[0m".format(self.singleOffset.x()))
            print(
                "O Y:\033[38;5;14m {} \033[0m".format(self.singleOffset.y()))
            print(
                "S X:\033[38;5;14m {} \033[0m, S Y:\033[38;5;14m {} \033[0m ".format(drawing_start_x, drawing_start_y))
            print(
                "E X:\033[38;5;14m {} \033[0m, E Y:\033[38;5;14m {} \033[0m ".format(drawing_end_x, drawing_end_y))

            cv2.line(self.drawing_img,
                     (round(drawing_start_x), round(drawing_start_y)),
                     (round(drawing_end_x), round(drawing_end_y)),
                     (self.drawing_color[2], self.drawing_color[1], self.drawing_color[0]),
                     self.drawing_size, cv2.LINE_AA)

            self.lastPoint = event.pos()
            cv2.imshow("color_img", self.drawing_img)
            self.repaint()

        elif self.mouse_middle_click:
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
    myshow.inputImage("1.jpg")

    myshow.changeImageTool("drawing")
    myshow.changeDrawingColor((100, 100, 0))
    myshow.changeDrawingSize(1)
    # myshow.save_macked_file()
    # myshow.conv()

    myshow.show()
    sys.exit(app.exec_())
