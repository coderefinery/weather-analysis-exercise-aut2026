from os import path, remove
from subprocess import run


def test_png_produced():
    outputs = [
        "figures/2024-01-precipitation.png",
        "figures/2024-01-temperature.png",
    ]

    for filename in outputs:
        if path.exists(filename):
            remove(filename)

    run(["python", "./script.py"], check=True)

    for filename in outputs:
        assert path.exists(filename)


def test_arithmetic_mean():
    from script import arithmetic_mean

    assert arithmetic_mean([1, 2, 3, 4, 5]) == 3

