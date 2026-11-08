from file import File
from scanner import Scanner
from pathlib import Path


def main():
    # test paths
    file_path = Path("./tests/test_files/loremipsum.txt")
    dir_path = Path("./tests/test_files/")

    # file test
    file_file = File(file_path, dir_path)
    print(f'FILE: {file_file}')
    # file test: will fail
    #dir_file = File(dir_path, dir_path)
    #print(f'File: {dir_file}')
    
    # scanner test
    dir_scan = Scanner(dir_path)
    dir_scan.scan()
    print(f'SCAN: {scan}')
    # Will throw exception
    #file_scan = Scanner(file_path)
    #file_scan.scan()
    #print(f'DirScan: {dir_scan}')


if __name__ == "__main__":
    main()