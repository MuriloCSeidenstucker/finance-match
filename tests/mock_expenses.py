from src.expense import Expense


class Cases:
    PERFECT_MATCH = {
        "bank_expenses": [
            Expense(id="bank-1", title="Netflix", amount=39.90, details="", action=""),
            Expense(
                id="bank-2", title="Uber Trip", amount=25.00, details="", action=""
            ),
        ],
        "app_expenses": [
            Expense(id="app-1", title="Netflix", amount=39.90, details="", action=""),
            Expense(id="app-2", title="Uber Trip", amount=25.00, details="", action=""),
        ],
    }

    TITLE_SIMILAR_ACCEPTED = {
        "bank_expenses": [
            Expense(
                id="bank-1", title="Uber* Trip", amount=25.00, details="", action=""
            ),
        ],
        "app_expenses": [
            Expense(id="app-1", title="Uber Trip", amount=25.00, details="", action=""),
        ],
    }

    TITLE_SIMILAR_REJECTED = {
        "bank_expenses": [
            Expense(
                id="bank-1", title="Uber* Trip", amount=25.00, details="", action=""
            ),
        ],
        "app_expenses": [
            Expense(id="app-1", title="Cabify", amount=25.00, details="", action=""),
        ],
    }

    APP_ONLY_EXPENSE = {
        "bank_expenses": [
            Expense(id="bank-1", title="Netflix", amount=39.90, details="", action=""),
        ],
        "app_expenses": [
            Expense(id="app-1", title="Netflix", amount=39.90, details="", action=""),
            Expense(id="app-2", title="Spotify", amount=19.90, details="", action=""),
        ],
    }

    BANK_ONLY_EXPENSE = {
        "bank_expenses": [
            Expense(id="bank-1", title="Netflix", amount=39.90, details="", action=""),
            Expense(id="bank-2", title="iFood", amount=64.50, details="", action=""),
        ],
        "app_expenses": [
            Expense(id="app-1", title="Netflix", amount=39.90, details="", action=""),
        ],
    }

    MIXED_SCENARIO = {
        "bank_expenses": [
            Expense(
                id="bank-1",
                title="Uber Uber *trip Help.u",
                amount=25.00,
                details="",
                action="",
            ),
            Expense(
                id="bank-2",
                title="Padaria Central",
                amount=12.50,
                details="",
                action="",
            ),
            Expense(
                id="bank-3",
                title="Amazon Prime",
                amount=14.90,
                details="",
                action="",
            ),
        ],
        "app_expenses": [
            Expense(id="app-1", title="Uber", amount=25.00, details="", action=""),
            Expense(id="app-2", title="Mercado", amount=12.50, details="", action=""),
            Expense(
                id="app-3", title="Amazon Prime", amount=14.90, details="", action=""
            ),
        ],
    }
