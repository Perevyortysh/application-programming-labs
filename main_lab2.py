import argparse
from annotations import create_annotation
from image_downloader import download_images
from image_iterator import ImageIterator


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword")
    parser.add_argument("output_dir")
    parser.add_argument("annotation_file")
    parser.add_argument("--max_images", default=50, type=int)

    return parser.parse_args()


def main():
    try:
        args = parse_args()

        download_images(args.keyword, args.output_dir, args.max_images)
        create_annotation(args.output_dir, args.annotation_file)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
