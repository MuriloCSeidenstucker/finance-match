from rich.console import Console

from src.match_controller import expense_match
from tests.mock_expenses import TEST_MATCH

console = Console()


def test_match():
    mock_bank_expenses = TEST_MATCH.get("bank_expenses")
    mock_app_expenses = TEST_MATCH.get("app_expenses")

    result = expense_match(mock_bank_expenses, mock_app_expenses)
    console.print(result)
