from pathlib import Path

from abstract_checker import AbstractChecker


class FolderChecker(AbstractChecker):

    def __init__(self, folder: Path):
        super().__init__(folder)

    def check_exist(self, folder: str, error_code: int) -> 'FolderChecker':
        if not self._path.exists():
            print('Error - ' + folder + ' folder does not exist.' + str(self._path))
            exit(error_code)

        return self

    def identical(self, folder_checker: 'FolderChecker') -> bool:
        return Path.samefile(self._path, folder_checker._path)
