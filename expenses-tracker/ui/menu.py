from typing import Final

from pandas import DataFrame
from ui.handlers.calculate_total_spending import CalculateTotalSpending
from ui.handlers.export_monthly_summary import ExportMonthlySummary
from ui.handlers.filter_by_date_and_category import FilterByDateAndCategory
from ui.handlers.find_largest_transaction import FindLargestTransaction
from ui.handlers.find_smallest_transaction import FindSmallestTransaction
from ui.handlers.group_expenses_by_category import GroupExpensesByCategory
from ui.handlers.ui_handler import UiHandler
from ui.utils import show_header_message

EXIT_KEY: Final[str] = "E"


class Menu:
    def __init__(self):
        self._handlers: dict[str, UiHandler] = {
            "1": CalculateTotalSpending(),
            "2": GroupExpensesByCategory(),
            "3": FilterByDateAndCategory(),
            "4": FindLargestTransaction(),
            "5": FindSmallestTransaction(),
            "6": ExportMonthlySummary(),
        }

    def _show_main_menu(self) -> None:
        print("1 - Calculate total spending")
        print("2 - Group expenses by category")
        print("3 - Filter by date and category")
        print("4 - Find the largest transaction")
        print("5 - Find the smallest transaction")
        print("6 - Export a monthly summary")
        print("E - Exit")

    def _execute_option(self, option: str, expenses_df: DataFrame) -> None:
        handler = self._handlers.get(option)
        if not handler:
            return
        handler.execute(expenses_df)

    def run(self, expenses_df: DataFrame) -> None:
        while True:
            show_header_message("My Expenses")
            self._show_main_menu()
            option = input()
            if option.upper() == EXIT_KEY:
                break
            print()
            self._execute_option(option, expenses_df)
