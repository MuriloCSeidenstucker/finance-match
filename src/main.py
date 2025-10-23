from rich.console import Console

from src import intro_view

console = Console()


def start():
    report_paths = intro_view.start()
    console.print(report_paths)
