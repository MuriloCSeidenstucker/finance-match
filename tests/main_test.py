from pytest_mock import MockerFixture

from src.main import start


def test_start(mocker: MockerFixture):
    mock_print = mocker.patch("rich.console.Console.print")

    start()

    mock_print.assert_called_once_with("Hello World!")
