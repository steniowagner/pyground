from pathlib import Path

from ui.utils import show_header_message


def show_message() -> None:
    show_header_message("Import Expenses")
    print("1 - Import from JSON")
    print("2 - Import from CSV")


def get_file_path(option: str) -> str:
    mapping_option_file_path = {
        "1": "test_files/expenses.json",
        "2": "test_files/expenses.csv",
    }

    if option not in mapping_option_file_path:
        raise ValueError("Invalid option")

    return mapping_option_file_path[option]


def get_datasource_path() -> Path:
    show_message()
    option = input()
    str_file_path = get_file_path(option)
    file_path = Path(str_file_path).expanduser()
    return file_path
