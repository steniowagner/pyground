from repositories.expenses_repository import ExpensesRepository
from ui.datasource_filepath import DatasourceFilepath
from ui.menu import Menu
from ui.utils import clear_terminal


def load_expenses_df():
    datasource_filepath = DatasourceFilepath()
    file_path = datasource_filepath.get_filepath()
    expenses_repository = ExpensesRepository()
    expenses_repository.load(file_path)
    return expenses_repository.df


def main():
    clear_terminal()
    expenses_df = load_expenses_df()
    menu = Menu()
    menu.run(expenses_df)


main()
