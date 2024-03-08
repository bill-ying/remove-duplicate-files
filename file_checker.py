import hashlib
from pathlib import Path

from abstract_checker import AbstractChecker


class FileChecker(AbstractChecker):
    def __init__(self, file: Path):
        super().__init__(file)

    def __get_file_hash(self) -> str:
        hash_sha256 = hashlib.sha256()

        with open(self._path, 'rb') as temp_file:
            chunk = 0

            while chunk != b'':
                chunk = temp_file.read(1024)
                hash_sha256.update(chunk)

        return hash_sha256.hexdigest()

    def identical(self, file_checker: 'FileChecker') -> bool:
        return file_checker._path.stat().st_size == self._path.stat().st_size and \
            self.__get_file_hash() == file_checker.__get_file_hash()
