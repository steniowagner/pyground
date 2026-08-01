from abc import ABC, abstractmethod

from pandas import DataFrame


class UiHandler(ABC):
    @abstractmethod
    def execute(self, expenses_df: DataFrame) -> None: ...
