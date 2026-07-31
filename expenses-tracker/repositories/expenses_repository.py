from pathlib import Path

import pandas as pd
from constants import EXPENSES_CSV_REQUIRED_COLUMNS
from file_handlers.file_handler_factory import create_file_handler


class ExpensesRepository:
    def __init__(self):
        self.df = pd.DataFrame()

    def _run_file_checks(self, path: Path):
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        if not path.is_file():
            raise ValueError(f"Path is not a file: {path}")

    def _run_df_checks(self, dataframe: pd.DataFrame):
        required_columns = set(EXPENSES_CSV_REQUIRED_COLUMNS)
        missing_columns = required_columns - set(dataframe.columns)
        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            error_message = f"Missing required columns: {missing}"
            raise ValueError(error_message)

    def load(self, str_path: str):
        path = Path(str_path).expanduser()
        self._run_file_checks(path)

        handler = create_file_handler(path)
        df = handler.read()
        self._run_df_checks(df)
        self.df = df
        self.df["date"] = pd.to_datetime(self.df["date"], errors="raise")
