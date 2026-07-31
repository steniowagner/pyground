from abc import ABC, abstractmethod
from pathlib import Path

from pandas import DataFrame


class FileHandler(ABC):
    def __init__(self, file_path: str):
        self.file_path = Path(file_path).expanduser()

    @abstractmethod
    def read(self) -> DataFrame:
        pass

    @abstractmethod
    def write(self):
        pass
