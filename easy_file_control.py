import glob
import os
from typing import List


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

def search_file(_directory: str, _file: str, _all_sub_folders: bool = False) -> bool:
    """서브 폴더에서 까지 특정 파일 찾기 함수.

    Args:
        _directory: main directory path 설졍
        _file: 찾을 파일 이름 확장자 포함
        _all_sub_folders: 하위 폴더까지 검색하려면 True
    Returns:
        파일이 있으면 True, 없으면 False 를 반환.
    """
    _task_path_list = []
    if _all_sub_folders:
        try:
            for (_path, _dir, _files) in os.walk(_directory):
                for filename in _files:
                    if filename == _file:
                        return True
                        # print("%s" % (os.path.join(_path, filename)))
                    else:
                        pass
        except PermissionError:
            pass
        return False

    else:
        _task_path_list = glob.glob(os.path.join(_directory, _file))
        if len(_task_path_list) == 0:
            return False
        else:
            return True

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

# if __name__ == '__main__':
#     print(search_file(r"C:\ProgrammingFiles\Python\Simple_image_process\python_", "1.jpg", False))
