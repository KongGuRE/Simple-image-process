import shutil
import glob
import math
from multiprocessing import Process
import datetime

def file_copy2(_path, _dst):
    shutil.copy2(_path, _dst)

def directory_copy(_src, _dst):
    shutil.copytree(_src, _dst)

def file_copy_list_path(_task_number, _number_of_task, _path, _dst):
    try:
        for file_name in _path:
            shutil.copy2(file_name, _dst)
    except:
        print('\033[31m' + str(_task_number) + 'exit()' + '\033[0m')
        return 0

def path_type_detector(_number_of_Process, _path_data):
    if type(_path_data) == list:
        _jpg_files = []

        for _path in _path_data:
            _jpg_files = _jpg_files + glob.glob(_path + '/*.jpg')

        _number_of_data = len(_jpg_files)
        print(_number_of_data)

        _number_of_Process = 25

        print(math.ceil(_number_of_data /  _number_of_Process))
        _number_of_task = math.ceil(_number_of_data /  _number_of_Process)

        _jpg_files_list = []
        for task_number in range(1,  _number_of_Process + 1):
            if number_of_task == 1:
                _jpg_files_list.append([_jpg_files[number_of_task * task_number - number_of_task]])

            elif number_of_task > 1:
                _jpg_files_list.append(
                    _jpg_files[number_of_task * task_number - number_of_task: number_of_task * task_number])

def main(_task_number, _number_of_task, _path, _dst):
    print("Start Process: ", _task_number)
    file_copy_list_path(_task_number, _number_of_task, _path, _dst)


if __name__ == '__main__':
    # 데이터 경로 설정 -- User setting
    start = datetime.datetime.now()

    path_list = [r"C:\DataSET\ImageData\Center Top 성능 테스트\OK\1",
                 r"C:\DataSET\ImageData\Center Top 성능 테스트\OK\2",
                 r"C:\DataSET\ImageData\Center Top 성능 테스트\OK\3",
                 r"C:\DataSET\ImageData\Center Top 성능 테스트\OK\4",
                 r"C:\DataSET\ImageData\Center Top 성능 테스트\OK\5",
                 r"C:\DataSET\ImageData\Center Top 성능 테스트\OK\6",
                 r"C:\DataSET\ImageData\Center Top 성능 테스트\OK\7",
                 r"C:\DataSET\ImageData\Center Top 성능 테스트\OK\8"]

    dst: str = r"C:\DataSET\ImageData\Center Top 성능 테스트\OK"

    jpg_files = []

    for path in path_list:
        jpg_files = jpg_files + glob.glob(path + '/*.jpg')

    number_of_data = len(jpg_files)
    print(number_of_data)

    number_of_Process = 25

    print(math.ceil(number_of_data / number_of_Process))
    number_of_task = math.ceil(number_of_data / number_of_Process)

    jpg_files_list = []
    for task_number in range(1, number_of_Process + 1):
        if number_of_task == 1:
            jpg_files_list.append([jpg_files[number_of_task * task_number - number_of_task]])

        elif number_of_task > 1:
            jpg_files_list.append(
                jpg_files[number_of_task * task_number - number_of_task: number_of_task * task_number])

    th1 = Process(target=main, args=(1, number_of_task, jpg_files_list[0], dst))
    th2 = Process(target=main, args=(2, number_of_task, jpg_files_list[1], dst))
    th3 = Process(target=main, args=(3, number_of_task, jpg_files_list[2], dst))
    th4 = Process(target=main, args=(4, number_of_task, jpg_files_list[3], dst))
    th5 = Process(target=main, args=(5, number_of_task, jpg_files_list[4], dst))
    th6 = Process(target=main, args=(6, number_of_task, jpg_files_list[5], dst))
    th7 = Process(target=main, args=(7, number_of_task, jpg_files_list[6], dst))
    th8 = Process(target=main, args=(8, number_of_task, jpg_files_list[7], dst))
    th9 = Process(target=main, args=(9, number_of_task, jpg_files_list[8], dst))
    th10 = Process(target=main, args=(10, number_of_task, jpg_files_list[9], dst))
    th11 = Process(target=main, args=(11, number_of_task, jpg_files_list[10], dst))
    th12 = Process(target=main, args=(12, number_of_task, jpg_files_list[11], dst))
    th13 = Process(target=main, args=(13, number_of_task, jpg_files_list[12], dst))
    th14 = Process(target=main, args=(14, number_of_task, jpg_files_list[13], dst))
    th15 = Process(target=main, args=(15, number_of_task, jpg_files_list[14], dst))
    th16 = Process(target=main, args=(16, number_of_task, jpg_files_list[15], dst))
    th17 = Process(target=main, args=(17, number_of_task, jpg_files_list[16], dst))
    th18 = Process(target=main, args=(18, number_of_task, jpg_files_list[17], dst))
    th19 = Process(target=main, args=(19, number_of_task, jpg_files_list[18], dst))
    th20 = Process(target=main, args=(20, number_of_task, jpg_files_list[19], dst))
    th21 = Process(target=main, args=(21, number_of_task, jpg_files_list[20], dst))
    th22 = Process(target=main, args=(22, number_of_task, jpg_files_list[21], dst))
    th23 = Process(target=main, args=(23, number_of_task, jpg_files_list[22], dst))
    th24 = Process(target=main, args=(24, number_of_task, jpg_files_list[23], dst))
    th25 = Process(target=main, args=(25, number_of_task, jpg_files_list[24], dst))
    # process run
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
    th22.start()
    th23.start()
    th24.start()
    th25.start()
    # process join
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
    th22.join()
    th23.join()
    th24.join()
    th25.join()

    end = datetime.datetime.now()
    result = end - start
    print(result)
    print(result.microseconds / 1000000)

