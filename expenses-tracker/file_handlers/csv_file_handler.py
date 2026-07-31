import csv

import pandas as pd
from constants import EXPENSES_CSV_REQUIRED_COLUMNS
from file_handlers.file_handler import FileHandler


class CSVFileHandler(FileHandler):
    def read(self, config: dict | None = None):
        if config is None:
            config = {}

        dtype = config.get("dtype", None)
        parse_dates = config.get("parse_dates", None)
        date_format = config.get("date_format", None)

        return pd.read_csv(
            self.file_path,
            encoding="utf-8",
            sep=",",
            dtype=dtype,
            parse_dates=parse_dates,
            date_format=date_format,
        )

    def write(self, row: dict):
        with open(self.file_path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=EXPENSES_CSV_REQUIRED_COLUMNS)
            w.writerow(row)
