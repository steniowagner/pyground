from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from pandas import DataFrame


class FileHandler(ABC):
    def __init__(self, file_path: str):
        self.file_path = Path(file_path).expanduser()

    @abstractmethod
    def read(self, **kwargs: Any) -> DataFrame: ...

    @abstractmethod
    def write(self) -> None: ...
