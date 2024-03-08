import argparse
from pathlib import Path

from send2trash import send2trash

from file_checker import FileChecker
from folder_checker import FolderChecker


class DuplicateFileRemover:
    __source_folder: Path
    __target_folder: Path

    def __init__(self, source_folder: str, target_folder: str):
        self.__source_folder = Path(source_folder)
        self.__target_folder = Path(target_folder)

    def __recycle_duplicate_file(self, file: Path) -> None:
        target_file = Path(self.__target_folder, file.name)

        if target_file.exists() and FileChecker(file).identical(FileChecker(target_file)):
            send2trash(target_file)
            print(str(target_file) + ' deleted')

        return

    def remove_duplicate_files(self) -> None:
        source_folder_checker = FolderChecker(self.__source_folder).check_exist('Source', 9001)
        target_folder_checker = FolderChecker(self.__target_folder).check_exist('Target', 9002)

        if source_folder_checker.identical(target_folder_checker):
            print('Source and target folders are the same')
            exit(9003)
        else:
            [self.__recycle_duplicate_file(file) for file in self.__source_folder.iterdir()]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove the duplicate files from target folder if they already exist'
                                                 ' in source folder')
    parser.add_argument('source_folder', type=str, help='The folder where to check the files exist')
    parser.add_argument('target_folder', type=str, help='The folder where to remove the duplicate files')
    args = parser.parse_args()
    remover = DuplicateFileRemover(args.source_folder, args.target_folder)
    remover.remove_duplicate_files()
