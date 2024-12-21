import argparse
from image import calculate_histogram, crop_image, read_image, save_image
from visualization_utils import show_histogram, show_images

def parse_args():
    parser = argparse.ArgumentParser(description="Программа обработки изображений")
    parser.add_argument("input_image", help="Путь к файлу с изображением")
    parser.add_argument("output_image", help="Путь для сохранения файла")
    parser.add_argument("width", type=int, help="Ширина изображения")
    parser.add_argument("height", type=int, help="Высота изображения")
    return parser.parse_args()

def main():
    try:
        args = parse_args()

        img = read_image(args.input_image)

        height, width = img.shape[:2]
        print(f"Размеры изображения: Ширина={width}, Высота={height}")

        if args.width < 1 or args.height < 1:
            print("Ширина и высота изображения должна быть больше нуля")
            return

        if args.width > width or args.height > height:
            print(
                "Ширина и высота изображения не должны быть больше размеров изображения"
            )
            return

        hist_r, hist_g, hist_b = calculate_histogram(img)
        show_histogram(hist_r, hist_g, hist_b)

        new_dimensions = (args.width, args.height)
        cropped_img = crop_image(img, new_dimensions)

        show_images(img, cropped_img)
        save_image(cropped_img, args.output_image)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
