from pathlib import Path

from file_handlers.csv_file_handler import CSVFileHandler
from file_handlers.file_handler import FileHandler
from file_handlers.json_file_handler import JSONFileHandler


class UnsupportedFileTypeError(ValueError):
    pass


def create_file_handler(file_path: Path) -> FileHandler:
    handlers: dict[str, type[FileHandler]] = {
        ".csv": CSVFileHandler,
        ".json": JSONFileHandler,
    }

    file_extension = file_path.suffix.lower()
    handler_class = handlers.get(file_extension)
    if handler_class is None:
        raise UnsupportedFileTypeError(
            f"Unsupported file type: {file_extension or 'no extension'}"
        )

    return handler_class(file_path)
