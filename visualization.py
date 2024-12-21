import matplotlib.pyplot as plt
import numpy as np
import cv2

def show_histogram(histogram: np.ndarray) -> None:
    """
    Показать гистограмму
    histogram: гистограмма для отображения
    """
    plt.figure()
    plt.title("Гистограмма")
    plt.xlabel("Значение")
    plt.ylabel("Частота")
    plt.plot(histogram)
    plt.xlim([0, 256])
    plt.show()

def show_images(image1: np.ndarray, image2: np.ndarray) -> None:
    """
    Показать изображения
    image1: первое изображение для отображения
    image2: второе изображение для отображения
    """
    plt.figure(figsize=(10, 5))  

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))  
    plt.title("Оригинальное изображение")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))  
    plt.title("Обрезанное изображение")
    plt.axis("off")

    plt.show()