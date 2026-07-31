from pandas import DataFrame
from ui.handlers.ui_handler import UiHandler


class FindSmallestTransaction(UiHandler):
    def execute(self, expenses_df: DataFrame):
        smallest_transaction = expenses_df[
            expenses_df["amount"] == expenses_df["amount"].min()
        ]
        print("\n", smallest_transaction.reset_index())
