from rich.console import Console

from src.match_controller import expense_match
from tests.mock_expenses import Cases

console = Console()


def test_match():
    result = expense_match(
        Cases.PERFECT_MATCH.get("bank_expenses"),
        Cases.PERFECT_MATCH.get("app_expenses"),
    )

    assert not result


def test_match_similar_accepted():
    result = expense_match(
        Cases.TITLE_SIMILAR_ACCEPTED.get("bank_expenses"),
        Cases.TITLE_SIMILAR_ACCEPTED.get("app_expenses"),
    )

    assert not result


def test_match_similar_rejected():
    expected = [{"id": "app-1", "title": "Cabify"}]

    result = expense_match(
        Cases.TITLE_SIMILAR_REJECTED.get("bank_expenses"),
        Cases.TITLE_SIMILAR_REJECTED.get("app_expenses"),
    )

    assert len(result) == len(expected)
    assert result[0].id == expected[0].get("id")
    assert result[0].title == expected[0].get("title")


def test_match_app_only_expense():
    expected = [{"id": "app-2", "action": "Excluir"}]

    result = expense_match(
        Cases.APP_ONLY_EXPENSE.get("bank_expenses"),
        Cases.APP_ONLY_EXPENSE.get("app_expenses"),
    )

    assert len(result) == len(expected)
    assert result[0].id == expected[0].get("id")
    assert result[0].action == expected[0].get("action")


def test_match_bank_only_expense():
    expected = [{"id": "bank-2", "action": "Adicionar"}]

    result = expense_match(
        Cases.BANK_ONLY_EXPENSE.get("bank_expenses"),
        Cases.BANK_ONLY_EXPENSE.get("app_expenses"),
    )

    assert len(result) == len(expected)
    assert result[0].id == expected[0].get("id")
    assert result[0].action == expected[0].get("action")


def test_match_strict_tolerance():
    expected = [{"id": "app-1", "title": "Uber"}, {"id": "app-2", "title": "Mercado"}]

    result = expense_match(
        Cases.MIXED_SCENARIO["bank_expenses"],
        Cases.MIXED_SCENARIO["app_expenses"],
        acceptable_diff=0.9,
    )

    assert len(result) == len(expected)
    assert result[0].id == expected[0].get("id")
    assert result[0].title == expected[0].get("title")
    assert result[1].id == expected[1].get("id")
    assert result[1].title == expected[1].get("title")


def test_match_loose_tolerance():
    expected = [{"id": "app-2", "title": "Mercado"}]

    result = expense_match(
        Cases.MIXED_SCENARIO["bank_expenses"],
        Cases.MIXED_SCENARIO["app_expenses"],
        acceptable_diff=0.3,
    )

    assert len(result) == len(expected)
    assert result[0].id == expected[0].get("id")
    assert result[0].title == expected[0].get("title")
