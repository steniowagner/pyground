from pathlib import Path

from ui.handlers.ui_handler import UiHandler


class ExportMonthlySummary(UiHandler):
    output_path = "outputs/expenses_by_month.json"

    def _handle_create_directory(self):
        file_path = Path(self.output_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)

    def execute(self, expenses_df):
        self._handle_create_directory()

        df_groupped_by_month = (
            expenses_df.groupby(expenses_df["date"].dt.to_period("M"))
            .agg(total_amount=("amount", "sum"), transaction_count=("amount", "count"))
            .to_json(orient="index", date_format="iso")
        )
        with open(self.output_path, "w") as f:
            f.write(df_groupped_by_month)

        print("\nExported successfully")
