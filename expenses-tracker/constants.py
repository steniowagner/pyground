from typing import Final

EXPENSES_CSV_REQUIRED_COLUMNS: Final[tuple[str, ...]] = (
    "date",
    "description",
    "category",
    "amount",
)
