import typer

from lab_package.lab4 import (
    to_str_recursive,
    to_str_iterative,
    sequence_recursive,
    sequence_iterative,
)

from lab_package.lab5 import unique_values
from lab_package.lab6 import generate_combinations


app = typer.Typer()


@app.command()
def lab4_to_str(method: str = "recursive"):
    data = [1, [2, [3, [4, [5]]]]]

    if method == "recursive":
        result = to_str_recursive(data)
    elif method == "iterative":
        result = to_str_iterative(data)
    else:
        typer.echo("Ошибка: method должен быть recursive или iterative")
        return

    typer.echo(result)


@app.command()
def lab4_sequence(n: int = 5, method: str = "recursive"):
    if method == "recursive":
        result = sequence_recursive(n)
    elif method == "iterative":
        result = sequence_iterative(n)
    else:
        typer.echo("Ошибка: method должен быть recursive или iterative")
        return

    typer.echo(result)


@app.command()
def lab5_unique():
    f = unique_values()

    data = [1, 2, 2, 3, 1, 4, 5]

    for x in data:
        result = f(x)
        if result is not None:
            typer.echo(result)


@app.command()
def lab6_combinations():
    sequences = [
        [1, 2],
        ["a", "b"],
        ["X", "Y"],
        [True, False],
    ]

    for combo in generate_combinations(*sequences):
        typer.echo(combo)


if __name__ == "__main__":
    app()