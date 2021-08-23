import shutil
import glob
import math
from multiprocessing import Process
import datetime
import os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)


def file_rename_list_path(_task_number, _number_of_task, _path, _output_folder_dir):
    file_name_add = int((_task_number-1) * _number_of_task)

    for number, file_name in enumerate(_path):
        dir_name = os.path.dirname(file_name)
        os.rename(file_name, os.path.join(dir_name, _output_folder_dir, str(file_name_add+number) + '.jpg'))

    # print('\033[31m' + str(_task_number) + 'exit()' + '\033[0m')
    return 0


def main(_task_number, _number_of_task, _path, _output_folder_dir):
    print("Start Process: ", _task_number)
    file_rename_list_path(_task_number, _number_of_task, _path, _output_folder_dir)


if __name__ == '__main__':

    create_output_folder_name = 'output_python'

    # 데이터 경로 설정 -- User setting
    start = datetime.datetime.now()

    path_list = [r"C:\DataSET\P-TCP\Crop Data\center-top1\a\1",
                 r"C:\DataSET\P-TCP\Crop Data\center-top1\a\2",
                 r"C:\DataSET\P-TCP\Crop Data\center-top1\a\3",
                 r"C:\DataSET\P-TCP\Crop Data\center-top1\a\4",
                 r"C:\DataSET\P-TCP\Crop Data\center-top1\a\5",
                 r"C:\DataSET\P-TCP\Crop Data\center-top1\a\6",
                 r"C:\DataSET\P-TCP\Crop Data\center-top1\a\7",
                 r"C:\DataSET\P-TCP\Crop Data\center-top1\a\8",
                 r"C:\DataSET\P-TCP\Crop Data\center-top1\a\9",
                 r"C:\DataSET\P-TCP\Crop Data\center-top1\a\11",
                 r"C:\DataSET\P-TCP\Crop Data\center-top1\a\12",
                 ]
    jpg_files = []

    for path in path_list:
        jpg_files = jpg_files + glob.glob(os.path.join(path, '*.jpg'))

    number_of_data = len(jpg_files)
    print("number_of_data : " + str(number_of_data))

    number_of_Process = 50

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
    th26 = Process(target=main, args=(26, number_of_task, jpg_files_list[25], dst))
    th27 = Process(target=main, args=(27, number_of_task, jpg_files_list[26], dst))
    th28 = Process(target=main, args=(28, number_of_task, jpg_files_list[27], dst))
    th29 = Process(target=main, args=(29, number_of_task, jpg_files_list[28], dst))
    th30 = Process(target=main, args=(30, number_of_task, jpg_files_list[29], dst))
    th31 = Process(target=main, args=(31, number_of_task, jpg_files_list[30], dst))
    th32 = Process(target=main, args=(32, number_of_task, jpg_files_list[31], dst))
    th33 = Process(target=main, args=(33, number_of_task, jpg_files_list[32], dst))
    th34 = Process(target=main, args=(34, number_of_task, jpg_files_list[33], dst))
    th35 = Process(target=main, args=(35, number_of_task, jpg_files_list[34], dst))
    th36 = Process(target=main, args=(36, number_of_task, jpg_files_list[35], dst))
    th37 = Process(target=main, args=(37, number_of_task, jpg_files_list[36], dst))
    th38 = Process(target=main, args=(38, number_of_task, jpg_files_list[37], dst))
    th39 = Process(target=main, args=(39, number_of_task, jpg_files_list[38], dst))
    th40 = Process(target=main, args=(40, number_of_task, jpg_files_list[39], dst))
    th41 = Process(target=main, args=(41, number_of_task, jpg_files_list[40], dst))
    th42 = Process(target=main, args=(42, number_of_task, jpg_files_list[41], dst))
    th43 = Process(target=main, args=(43, number_of_task, jpg_files_list[42], dst))
    th44 = Process(target=main, args=(44, number_of_task, jpg_files_list[43], dst))
    th45 = Process(target=main, args=(45, number_of_task, jpg_files_list[44], dst))
    th46 = Process(target=main, args=(46, number_of_task, jpg_files_list[45], dst))
    th47 = Process(target=main, args=(47, number_of_task, jpg_files_list[46], dst))
    th48 = Process(target=main, args=(48, number_of_task, jpg_files_list[47], dst))
    th49 = Process(target=main, args=(49, number_of_task, jpg_files_list[48], dst))
    th50 = Process(target=main, args=(50, number_of_task, jpg_files_list[49], dst))
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
    th26.start()
    th27.start()
    th28.start()
    th29.start()
    th30.start()
    th31.start()
    th32.start()
    th33.start()
    th34.start()
    th35.start()
    th36.start()
    th37.start()
    th38.start()
    th39.start()
    th40.start()
    th41.start()
    th42.start()
    th43.start()
    th44.start()
    th45.start()
    th46.start()
    th47.start()
    th48.start()
    th49.start()
    th50.start()
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
    th26.join()
    th27.join()
    th28.join()
    th29.join()
    th30.join()
    th31.join()
    th32.join()
    th33.join()
    th34.join()
    th35.join()
    th36.join()
    th37.join()
    th38.join()
    th39.join()
    th40.join()
    th41.join()
    th42.join()
    th43.join()
    th44.join()
    th45.join()
    th46.join()
    th47.join()
    th48.join()
    th49.join()
    th50.join()

    end = datetime.datetime.now()
    result = end - start
    print(result)
    print(result.microseconds / 1000000)
