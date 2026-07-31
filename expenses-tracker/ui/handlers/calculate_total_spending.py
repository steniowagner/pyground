from pandas import DataFrame
from ui.handlers.ui_handler import UiHandler


class CalculateTotalSpending(UiHandler):
    def execute(self, expenses_df: DataFrame):
        total = expenses_df["amount"].sum()
        print(f"Total spending: $ {total:.2f}")
