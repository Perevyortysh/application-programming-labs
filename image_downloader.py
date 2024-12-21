import os
from icrawler.builtin import GoogleImageCrawler


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
