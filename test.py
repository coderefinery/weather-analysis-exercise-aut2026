from os import path, remove
from subprocess import run
from script import arithmetic_mean

def test_png_produced():
    outputs = ["2024-01-precipitation.png", "2024-01-temperature.png"]
    for filename in outputs:
        if path.exists(filename):
            remove(filename)
    run(["python","./script.py"])
    for filename in outputs:
        assert path.exists(filename)


def test_arithmetic_mean():
    values = [1,2,3,4]
    assert arithmetic_mean(values) == 2.5
