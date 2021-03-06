# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\ProgrammingFiles\Python\Simple_image_process\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import datetime
import math
import multiprocessing
import random
import sys
import threading
import time
from typing import List

from PyQt5 import QtCore, QtGui, QtWidgets

import Integrated_image_processing as Iip


class Ui_MainWindow(QtWidgets.QMainWindow):
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

        #
        self.remove_files_results: dict = {}

    def setupUi(self, MainWindow):
        print("MainWindow")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(404, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridGroupBox)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.le_datapath = QtWidgets.QLineEdit(self.gridGroupBox)
        self.le_datapath.setObjectName("le_datapath")
        self.gridLayout.addWidget(self.le_datapath, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ckb_subfolders = QtWidgets.QCheckBox(self.gridGroupBox)
        self.ckb_subfolders.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ckb_subfolders.setChecked(True)
        self.ckb_subfolders.setObjectName("ckb_subfolders")
        self.horizontalLayout.addWidget(self.ckb_subfolders)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.gridGroupBox)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_ext = QtWidgets.QLineEdit(self.gridGroupBox)
        self.le_ext.setObjectName("le_ext")
        self.horizontalLayout.addWidget(self.le_ext)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 2)
        self.gridLayout_3.addWidget(self.gridGroupBox, 0, 0, 1, 1)
        self.gridGroupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.gridGroupBox1.setObjectName("gridGroupBox1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridGroupBox1)
        self.gridLayout_2.setContentsMargins(0, 5, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.gridGroupBox1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.le_x_size = QtWidgets.QLineEdit(self.gridGroupBox1)
        self.le_x_size.setObjectName("le_x_size")
        self.horizontalLayout_2.addWidget(self.le_x_size)
        self.label_3 = QtWidgets.QLabel(self.gridGroupBox1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.le_y_size = QtWidgets.QLineEdit(self.gridGroupBox1)
        self.le_y_size.setObjectName("le_y_size")
        self.horizontalLayout_2.addWidget(self.le_y_size)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.gridGroupBox1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.le_Processor_numbers = QtWidgets.QLineEdit(self.gridGroupBox1)
        self.le_Processor_numbers.setObjectName("le_Processor_numbers")
        self.horizontalLayout_4.addWidget(self.le_Processor_numbers)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.txtbw_status = QtWidgets.QTextBrowser(self.gridGroupBox1)
        self.txtbw_status.setObjectName("txtbw_status")
        self.verticalLayout.addWidget(self.txtbw_status)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_main_start = QtWidgets.QPushButton(self.gridGroupBox1)
        self.btn_main_start.setObjectName("btn_main_start")
        self.horizontalLayout_5.addWidget(self.btn_main_start)
        self.btn_main_stop = QtWidgets.QPushButton(self.gridGroupBox1)
        self.btn_main_stop.setObjectName("btn_main_stop")
        self.horizontalLayout_5.addWidget(self.btn_main_stop)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.gridGroupBox1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gridGroupBox.setTitle(_translate("MainWindow", "Data Path"))
        self.ckb_subfolders.setText(_translate("MainWindow", "SubFolders"))
        self.label.setText(_translate("MainWindow", "Ext"))
        self.le_ext.setText(_translate("MainWindow", ".jpg"))
        self.gridGroupBox1.setTitle(_translate("MainWindow", "Check image size and remove"))
        self.label_2.setText(_translate("MainWindow", "X"))
        self.le_x_size.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Y"))
        self.le_y_size.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Processor numbers"))
        self.le_Processor_numbers.setText(_translate("MainWindow", "0"))
        self.btn_main_start.setText(_translate("MainWindow", "Start"))
        self.btn_main_stop.setText(_translate("MainWindow", "Stop"))

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

    def btn_main_start_clicked_process(self, data_path: List[str],
                                       data_ext: str,
                                       sub_folders: str,
                                       size_x: int, size_y: int, number_of_Process: int,
                                       return_dict: dict,
                                       txtbw_status):
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
            process = multiprocessing.Process.apply_async(target=Iip.main, name="btn_process",
                                              args=(task_number, task_list[task_number], size_x, size_y, return_dict,),
                                              daemon=True, callback=self._btn_main_start_clicked_process_callback)
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

    def _btn_main_start_clicked_process_callback(self, results: dict):
        self.remove_files_results: dict = {}
        self.remove_files_results.update(results)

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

        print(self.process.is_alive())

        for data in self.remove_files_results.values():
            number_of_data += len(data)
            for a in data:
                print(a)
        print(number_of_data)


if __name__ == "__main__":
    multiprocessing.freeze_support()  # for multiprocessing other process on windows
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
