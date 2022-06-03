from scripts.resistor_colour import *


def test_resistor_colour_0():
    m = ResistorColour()
    assert m.band_value("black") == 0
    assert m.band_value("blue") == 6


def test_band_colours_returns_colours():
    m = ResistorColour()
    assert m.band_colours() == ["black", "brown", "red", "orange", "yellow",
                                "green", "blue", "violet", "grey", "white"]
