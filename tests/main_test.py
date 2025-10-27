from pytest_mock import MockerFixture

from src.main import start


def test_start(mocker: MockerFixture):
    mock_view = mocker.patch("src.main.introduction_view")
    mock_bank_converter = mocker.patch("src.main.bank_report_converter")
    mock_app_converter = mocker.patch("src.main.app_report_converter")
    mock_controller = mocker.patch("src.main.expense_match")

    start()

    mock_view.assert_called_once()
    mock_bank_converter.assert_called_once()
    mock_app_converter.assert_called_once()
    mock_controller.assert_called_once()
