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
import shutil
from tqdm import tqdm

import PIL

PIL.Image.MAX_IMAGE_PIXELS = 933120000

def createFolder(_directory):
    """폴더의 유무 확인후 없으면 만들기.

    Args:
        _directory: 확인할 폴더 path
    Returns:
        폴더가 없으면 만들기
    """
    try:
        if not os.path.exists(_directory):
            os.makedirs(_directory)
    except OSError:
        print('Error: Creating directory. ' + _directory)
        exit(1)


def search_directory(_directory: str, _file_ext: str = "*", _all_sub_folders: bool = False) -> List[str]:
    """서브 폴더에서 까지 파일 찾기 함수.

    Args:
        _directory: main directory path 설졍
        _file_ext: 찾을 특정 확장자가 있으면 설정 기본값 ex = ".jpg",
        _all_sub_folders: 하위 폴더까지 검색하려면 True
    Returns:
        폴더 안에 파일의 path를 list로 합니다.
    """
    _task_path_list = []
    if _all_sub_folders:
        try:
            for (_path, _dir, _files) in os.walk(_directory):
                for filename in _files:
                    _ext = os.path.splitext(filename)[-1]
                    if _ext == _file_ext:
                        _task_path_list.append(os.path.join(_path, filename))
                        # print("%s" % (os.path.join(_path, filename)))
                    elif _file_ext == "*":
                        _task_path_list.append(os.path.join(_path, filename))
        except PermissionError:
            pass
    else:
        _task_path_list = glob.glob(os.path.join(_directory, "*" + _file_ext))
    return _task_path_list


def list_flatten(lst: list):
    """2차원 list를 1치원으로 변경하는 함수.

    Args:
        lst: 변경할 2차원 list
    Returns:
        변경된 1차원 list
    """
    _result = []
    for item in lst:
        if type(item) == list:
            _result += list_flatten(item)
        else:
            _result += [item]
    return _result


def list_chunk(lst, n):
    """차원 list를 일정 비율로 자르기.

    Args:
        lst: 변경할 1차원 list
        n : 자를 비율
    Returns:
        변경된 list
    """
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def check_img_size(_file_path_list: list, _rz_size_x: int, _rz_size_y: int) -> List[str]:
    """이미지 사이즈를 확인하여 조건과 다르면 path return.

    Args:
        _file_path_list: 확인할 데이터 path list
        _rz_size_x : x 축 size
        _rz_size_y : y 축 size
    Returns:
        조건과 다른 data path return
    """
    return_data_list: list = []

    for _imgFile in _file_path_list:
        """
        cv2.imread에 오류가 있으면 Image.open으로 사용
        # img_file = Image.open(_imgFile)
        # img_size = img_file.size
        Image.open는 큰 이미지의 경우 못읽어옴.
        """
        # print("files: \033[38;5;14m {} \033[0m".format(_imgFile))
        try:
            img_file = cv2.imread(_imgFile)
            img_size = img_file.shape

            if img_size[1] == _rz_size_x:
                if img_size[0] == _rz_size_y:
                    pass
                else:
                    return_data_list.append(_imgFile)
            else:
                return_data_list.append(_imgFile)
        except:
            try:
                img_file = Image.open(_imgFile)
                img_size = img_file.size
                if img_size[0] == _rz_size_x:
                    if img_size[1] == _rz_size_y:
                        pass
                    else:
                        return_data_list.append(_imgFile)
                else:
                    return_data_list.append(_imgFile)
            except:
                try:
                    return_data_list.append(_imgFile)
                    print("\033[38;5;9mFailed reading File {} \033[0m".format(_imgFile))
                except:
                    pass

    return return_data_list


def del_ex(_file_rm_data_name: list) -> List[str]:
    """파일 list 삭제 함수.

    Args:
        _file_rm_data_name: 삭제할 데이터 path list
    Returns:
        delete failed file path list
    """
    failed_file_list: list = []
    if type(_file_rm_data_name) == list:
        if len(_file_rm_data_name) > 0:
            for _rm_file in _file_rm_data_name:
                try:
                    print("Delete files: \033[38;5;14m {} \033[0m".format(_rm_file))
                    os.unlink(_rm_file)
                except OSError as err:
                    failed_file_list.append(_rm_file)
                    print("\033[38;5;9m Failed to delete file : {} \033[0m".format(_rm_file))
                    # print(err)
    else:
        pass

    return failed_file_list


def check_img_size_and_remove(_file_path_list: list, _rz_size_x: int, _rz_size_y: int) -> List[str]:
    _rm_data_list = check_img_size(_file_path_list, _rz_size_x, _rz_size_y)
    # _rm_data_list = del_ex(_rm_data_list)
    return _rm_data_list


def main(_task_number: int, _file_path_list: list, _rz_size_x: int, _rz_size_y: int, _return_dict: dict):
    print("Start Process: \033[38;5;14m {} \033[0m".format(_task_number))
    start = datetime.datetime.now()

    # print("{} -> data: {}, type: {}".format("_task_number", _task_number, type(_task_number)))
    # print("{} -> data: {}, type: {}".format("_file_path_list", len(_file_path_list), type(_file_path_list)))
    # print("{} -> data: {}, type: {}".format("_rz_size_x", _rz_size_x, type(_rz_size_x)))
    # print("{} -> data: {}, type: {}".format("_rz_size_y", _rz_size_y, type(_rz_size_y)))
    # print("{} -> data: {}, type: {}".format("_return_dict", _return_dict, type(_return_dict)))

    failed_file_list = check_img_size_and_remove(_file_path_list, _rz_size_x, _rz_size_y)
    # failed_file_list = del_ex(failed_file_list)
    _return_dict[_task_number] = failed_file_list

    end = datetime.datetime.now()
    result = end - start
    print("End Process: \033[38;5;13m {} \033[0m Times : \033[38;5;14m {} \033[0m".format(_task_number, result))

    return failed_file_list

if __name__ == "__main__":
    multiprocessing.freeze_support()  # for multiprocessing other process on windows
    start = datetime.datetime.now()

    data_list = [
        search_directory(r"E:\dataset\2호기 미분류 이미지\RT 분류\NG", "*", True),
    ]

    data_list = list_flatten(data_list)
    random.shuffle(data_list)

    number_of_Process = 1
    number_of_data = len(data_list)
    number_of_task = math.ceil(number_of_data / number_of_Process)

    print("number of data: \033[38;5;14m {} \033[0m".format(number_of_data))
    print("number of task: \033[38;5;14m {} \033[0m".format(number_of_task))

    task_list = list_chunk(data_list, number_of_task)
    setting_process = len(task_list)

    print("setting process : \033[38;5;14m {} \033[0m".format(number_of_Process),
          "activate process: \033[38;5;9m {} \033[0m".format(setting_process))

    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    jobs = []

    size_x = 255
    size_y = 256

    for task_number in range(setting_process):
        process = Process(target=main,
                          args=(task_number, task_list[task_number], size_x, size_y, return_dict))
        jobs.append(process)
        process.start()

    for proc in jobs:
        proc.join()

    for data in return_dict.keys():
        print(data)

    for data in return_dict.values():
        print(len(data))

    end = datetime.datetime.now()
    result = end - start
    print("\n")
    print(result)
    print(result.microseconds / 1000000)