import glob

import Img_Data_Process as IDP
from PIL import Image
import os
import cv2  # OpenCV import
import numpy as np
import shutil
from threading import Thread
from multiprocessing import Process, Queue


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)


def Dj_aaa():
    root = r"C:\Users\USER\Desktop\2021-07-16\PPM6RH0AA"
    file_1 = r"RawImage_0.jpg"
    filr_2 = r"RawImage_0r (2).jpg"
    file_name_1 = os.path.join(root, file_1)
    file_name_2 = os.path.join(root, filr_2)
    color_1 = cv2.imread(file_name_1, cv2.IMREAD_COLOR)
    color_2 = cv2.imread(file_name_2, cv2.IMREAD_COLOR)

    print(color_1.shape)
    print(color_2.shape)

    print(color_1[0:100, 0, 0])
    print(color_2[0:100, 0, 0])

    print((color_1[0:100, 0, 0] == color_2[0:100, 0, 0]))
    print(np.array_equal(color_1[0:100, 0, 0], color_2[0:100, 0, 0]))

    # print((color_1 == color_2))
def case_0(_co, _dj_c, _path):
    # print(len(os.listdir(path)))
    _img_files = glob.glob(_path + '/*.jpg')
    # print(len(img_files))
    print(_co)

    createFolder_path = os.path.join(_path, 'output_Python')
    try:
        if _dj_c == 1:

            _img_files = [_img_files[_dj_c * _co - _dj_c]]
            # print(_img_files)
        elif _dj_c > 1:
            _img_files = _img_files[_dj_c * _co - _dj_c: _dj_c * _co]
            # for _ck_file in _img_files:
            #     print("process-", _co, "  file name: ", _ck_file)
    except:
        print('\033[31m' + str(_co) + 'exit()' + '\033[0m')
        return 0

    try:
        for file_name in _img_files:
            # image read
            color = cv2.imread(file_name, cv2.IMREAD_COLOR)

            data_name = os.path.basename(file_name).rstrip('.jpg')
            # print(os.path.basename(file_name).rstrip('.jpg')) # RawImage_1480
            # print(color.shape) # (13800, 7300, 3)
            print(data_name)

            for count in range(11):
                _ys = 1000
                save_file = color[0 + _ys * count: 2000 + _ys * count, 1200:6100, :]
                # print(save_file.shape)

                name = os.path.join(createFolder_path, data_name + "_" + str(count) + ".jpg")
                cv2.imwrite(name, save_file)
    except:
        print('\033[31m' + str(_co) + 'exit()' + '\033[0m')
        return 0

def case_1(_co, _dj_c, _path):
    # print(len(os.listdir(path)))
    _img_files = glob.glob(_path + '/*.jpg')
    # print(len(img_files))
    print(_co)

    createFolder_path = os.path.join(_path, 'output_Python')
    try:
        if _dj_c == 1:

            _img_files = [_img_files[_dj_c * _co - _dj_c]]
            # print(_img_files)
        elif _dj_c > 1:
            _img_files = _img_files[_dj_c * _co - _dj_c: _dj_c * _co]
            # for _ck_file in _img_files:
            #     print("process-", _co, "  file name: ", _ck_file)
    except:
        print('\033[31m' + str(_co) + 'exit()' + '\033[0m')
        return 0

    try:
        for file_name in _img_files:
            # image read
            color = cv2.imread(file_name, cv2.IMREAD_COLOR)

            data_name = os.path.basename(file_name).rstrip('.jpg')
            # print(os.path.basename(file_name).rstrip('.jpg')) # RawImage_1480
            # print(color.shape) # (13800, 7300, 3)
            print(data_name)

            for count in range(9):
                _ys = 1515
                save_file = color[0 + _ys * count: 3030 + _ys * count, 0:7022, :]
                # print(save_file.shape)

                name = os.path.join(createFolder_path, data_name + "_" + str(count) + ".jpg")
                cv2.imwrite(name, save_file)
    except:
        print('\033[31m' + str(_co) + 'exit()' + '\033[0m')
        return 0

def case_2(_co, _dj_c, _path):
    # print(len(os.listdir(path)))
    _img_files = glob.glob(_path + '/*.jpg')
    # print(len(img_files))
    print(_co)

    createFolder_path = os.path.join(_path, 'output_Python')
    try:
        if _dj_c == 1:

            _img_files = [_img_files[_dj_c * _co - _dj_c]]
            # print(_img_files)

        elif _dj_c > 1:
            _img_files = _img_files[_dj_c * _co - _dj_c: _dj_c * _co]
            # for _ck_file in _img_files:
            #     print("process-", _co, "  file name: ", _ck_file)

    except:
        print('\033[31m' + str(_co) + 'exit()' + '\033[0m')
        return 0

    try:
        for file_name in _img_files:
            # image read
            color = cv2.imread(file_name, cv2.IMREAD_COLOR)

            data_name = os.path.basename(file_name).rstrip('.jpg')
            # print(os.path.basename(file_name).rstrip('.jpg')) # RawImage_1480
            # print(color.shape) # (13800, 7300, 3)
            print(data_name)

            for count in range(8):
                _ys = 2500
                save_file = color[_ys * count: 5000 + _ys * count, 0:7022, :]
                # print(save_file.shape)

                name = os.path.join(createFolder_path, data_name + "_" + str(count) + ".jpg")
                cv2.imwrite(name, save_file)
    except:
        print('\033[31m' + str(_co) + 'exit()' + '\033[0m')
        return 0

def case_3(_co, _dj_c, _path):
    # print(len(os.listdir(path)))
    _img_files = glob.glob(_path + '/*.jpg')
    # print(len(img_files))
    print(_co)

    createFolder_path = os.path.join(_path, 'output_Python')
    try:
        if _dj_c == 1:

            _img_files = [_img_files[_dj_c * _co - _dj_c]]
            # print(_img_files)

        elif _dj_c > 1:
            _img_files = _img_files[_dj_c * _co - _dj_c: _dj_c * _co]
            # for _ck_file in _img_files:
            #     print("process-", _co, "  file name: ", _ck_file)

    except:
        print('\033[31m' + str(_co) + 'exit()' + '\033[0m')
        return 0

    try:
        for file_name in _img_files:
            # image read
            color = cv2.imread(file_name, cv2.IMREAD_COLOR)

            data_name = os.path.basename(file_name).rstrip('.jpg')
            # print(os.path.basename(file_name).rstrip('.jpg')) # RawImage_1480
            # print(color.shape) # (13800, 7300, 3)
            print(data_name)

            for count in range(9):
                _ys = 3000
                _top_off_set = 0
                _bottom_off_set = 0
                save_file = color[_ys * count + _top_off_set: 6350 + _ys * count - _bottom_off_set, 0:7022, :]
                # print(save_file.shape)

                name = os.path.join(createFolder_path, data_name + "_" + str(count) + ".jpg")
                cv2.imwrite(name, save_file)
    except:
        print('\033[31m' + str(_co) + 'exit()' + '\033[0m')
        return 0

def main(_co, _dj_c, _path):
    case_0(_co, _dj_c, _path)
    # case_1(_co, _dj_c, _path)
    # case_2(_co, _dj_c, _path)
    # case_3(_co, _dj_c, _path)

if __name__ == "__main__":
    path = r'C:\DataSET\ImageData\P-TCP\Original Data\210726\front-bot\2021-07-12\PPM6S31AB\new'
    # print(len(os.listdir(path)))

    createFolder_path = os.path.join(path, 'output_Python')
    createFolder(createFolder_path)

    dj_c = 1

    th1 = Process(target=main, args=(1, dj_c, path))
    th2 = Process(target=main, args=(2, dj_c, path))
    th3 = Process(target=main, args=(3, dj_c, path))
    th4 = Process(target=main, args=(4, dj_c, path))
    th5 = Process(target=main, args=(5, dj_c, path))
    th6 = Process(target=main, args=(6, dj_c, path))
    th7 = Process(target=main, args=(7, dj_c, path))
    th8 = Process(target=main, args=(8, dj_c, path))
    th9 = Process(target=main, args=(9, dj_c, path))
    th10 = Process(target=main, args=(10, dj_c, path))
    th11 = Process(target=main, args=(11, dj_c, path))
    th12 = Process(target=main, args=(12, dj_c, path))
    th13 = Process(target=main, args=(13, dj_c, path))
    th14 = Process(target=main, args=(14, dj_c, path))
    th15 = Process(target=main, args=(15, dj_c, path))
    th16 = Process(target=main, args=(16, dj_c, path))
    th17 = Process(target=main, args=(17, dj_c, path))
    th18 = Process(target=main, args=(18, dj_c, path))
    th19 = Process(target=main, args=(19, dj_c, path))
    th20 = Process(target=main, args=(20, dj_c, path))
    th21 = Process(target=main, args=(21, dj_c, path))

    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
    th6.start()
    th7.start()
    th8.start()
    th9.start()
    th10.start()
    th11.start()
    th12.start()
    th13.start()
    th14.start()
    th15.start()
    th16.start()
    th17.start()
    th18.start()
    th19.start()
    th20.start()
    th21.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()
    th6.join()
    th7.join()
    th8.join()
    th9.join()
    th10.join()
    th11.join()
    th12.join()
    th13.join()
    th14.join()
    th15.join()
    th16.join()
    th17.join()
    th18.join()
    th19.join()
    th20.join()
    th21.join()

    # Dj_aaa()
    # main()
