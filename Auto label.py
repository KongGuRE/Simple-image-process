import glob
import os
import shutil
from typing import List
import logging
from logging.config import dictConfig



dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'failed copy file.log',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})


class provisional_auto_label:

    def __init__(self):
        None

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def def_data_read(_data_path: str) -> dir:
        # 파일 읽기
        with open(_data_path) as f:
            lines = f.readlines()
            start_number: int = 0
            end_number: int = 0
            start_find_detector: bool = False
            dir_key_find_detector: bool = False
            file_data: dict = {}

            for number, line in enumerate(lines):
                line = line.strip()

                if dir_key_find_detector:
                    if line == str("ENDSEC"):
                        # print("{}, count: \033[38;5;14m {} \033[0m line: \033[38;5;14m {} \033[0m {}"
                        #       .format("1", number, line, line == "ENDSEC"))
                        end_number = number
                        dir_key_find_detector = False
                        break
                    else:
                        line_data_list = line.strip().split(",")
                        for line_data_list_number, dir_key in enumerate(file_data.keys()):
                            file_data["{}".format(dir_key)].append(line_data_list[line_data_list_number])
                else:
                    if line == "DEFECT":
                        # print("{}, count: \033[38;5;14m {} \033[0m line: \033[38;5;14m {} \033[0m {}"
                        #       .format("2", number, line, line == "DEFECT"))
                        start_find_detector = True

                    elif start_find_detector:
                        start_number = number
                        start_find_detector = False
                        dir_key_find_detector = True
                        # print(line.strip().split(","))
                        for data in line.strip().split(","):
                            file_data["{}".format(data)] = []
        return file_data

    def read_def_file_and_Auto_labeling_custom(self, _data_dir_path):
        def_files_list = self.search_directory(_data_dir_path, ".def", _all_sub_folders=True)

        failed_copy_file = []

        for def_File in def_files_list:
            print("files: \033[38;5;14m {} \033[0m".format(def_File))
            print("files dir name: \033[38;5;14m {} \033[0m".format(os.path.dirname(def_File)))

            logging.debug("files: \033[38;5;14m {} \033[0m".format(def_File))
            logging.debug("files dir name: \033[38;5;14m {} \033[0m".format(os.path.dirname(def_File)))

            def_files_dir_name = os.path.dirname(def_File)
            def_files_data = self.def_data_read(def_File)

            for data_number in range(len(def_files_data["NO"])):
                # print(os.path.join(classification_data_path, def_files_data["VISIONTYPE"][data_number]))
                classification_data_path = os.path.join(def_files_dir_name, "python_classification")

                VISIONTYPE_data_path = os.path.join(classification_data_path, def_files_data["VISIONTYPE"][data_number])

                if def_files_data["VERIFY"][data_number] == '':
                    pass
                    # VERIFY_data_path = os.path.join(VISIONTYPE_data_path, "Not defined")
                else:
                    VERIFY_data_path = os.path.join(VISIONTYPE_data_path, def_files_data["VERIFY"][data_number])

                    DEFECTNAME_data_path = os.path.join(VERIFY_data_path, def_files_data["DEFECTNAME"][data_number])

                    copy_file_path = DEFECTNAME_data_path

                    self.createFolder(copy_file_path)

                    # print(copy_file_path)

                    expect_copy_data = os.path.join(def_files_dir_name, "Images",
                                                    def_files_data["VISIONTYPE"][data_number],
                                                    def_files_data["COLORIMAGE"][data_number]
                                                    )

                    try:
                        shutil.copy2(expect_copy_data, copy_file_path)
                    except:
                        failed_copy_file.append(expect_copy_data)

            for data in failed_copy_file:
                print(data)
                logging.debug(data)


if __name__ == '__main__':
    start = provisional_auto_label()
    start.read_def_file_and_Auto_labeling(r"C:\DataSET\3호기 미분류 이미지")
