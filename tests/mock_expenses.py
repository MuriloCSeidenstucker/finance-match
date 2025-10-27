from src.expense import Expense

TEST_MATCH = {
    "bank_expenses": [
        Expense(
            id="bank-1", title="spy expense 1", amount=10.00, details="", action=""
        ),
        Expense(
            id="bank-2", title="spy expense 2", amount=20.00, details="", action=""
        ),
        Expense(
            id="bank-3", title="spy expense 3", amount=30.00, details="", action=""
        ),
    ],
    "app_expenses": [
        Expense(
            id="bank-1", title="spy expense 1", amount=10.00, details="", action=""
        ),
        Expense(
            id="bank-2", title="spy expense 2", amount=20.00, details="", action=""
        ),
        Expense(
            id="bank-3", title="spy expense 3", amount=30.00, details="", action=""
        ),
    ],
}
