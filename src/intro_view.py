from rich.console import Console

console = Console()


def start():
    bank_report_path = console.input("Insira o PATH do relatório bancário: ")
    app_report_path = console.input(
        "Insira o PATH do relatório do app de gestão financeira: "
    )

    return {"bank_report": bank_report_path, "app_report": app_report_path}
