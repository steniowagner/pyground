from pandas import DataFrame
from ui.handlers.ui_handler import UiHandler


class FindLargestTransaction(UiHandler):
    def execute(self, expenses_df: DataFrame) -> None:
        largest_transaction = expenses_df[
            expenses_df["amount"] == expenses_df["amount"].max()
        ]
        print("\n", largest_transaction.reset_index())
