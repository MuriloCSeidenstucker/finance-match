from pytest_mock import MockerFixture

from src.intro_view import introduction_view


def test_start(mocker: MockerFixture):
    mock_paths = ["bank_report_spy", "app_report_spy"]
    mock_input = mocker.patch("rich.console.Console.input", side_effect=mock_paths)

    response = introduction_view()

    assert mock_input.call_count == 2
    assert response["bank_report"] == mock_paths[0]
    assert response["app_report"] == mock_paths[1]
