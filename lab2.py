import os
import csv
import argparse
from icrawler.builtin import GoogleImageCrawler


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword")
    parser.add_argument("output_dir")
    parser.add_argument("annotation_file")
    parser.add_argument("--max_images", default=50, type=int)

    return parser.parse_args()


def download_images(keyword: str, output_dir: str, max_num_images: int = 50) -> None:
    """
    Скачивание изображений
    keyword: ключевое слово для поиска
    output_dir: путь к папке для сохранения изображений
    annotation_file: путь к файлу аннотации
    max_num_images: максимальное количество скачиваемых изображений
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    crawler = GoogleImageCrawler(storage={"root_dir": output_dir})
    crawler.crawl(keyword=keyword, max_num=max_num_images)


def create_annotation(output_dir: str, annotation: str) -> None:
    """
    Создание csv-файла с аннотацией изображений
    annotation: строка, указывающая путь к файлу, в который будет записана аннотация
    """
    with open(annotation, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["absolute_path", "relative_path"])

        for root, _, files in os.walk(output_dir):
            for filename in files:
                abs_path = os.path.abspath(os.path.join(root, filename))
                rel_path = os.path.relpath(os.path.join(root, filename), output_dir)
                writer.writerow([abs_path, rel_path])


class ImageIterator:
    def __init__(self, annotation: str) -> None:
        self.index = 0
        self.items = []
        try:
            with open(annotation, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                self.items = list(reader)
                self.current_index = 0
        except FileNotFoundError as e:
            raise e
        except Exception as e:
            raise e

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.items):
            item = self.items[self.current_index]
            self.current_index += 1
            return item
        else:
            raise StopIteration


def main():
    try:
        args = parse_args()

        download_images(args.keyword, args.output_dir, args.max_images)
        create_annotation(args.output_dir, args.annotation_file)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()