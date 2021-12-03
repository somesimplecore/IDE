from line_profiler_pycharm import profile
from PIL import Image
import numpy as np

img = Image.open(input("Введите имя исходного изображения: "))
mosaicSize = int(input("Введите размер мозаики: "))
input_grayscale = int(input("Введите желаемую градацию серого: "))


@profile
def get_mosaic_img(image, mosaic_size, grayscale):
    """
    Возвращает мозаичную серую картинку из исходной по заданным параметрам
    :param image: исходная картинка
    :param mosaic_size:  размер мозайки
    :param grayscale: градация серого
    :return: картинка в мозаичном виде в градациях серого
    """
    arr = np.array(image)
    height, width = len(arr), len(arr[1])
    for i in range(0, height, mosaic_size):
        for j in range(0, width, mosaic_size):
            rgb_grey = arr[i:i + mosaic_size, j:j + mosaic_size].sum() // 100 // 3 // grayscale * grayscale
            arr[i:i + mosaic_size, j:j + mosaic_size] = rgb_grey
    return Image.fromarray(arr)


get_mosaic_img(img, mosaicSize, input_grayscale).save(input("Введите имя результирующего изображения: "))
help(get_mosaic_img)