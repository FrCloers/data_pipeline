from typing import Generator

# ETL - Pipeline: extract, transform, load.
def read_large_dataset(file_name: str) -> Generator:
    with open(file_name) as f:          #f ist eine Iterator, welchen ich zeilenweise auslesen kann
        for line in f:
            yield line

def split_lines(file_generator: Generator):
    """spliited Zeilen eine Liste (kommasepariert)"""
    result = (line.strip().split(",") for line in file_generator)
    return result


def dictify(list_generator: Generator):
    cols = next(list_generator)
    return (dict(zip(cols, data)) for data in list_generator)

def load_data(file_name: str):
    file_generator = read_large_dataset(file_name)
    split_generator = split_lines(file_generator)
    #print(next(split_generator))
    result = dictify(split_generator)
    return result

