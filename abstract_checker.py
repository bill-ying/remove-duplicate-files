from abc import ABC, abstractmethod
from pathlib import Path


class AbstractChecker(ABC):
    _path: Path

    @abstractmethod
    def __init__(self, path: Path):
        self._path = path

    @abstractmethod
    def identical(self, checker: 'AbstractChecker') -> bool:
        pass
