import shutil
import glob
import math
from multiprocessing import Process
import datetime
import os
from tqdm import tqdm


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)


def file_rename_list_path(_task_number, _number_of_task, _path, _output_folder_dir):
    file_name_add = int((_task_number-1) * _number_of_task)

    for number, file_name in enumerate(tqdm(_path)):
        dir_name = os.path.dirname(file_name)
        shutil.move(file_name, os.path.join(dir_name, _output_folder_dir, str(file_name_add+number).zfill(7) + '.jpg'))

    # print('\033[31m' + str(_task_number) + 'exit()' + '\033[0m')
    return 0


def main(_task_number, _number_of_task, _path, _output_folder_dir):
    print("Start Process: ", _task_number)
    file_rename_list_path(_task_number, _number_of_task, _path, _output_folder_dir)


if __name__ == '__main__':

    create_output_folder_name = 'output_python'

    # 데이터 경로 설정 -- User setting
    start = datetime.datetime.now()

    path_list = [r"C:\20210818\teain-dataset\rear-top\Test\NG"]
    jpg_files = []

    all_sub_folders = False

    if all_sub_folders:
        for path in path_list:
            jpg_files = jpg_files + glob.glob(os.path.join(path, '**/*.jpg'))
            createFolder(os.path.join(path, create_output_folder_name))
    else:
        for path in path_list:
            jpg_files = jpg_files + glob.glob(os.path.join(path, '*.jpg'))
            createFolder(os.path.join(path, create_output_folder_name))

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

    dst = create_output_folder_name

    main(1, number_of_task, jpg_files_list[0], dst)

    end = datetime.datetime.now()
    result = end - start
    print(result)
    print(result.microseconds / 1000000)
