from typing import List

import pandas as pd

from src.expense import Expense


def bank_report_converter(bank_path: str) -> List[Expense]:
    bank_report_df = pd.read_csv(bank_path)

    bank_expenses = []
    for row in bank_report_df.itertuples():
        expense_id = f"bank-report-{row[0]}"
        title = row[2]
        amount = row[3]
        bank_expenses.append(
            Expense(
                id=expense_id,
                title=title,
                amount=amount,
                details="",
                action="",
            )
        )

    return bank_expenses


def app_report_converter(app_path: str) -> List[Expense]:
    app_report_df = pd.read_excel(app_path, header=None, skiprows=3)
    app_report_df.rename(columns={0: "title", 1: "amount"}, inplace=True)
    app_report_df.dropna(subset=["amount"], inplace=True)
    app_report_df["amount"] = (
        app_report_df["amount"]
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    app_report_df["amount"] = pd.to_numeric(app_report_df["amount"], errors="coerce")
    app_report_df["amount"] = app_report_df["amount"].abs()

    app_expenses = []
    for row in app_report_df.itertuples():
        expense_id = f"app-report-{row[0]}"
        title = row[1]
        amount = row[2]
        app_expenses.append(
            Expense(
                id=expense_id,
                title=title,
                amount=amount,
                details="",
                action="",
            )
        )

    return app_expenses
