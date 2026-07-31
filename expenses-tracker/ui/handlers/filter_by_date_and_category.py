import pandas as pd
from ui.handlers.ui_handler import UiHandler


class FilterByDateAndCategory(UiHandler):
    def _show_menu(self):
        start_date = input(
            "Type the start-date (yyyy-mm-dd) (press enter to leave it blank):"
        )
        end_date = input(
            "Type the end-date (yyyy-mm-dd) (press enter to leave it blank):"
        )
        category = input("Type the category (press enter to leave it blank):")
        return {
            "category": category,
            "start_date": start_date,
            "end_date": end_date,
        }

    def _filter_by_category(self, expenses_df: pd.DataFrame, category: str):
        return expenses_df[expenses_df["category"] == category]

    def _filter_by_date(
        self, expenses_df: pd.DataFrame, start_date: str, end_date: str
    ):
        filtered_df = expenses_df.copy()

        if start_date:
            parsed_start_date = pd.to_datetime(start_date)
            filtered_df = filtered_df[filtered_df["date"] >= parsed_start_date]

        if end_date:
            parsed_end_date = pd.to_datetime(end_date)
            filtered_df = filtered_df[filtered_df["date"] <= parsed_end_date]

        return filtered_df

    def execute(self, expenses_df):
        global filtered_df
        filtered_df = expenses_df

        options = self._show_menu()
        category = options.get("category", None)
        if category:
            filtered_df = self._filter_by_category(
                expenses_df=expenses_df, category=category
            )

        start_date = options.get("start_date", None)
        end_date = options.get("end_date", None)
        if start_date or end_date:
            filtered_df = self._filter_by_date(
                start_date=start_date, end_date=end_date, expenses_df=filtered_df
            )

        output_message = (
            "No results for your filter"
            if filtered_df.empty
            else filtered_df.reset_index()
        )
        print(f"\n{output_message}")
