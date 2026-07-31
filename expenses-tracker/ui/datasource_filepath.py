from ui.utils import show_header_message


class DatasourceFilepath:
    def _show_message(self):
        show_header_message("Import Expenses")
        print("1 - Import from JSON")
        print("2 - Import from CSV")

    def _get_file_path(self, option: str):
        mapping_option_file_path = {
            "1": "test_files/expenses.json",
            "2": "test_files/expenses.csv",
        }

        if option not in mapping_option_file_path:
            raise ValueError("Invalid option")

        return mapping_option_file_path[option]

    def get_filepath(self):
        self._show_message()
        option = input()
        file_path = self._get_file_path(option)
        return file_path
