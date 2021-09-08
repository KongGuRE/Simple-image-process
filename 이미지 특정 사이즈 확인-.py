from datetime import time

from tqdm import tqdm

import Img_Data_Process as IDP
from PIL import Image
import os
import shutil

def all_data_del(_Data_Path_List_1, _img_file_name_list_A, _rz_size_x, _rz_size_y):

    IP_1 = IDP.Img_Data_Loader()
    _Data_Path_List_1, img_file_name_list_A = IP_1.Load_Img_Path(_Data_Path_List_1, _img_file_name_list_A, ck=True)

    rm_file = []

    for File_idx, imgFile in enumerate(tqdm(_Data_Path_List_1)):
        image1 = Image.open(imgFile)
        imag1_size = image1.size
        if imag1_size[0] == _rz_size_x:
            if imag1_size[1] == _rz_size_y:
                None
            else:
                rm_file.append(imgFile)
        else:
            rm_file.append(imgFile)
    print(len(rm_file))

    for a in rm_file:
        print(a)


if __name__ == '__main__':

    # 데이터 경로 설정 -- User setting
    root_path: str = r"C:\DataSET\P-TCP\Crop Data\center-top1"
    # data_1_path: str = r"OK"
    data_2_path: str = r"NG"
    # data_3_path: str = r"Test\OK"
    # data_4_path: str = r"Test\NG"

    # 정상 이미지 사이즈 입력
    rz_size_x = 256
    rz_size_y = 256

    # 하나씩 삭제 -- 삭제가 잘 안됨
    # one_by_one_data_del(root_path, data_1_path, rz_size)
    # 한번에 삭
    # all_data_del(root_path, data_1_path, rz_size_x, rz_size_y)
    all_data_del(root_path, data_2_path, rz_size_x, rz_size_y)
    # all_data_del(root_path, data_3_path, rz_size_x, rz_size_y)
    # all_data_del(root_path, data_4_path, rz_size_x, rz_size_y)
