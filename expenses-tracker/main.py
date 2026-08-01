import pandas as pd
from repositories.expenses_repository import ExpensesRepository
from ui.handlers.get_datasource_path import get_datasource_path
from ui.menu import Menu
from ui.utils import clear_terminal


def load_expenses() -> ExpensesRepository:
    file_path = get_datasource_path()
    expenses_repository = ExpensesRepository()
    expenses_repository.load(file_path)
    return expenses_repository


def main() -> None:
    clear_terminal()

    try:
        expenses_repository = load_expenses()
    except FileNotFoundError as error:
        print(f"File error: {error}")
        return
    except UnicodeTranslateError as error:
        print(error)
        return
    except (ValueError, pd.errors.ParserError) as error:
        print(f"Invalid expense data: {error}")
        return

    Menu().run(expenses_repository.df)


if __name__ == "__main__":
    main()
