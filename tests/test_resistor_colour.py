from scripts.resistor_colour import *


def test_resistor_colour_0():
    m = ResistorColour()
    assert m.band_value("black") == 0
    assert m.band_value("blue") == 6
