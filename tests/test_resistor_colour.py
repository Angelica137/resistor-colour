from scripts.resistor_colour import resistor_colour


def test_resistor_colour_0():
    assert resistor_colour("black") == 0
