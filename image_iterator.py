import csv


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
