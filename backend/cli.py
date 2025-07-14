import typer

from .engine import ConversationMemory
from .plugin_manager import PluginManager

app = typer.Typer()
pm = PluginManager()
mem = ConversationMemory()


@app.command()
def load(name: str) -> None:
    pm.load(name)
    typer.echo(f"loaded {name}")


@app.command()
def add(role: str, content: str) -> None:
    mem.add(role, content)
    typer.echo("added")


@app.command()
def search(query: str) -> None:
    results = mem.search(query)
    typer.echo(results)


if __name__ == "__main__":
    app()
