import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import Integrated_image_processing as Iip

import datetime
import glob
import math
import multiprocessing
import os
import random
from multiprocessing import Process
from typing import List

import cv2
from PIL import Image

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(r"main.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 변수
        self.manager = multiprocessing.Manager()
        self.return_dict = self.manager.dict()

        # 버튼
        self.btn_main_start.clicked.connect(self.btn_main_start_clicked)
        self.btn_main_stop.clicked.connect(self.btn_main_stop_clicked)

    def btn_main_start_clicked(self):
        self.return_dict = self.manager.dict()

        self.process = Process(target=self.btn_main_start_clicked_process,
                               args=(self.le_datapath.text(),
                                     self.le_ext.text(),
                                     int(self.le_x_size.text()),
                                     int(self.le_y_size.text()),
                                     self.ckb_subfolders.isChecked(),
                                     int(self.le_Processor_numbers.text()),
                                     self.return_dict
                                     ))
        self.process.start()

    @staticmethod
    def btn_main_start_clicked_process(data_path,
                                       data_ext,
                                       sub_folders,
                                       size_x, size_y, number_of_Process,
                                       return_dict):

        # test_list = [
        #     self.le_datapath.text(),
        #     self.le_ext.text(),
        #     int(self.le_x_size.text()),
        #     int(self.le_y_size.text()),
        #     self.ckb_subfolders.isChecked(),
        #     int(self.le_Processor_numbers.text())
        # ]
        # for test in test_list:
        #     print(test)
        #     print(type(test))
        # exit()

        data_list = [
            Iip.search_directory(data_path, data_ext, sub_folders)
        ]

        data_list = Iip.list_flatten(data_list)
        random.shuffle(data_list)

        number_of_data = len(data_list)
        number_of_task = math.ceil(number_of_data / number_of_Process)

        print("number of data: \033[38;5;14m {} \033[0m".format(number_of_data))
        print("number of task: \033[38;5;14m {} \033[0m".format(number_of_task))

        task_list = Iip.list_chunk(data_list, number_of_task)
        setting_process = len(task_list)

        print("setting process : \033[38;5;14m {} \033[0m".format(number_of_Process),
              "activate process: \033[38;5;9m {} \033[0m".format(setting_process))

        jobs = []

        for task_number in range(setting_process):
            process = Process(target=Iip.main,
                              args=(task_number, task_list[task_number], size_x, size_y, return_dict))
            jobs.append(process)
            process.start()

        for proc in jobs:
            proc.join()

    def btn_main_stop_clicked(self):
        self.process.join()

        for data in self.return_dict.keys():
            print(data)

        for data in self.return_dict.values():
            print(len(data))


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
