from pandas import DataFrame
from ui.handlers.ui_handler import UiHandler


class GroupExpensesByCategory(UiHandler):
    def execute(self, expenses_df: DataFrame):
        categories = set()

        for _, expense in expenses_df.iterrows():
            category = expense.get("category")
            if category is not None:
                categories.add(category)

        print("Categories:")
        for category in sorted(categories):
            print(f"- {category}")
