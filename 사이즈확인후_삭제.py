from datetime import time

from tqdm import tqdm

import Img_Data_Process as IDP
from PIL import Image
import os
import shutil

def one_by_one_data_del(root_dir, data_path, _rz_size):
    file_rm_data_number: int = 0
    file_rm_data_name: list = []
    for (root, dirs, files) in os.walk(root_dir):
        if root == os.path.join(root_dir, data_path):
            if len(files) > 0:
                for file_name in files:
                    _image_1 = Image.open(os.path.join(root_dir, data_path, file_name))
                    _image_1_size = _image_1.size
                    if _image_1_size[0] == _rz_size:
                        if _image_1_size[1] == _rz_size:
                            None
                        else:
                            os.unlink(file_name, ignore_errors=True)
                            print(file_name)
                            try:
                                os.unlink(file_name, ignore_errors=True)
                                print(file_name)
                            except:
                                print("\033[31m", "File file delete", file_name)
                                file_rm_data_number = file_rm_data_number + 1
                                file_rm_data_name.append(file_name)
                    else:
                        try:
                            os.unlink(file_name,ignore_errors=True)
                            print(file_name)
                        except:
                            print("\033[31m", "File file delete", file_name)
                            file_rm_data_number = file_rm_data_number + 1
                            file_rm_data_name.append(file_name)


def all_data_del(_Data_Path_List_1, _img_file_name_list_A, _rz_size):

    IP_1 = IDP.Img_Data_Loader()
    _Data_Path_List_1, img_file_name_list_A = IP_1.Load_Img_Path(root_path, data_1_path, ck=True)

    rm_file = []

    for File_idx, imgFile in enumerate(tqdm(_Data_Path_List_1)):
        image1 = Image.open(imgFile)
        imag1_size = image1.size
        if imag1_size[0] == _rz_size:
            if imag1_size[1] == _rz_size:
                None
            else:
                rm_file.append(imgFile)
        else:
            rm_file.append(imgFile)
    print(len(rm_file))

    file_rm_data_number: int = 0
    file_rm_data_name: list = []
    for a in rm_file:
        try:
            print(a)
            os.unlink(str(a))
        except:
            try:
                print(a)
                os.unlink(str(a))
            except:
                print("\033[31m", "File file delete", a)
                file_rm_data_number = file_rm_data_number + 1
                file_rm_data_name.append(a)
                return file_rm_data_name

    # print("삭제되지 않은 이미지 파일 갯수: ", file_rm_data_number)
    # print("삭제되지 않은 파일이 있을 경우 프로그램을 한번더 실행해 주세요")

# Press the green button in the gutter to run the script.


if __name__ == '__main__':

    # 데이터 경로 설정 -- User setting
    root_path: str = r"C:\DataSET\ImageData\Center Top 성능 테스트"
    data_1_path: str = r"OK"

    # 정상 이미지 사이즈 입력
    rz_size = 0

    # 하나씩 삭제 -- 삭제가 잘 안됨
    # one_by_one_data_del(root_path, data_1_path, rz_size)
    # 한번에 삭제
    file_rm_data_name = all_data_del(root_path, data_1_path, rz_size)
    if type(file_rm_data_name) == list:
        if len(file_rm_data_name) > 0:
            try:
                for a in file_rm_data_name:
                    os.unlink(a)
                print("File file delete successfully")
            except:
                print("Delete file")
    else:
        None

    # 데이터 읽어오기

    # cv2.imread 가 데이터를 읽어오지 못하는 문제가 있음.
    # 따라서 본 코드는 from PIL import Image 의 Image.open 을 이용하여 데이터를 불러와서 사용


"""    
반복실행 후에도 삭제되지 않는 파일은 windows 상에서 이미 지워진 파일이거나 
특정 외부 proses 잡고 있을 가능성이 있습니다. 
이 경우 파일을 확인 하여 
"""
