from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

'''Define main window'''
class myWindow(QWidget):                                                       # QMainWindow is not available because QLabel inherits from QWidget
    def __init__(self):
        super(myWindow, self).__init__()
        self.resize(500,500)                                                   # Set the window size (it can be changed according to the size of the picture you display)
        self.setWindowTitle("Picture manipulation")                                        # Set window name
        self.isLeftPressed = bool(False)                                       # Picture is clicked (left mouse button) flag bit
        self.isImgLabelArea = bool(True)                                       # Mouse into the label picture display area

    def input_image(self, path):
        self.imgPixmap = QPixmap(path)  # Load Images
        self.scaledImg = self.imgPixmap.scaled(self.imgPixmap.width(), self.imgPixmap.height())  # Initialize zoom
        self.singleOffset = QPoint(0, 0)  # Initialize offset value

    '''Heavy haul drawing: Dynamic drawing'''
    def paintEvent(self,event):
        self.imgPainter = QPainter()                                           # Use to draw pictures dynamically
        self.imgFramePainter = QPainter()                                      # Use to draw picture outline dynamically
        self.imgPainter.begin(self)                                            # If there is no begin and end, the update cycle will continue
        self.imgPainter.drawPixmap(self.singleOffset, self.scaledImg)          # Extract Pixmap from image file and display it in the specified location
        self.imgFramePainter.setPen(QColor(168, 34, 3))  # Default black if not set   # Set drawing color / size / style
        self.imgFramePainter.drawRect(10, 10, 480, 480)                        # Draw lines for pictures (extend 1 outwards)
        self.imgPainter.end()                                                  # If there is no begin and end, the update cycle will continue

# =============================================================================
# Picture moving: first, make sure that the picture is clicked (left mouse button is pressed) and not released with the left mouse button;
#          Secondly, confirm the mouse movement;
#          Finally, update the offset value and move the picture
# =============================================================================
    '''Reload mouse down event(Single click)'''
    def mousePressEvent(self, event):
        print(event.pos())
        if event.buttons() == QtCore.Qt.LeftButton:                            # Left key press
            print("Left click")  # Response test statement
            self.isLeftPressed = True;                                         # Press the left key (the picture is clicked), and set the tree
            self.preMousePosition = event.pos()                                # Get the current mouse position
        elif event.buttons () == QtCore.Qt.RightButton:                        # Right click
            print("Right click")  # Response test statement
        elif event.buttons() == QtCore.Qt.MidButton:                           # Press key
            print("Middle click")  # Response test statement
        elif event.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.RightButton:  # Press the left and right keys at the same time
            print("Click left and right at the same time")  # Response test statement
        elif event.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.MidButton:    # Press the left middle key at the same time
            print("Middle left click")  # Response test statement
        elif event.buttons() == QtCore.Qt.MidButton | QtCore.Qt.RightButton:   # Press the right middle key at the same time
            print("Middle right click")  # Response test statement
        elif event.buttons() == QtCore.Qt.LeftButton | QtCore.Qt.MidButton \
             | QtCore.Qt.RightButton:                                          # Press the left middle right key at the same time
            print("Left middle right click at the same time")  # Response test statement

    '''Reload the scroll event'''
    def wheelEvent(self, event):
#        if event.delta() > 0:                                                 # Roller up, PyQt4
        # This function has been deprecated, use pixelDelta() or angleDelta() instead.
        angle=event.angleDelta() / 8                                           # Returns the QPoint object, which is the value of the wheel rotation, in 1 / 8 degree
        angleX=angle.x()                                                       # Distance rolled horizontally (not used here)
        angleY=angle.y()                                                       # Vertical rolling distance
        if angleY > 0:                                                         # Roller rolling
            print("Middle mouse button up")  # Response test statement
            self.scaledImg = self.imgPixmap.scaled(self.scaledImg.width()+5,
                                                   self.scaledImg.height()+5)
            newWidth = event.x() - (self.scaledImg.width() * (event.x()-self.singleOffset.x())) \
                        / (self.scaledImg.width()-5)
            newHeight = event.y() - (self.scaledImg.height() * (event.y()-self.singleOffset.y())) \
                        / (self.scaledImg.height()-5)
            self.singleOffset = QPoint(newWidth, newHeight)                    # Update offset
            self.repaint()                                                     # Repaint
        else:                                                                  # wheel down
            print("Middle mouse button down")  # Response test statement
            self.scaledImg = self.imgPixmap.scaled(self.scaledImg.width()-5,
                                                   self.scaledImg.height()-5)
            newWidth = event.x() - (self.scaledImg.width() * (event.x()-self.singleOffset.x())) \
                        / (self.scaledImg.width()+5)
            newHeight = event.y() - (self.scaledImg.height() * (event.y()-self.singleOffset.y())) \
                        / (self.scaledImg.height()+5)
            self.singleOffset = QPoint(newWidth, newHeight)                    # Update offset
            self.repaint()                                                     # Repaint

    '''Reload mouse button to expose events'''
    def mouseReleaseEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:                            # Release of left key
            self.isLeftPressed = False;  # Left click to release (picture is clicked), set False
            print("Release the left mouse button")  # Response test statement
        elif event.button() == Qt.RightButton:                                 # Right click release
            self.singleOffset = QPoint(0, 0)                                   # Set as initial value
            self.scaledImg = self.imgPixmap.scaled(self.size())                # Set as initial value
            self.repaint()                                                     # Repaint
            print("Right click to release")  # Response test statement

    '''Reload mouse move event'''
    def mouseMoveEvent(self,event):
        if self.isLeftPressed:                                                 # Left key press
            print("Press the left mouse button to move the mouse")  # Response test statement
            self.endMousePosition = event.pos() - self.preMousePosition        # Mouse current position - previous position = single offset
            self.singleOffset = self.singleOffset + self.endMousePosition      # Update offset
            self.preMousePosition = event.pos()                                # Update the position of the current mouse on the window. Use
            self.repaint()                                                     # Repaint

    def print(self, a):
        print("ok")

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

#    '' reload mouse to enter control event ''
#    def enterEvent(self, event):
#
#
#    '' reload mouse out control event ''
#    def leaveEvent(self, event):
#

# '''Main function'''
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     myshow = myWindow()
#     myshow.show()
#     sys.exit (app.exec_())