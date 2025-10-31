from typing import List

from rich.console import Console

from src.expense import Expense
from src.text_compare import title_match

console = Console()


def expense_match(
    bank_expenses: List[Expense],
    app_expenses: List[Expense],
    acceptable_diff: float = 0.6,
) -> List[Expense]:
    response = []

    bank_by_amount = {expense.amount: expense for expense in bank_expenses}
    app_by_amount = {expense.amount: expense for expense in app_expenses}

    for app_expense in app_expenses:
        bank_expense = bank_by_amount.get(app_expense.amount)

        if not bank_expense:
            app_expense.details = (
                "Essa despesa não foi encontrada no relatório bancário."
            )
            app_expense.action = "Excluir"
            response.append(app_expense)
            continue

        if not title_match(app_expense.title, bank_expense.title, acceptable_diff):
            app_expense.details = (
                "Valor corresponde, mas a descrição diverge. Verifique se está correta."
            )
            app_expense.action = "Verificar"
            response.append(app_expense)

    for bank_expense in bank_expenses:
        if bank_expense.amount not in app_by_amount:
            bank_expense.details = (
                "Essa despesa não está cadastrada no app de gestão financeira."
            )
            bank_expense.action = "Adicionar"
            response.append(bank_expense)

    return response
