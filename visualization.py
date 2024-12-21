import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_histogram(histogram: np.ndarray) -> None:
    """
    Показать RGB гистограмму (заполненную). 
    hist_r: гистограмма красного канала 
    hist_g: гистограмма зеленого канала 
    hist_b: гистограмма синего канала
    """
    plt.figure()
    plt.title(“Гистограмма изображения”) 
    plt.xlabel(“Интенсивность пикселей”) 
    plt.ylabel(“Частота”)
    
    plt.fill_between(range(256), hist_r.flatten(), color='red', alpha=0.6, label='Red РєР°РЅР°Р»')
    plt.fill_between(range(256), hist_g.flatten(), color='green', alpha=0.6, label='Green РєР°РЅР°Р»')
    plt.fill_between(range(256), hist_b.flatten(), color='blue', alpha=0.6, label='Blue РєР°РЅР°Р»')

    plt.xlim([0, 256])
    plt.legend()
    plt.grid(True)
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
