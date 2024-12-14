import argparse
import re


def parse_file_path() -> str:
    """
    Получить путь к файлу

    Returns:
        str путь к файлу
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    args = parser.parse_args()

    return args.file


def read_from_file(file: str) -> str:
    """
    Прочитать содержимое файла

    Args:
        file: путь к файлу

    Returns:
        str содержимое файла
    """
    with open(file, "r", encoding="utf-8") as f:
        return f.read()


def get_unique_woman_names(data: str) -> list[str]:
    """
    Получить уникальные имена женщин, начинающиеся на А

    Args:
        data: текст

    Returns:
        list[str]: уникальные имена женщин, начинающиеся на А
    """
    pattern = r"Имя: (А.*)\nПол: Ж" 
    return list(set(re.findall(pattern, data)))


def main():
    filepath = parse_file_path()

    data = read_from_file(filepath)

    woman_names = get_unique_woman_names(data)

    print(*woman_names, sep=", ")


if __name__ == "__main__":
    main()