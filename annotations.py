import csv
import os


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
