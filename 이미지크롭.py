import glob

import Img_Data_Process as IDP
from PIL import Image
import os
import cv2    # OpenCV import
import numpy as np
import shutil

# 마우스 이벤트 콜백함수 정의
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Button down mouse left button")

    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("Double click mouse left button")
        print("x:", x, " y:", y)

    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Button down mouse right button")

    # print("마우스 이벤트 발생, x:", x ," y:", y) # 이벤트 발생한 마우스 위치 출력


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)


if __name__ == "__main__":
    file_name = "0001.jpg"
    form_1 = '1'

    path = 'C:/DataSET/ImageData/P-TCP 2호기 AOI/'
    print(len(os.listdir(path)))
    img_files = glob.glob(path + '/*.jpg')
    print(len(img_files))

    createFolder(os.path.join(path, 'Crop_Result_Python'))

    # image read
    color = cv2.imread(file_name, cv2.IMREAD_COLOR)
    gray = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    unchange = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)

    while(True):
        cv2.namedWindow(form_1, flags=cv2.WINDOW_NORMAL)
        # 스크린 있는 화면 조절 전체화면
        cv2.resizeWindow(winname=form_1, width=1920, height=1080)
        # 스크린 없는 전체화면
        # cv2.setWindowProperty(form_1, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setMouseCallback(form_1, mouse_callback)

        cv2.imshow(form_1, unchange)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:    # ESC 키 눌러졌을 경우 종료
            print("ESC 키 눌러짐")
            break
    cv2.destroyAllWindows()