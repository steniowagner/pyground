from pathlib import Path

import pandas as pd
from constants import EXPENSES_CSV_REQUIRED_COLUMNS
from file_handlers.file_handler_factory import create_file_handler


class ExpensesRepository:
    def __init__(self):
        self._df = pd.DataFrame()

    @property
    def df(self) -> pd.DataFrame:
        return self._df.copy()

    def _run_file_checks(self, path: Path) -> None:
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {path}")

    def _normalize_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        normalized: pd.DataFrame = df.copy()

        normalized["date"] = pd.to_datetime(normalized["date"], errors="raise")

        normalized["amount"] = pd.to_numeric(normalized["amount"], errors="raise")

        normalized["description"] = (
            normalized["description"].astype("string").str.strip()
        )

        normalized["category"] = normalized["category"].astype("string").str.strip()

        return normalized

    def _run_df_checks(self, dataframe: pd.DataFrame) -> None:
        required_columns = set(EXPENSES_CSV_REQUIRED_COLUMNS)
        missing_columns = required_columns - set(dataframe.columns)
        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            error_message = f"Missing required columns: {missing}"
            raise ValueError(error_message)

    def load(self, path: Path) -> None:
        self._run_file_checks(path)

        handler = create_file_handler(path)
        df = self._normalize_dataframe(handler.read())
        self._run_df_checks(df)
        self._df = df
