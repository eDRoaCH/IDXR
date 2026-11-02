from file import File
from pathlib import Path

def add_path(path):
    pass

def scan_path(path):
    for item  in path.iterdir():
        if item.is_file():
            pass

def main():
    file_path = Path("./tests/test_files/loremipsum.txt")
    lorem = File(file_path)
    print(lorem)


if __name__ == "__main__":
    main()