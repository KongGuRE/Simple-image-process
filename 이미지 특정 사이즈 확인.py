import glob
import math
import os

from PIL import Image
from tqdm import tqdm

import Img_Data_Process as IDP


def all_data_del(_Data_Path_List_1, _rz_size_x, _rz_size_y):

    _rm_file = []

    for _File_idx, _imgFile in enumerate(tqdm(_Data_Path_List_1)):
        image1 = Image.open(_imgFile)
        imag1_size = image1.size
        if imag1_size[0] == _rz_size_x:
            if imag1_size[1] == _rz_size_y:
                None
            else:
                _rm_file.append(_imgFile)
        else:
            _rm_file.append(_imgFile)
    print(len(_rm_file))

    for a in _rm_file:
        print(a)


if __name__ == '__main__':

    create_output_folder_name = 'output_python'

    # 데이터 경로 설정 -- User setting
    path_list = [r"C:\20210818\teain-dataset\rear-top\Test"]
    jpg_files = []

    all_sub_folders = True

    if all_sub_folders:
        for path in path_list:
            jpg_files = jpg_files + glob.glob(os.path.join(path, '**/*.jpg'))
    else:
        for path in path_list:
            jpg_files = jpg_files + glob.glob(os.path.join(path, '*.jpg'))

    number_of_data = len(jpg_files)
    print("number_of_data : " + str(number_of_data))

    number_of_Process = 1

    print(math.ceil(number_of_data / number_of_Process))
    number_of_task = math.ceil(number_of_data / number_of_Process)

    jpg_files_list = []
    for task_number in range(1, number_of_Process + 1):
        if number_of_task == 1:
            jpg_files_list.append([jpg_files[number_of_task * task_number - number_of_task]])

        elif number_of_task > 1:
            jpg_files_list.append(
                jpg_files[number_of_task * task_number - number_of_task: number_of_task * task_number])

    # 정상 이미지 사이즈 입력
    rz_size_x = 256
    rz_size_y = 256

    all_data_del(jpg_files_list[0], rz_size_x, rz_size_y)

