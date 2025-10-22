import typer

from src.main import start

app = typer.Typer()


@app.command()
def run():
    start()
