from rich.console import Console

from src.data_controller import app_report_converter, bank_report_converter
from src.intro_view import introduction_view
from src.match_controller import expense_match

console = Console()


def start():
    report_paths = introduction_view()
    bank_expenses = bank_report_converter(report_paths.get("bank_report"))
    app_expenses = app_report_converter(report_paths.get("app_report"))
    response = expense_match(bank_expenses, app_expenses)
    console.print(response)
