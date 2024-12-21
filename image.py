import cv2
import numpy as np

def read_image(image_path: str) -> np.ndarray:
    """
    Прочитать изображение из файла
    image_path: путь к файлу с изображением
    returns: изображение в виде numpy массива
    """
    image = cv2.imread(image_path)
    if image is None:
        raise Exception(f"Ошибка при чтении изображения: {image_path}")
    return image


def calculate_histogram(image: np.ndarray) -> np.ndarray:
    """
    Вычислить гистограмму для изображения
    image: изображение для вычисления гистограммы
    returns: гистограмма для изображения
    """
    return cv2.calcHist([image], [0], None, [256], [0, 256])

def crop_image(image: np.ndarray, new_dimensions: tuple[int, int]) -> np.ndarray:
    """
    Обрезать изображение
    image: изображение
    new_dimensions: новая ширина и высота изображения
    Returns: обрезанное изображение
    """
    new_width, new_height = new_dimensions

    cropped_image = image[0:new_height, 0:new_width]
    return cropped_image

def save_image(image: np.ndarray, output_path: str) -> None:
    """
    Сохранить изображение
    """
    try:
        cv2.imwrite(output_path, image)
    except Exception as e:
        raise e