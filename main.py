from file import File
from scanner import Scanner
from pathlib import Path



def main():
    # file test
    file_path = Path("./tests/test_files/loremipsum.txt")
    lorem = File(file_path)
    print(f'FILE: {lorem}')
    # scanner test
    dir_path = Path("./tests/test_files/")
    scan = Scanner(dir_path)
    scan.scan()
    print(f'SCAN: {scan}')



if __name__ == "__main__":
    main()