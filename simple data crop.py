from PIL import Image
import glob
import os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)
        exit(1)


if __name__ == '__main__':

    new_width = 256
    new_height = 256
    _path = r'C:\DataSET\ImageData\Center Top 성능 테스트\CenterTop2\PPM7V39AA\Crop_Result'

    createFolder_path = os.path.join(_path, 'output_Python')
    createFolder(createFolder_path)

    _img_files = glob.glob(_path + '/*.jpg')

    for Image_name in _img_files:
        image = Image.open(Image_name)
        width, height = image.size  # Get dimensions

        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = (width + new_width) / 2
        bottom = (height + new_height) / 2

        image = image.crop((left, top, right, bottom))

        data_name = os.path.basename(Image_name).rstrip('.jpg')
        name = os.path.join(createFolder_path, data_name + ".jpg")

        print(name)

        image.save(name)
