import datetime
import math
import multiprocessing
import random
import sys
import threading
import time
from typing import List

from PyQt5 import uic
from PyQt5.QtWidgets import *

import Integrated_image_processing as Iip

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("main.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.manager = multiprocessing.Manager()
        self.return_dict = self.manager.dict()
        self.process = multiprocessing.Process.__init__(self)
        self.thread = threading.Thread.__init__(self)
        self.thread_alive = threading.Thread.__init__(self)

        # 버튼
        self.btn_main_start.clicked.connect(self.btn_main_start_clicked)
        self.btn_main_stop.clicked.connect(self.btn_main_stop_clicked)

    def btn_main_start_clicked(self):
        self.return_dict = self.manager.dict()

        try:
            self.thread = threading.Thread(target=self.btn_main_start_clicked_process,
                                           args=(self.le_datapath.text(),
                                                 self.le_ext.text(),
                                                 self.ckb_subfolders.isChecked(),
                                                 int(self.le_x_size.text()),
                                                 int(self.le_y_size.text()),
                                                 int(self.le_Processor_numbers.text()),
                                                 self.return_dict,
                                                 self.txtbw_status,))
            self.thread_alive = threading.Thread(target=self.btn_main_start_clicked_process_alive,
                                                 args=(self.thread,
                                                       self.btn_main_start))
            self.thread.start()
            self.thread_alive.start()

        except OSError as err:
            print("\033[38;5;9m Thread start failed {} \033[0m".format(1))
            print(err)

        self.btn_main_start.setDisabled(True)

    @staticmethod
    def btn_main_start_clicked_process(data_path: List[str],
                                       data_ext: str,
                                       sub_folders: str,
                                       size_x: int, size_y: int, number_of_Process: int,
                                       return_dict: dict,
                                       txtbw_status, ):
        start = datetime.datetime.now()
        print("Start Thread:\033[38;5;13m {} \033[0m Times : \033[38;5;14m {} \033[0m".format(1, start))

        data_list = [Iip.search_directory(data_path, data_ext, sub_folders)]
        data_list = Iip.list_flatten(data_list)
        random.shuffle(data_list)

        number_of_data = len(data_list)
        number_of_task = math.ceil(number_of_data / number_of_Process)

        print("number of task: \033[38;5;14m {} \033[0m".format(number_of_task), '\n',
              "number of data: \033[38;5;14m {} \033[0m".format(number_of_data))

        task_list = Iip.list_chunk(data_list, number_of_task)
        setting_process = len(task_list)

        print("setting process : \033[38;5;14m {} \033[0m".format(number_of_Process),
              "activate process: \033[38;5;9m {} \033[0m".format(setting_process))

        jobs = []

        for task_number in range(setting_process):
            process = multiprocessing.Process(target=Iip.main,
                                              args=(task_number, task_list[task_number], size_x, size_y, return_dict,))

            jobs.append(process)
            process.start()

        for proc in jobs:
            proc.join()

        number_of_data = 0
        for data in return_dict.values():
            number_of_data = number_of_data + len(data)

        txtbw_status.append("Find data number : {} ".format(number_of_data))

        result = datetime.datetime.now() - start
        print("End Thread: \033[38;5;13m {} \033[0m Times : \033[38;5;14m {} \033[0m".format(1, result))

    @staticmethod
    def btn_main_start_clicked_process_alive(Thread, Button):
        time.sleep(0.5)
        while True:
            if not Thread.is_alive():
                try:
                    Button.setEnabled(True)
                except:
                    pass
                break
            # print('.', end='', flush=True)

    def btn_main_stop_clicked(self):
        # for data in self.return_dict.keys():
        #     print(data)
        number_of_data = 0
        for data in self.return_dict.values():
            number_of_data += len(data)
            for a in data:
                print(a)
        print(number_of_data)


if __name__ == "__main__":
    multiprocessing.freeze_support()  # for multiprocessing other process on windows
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
