class ResistorColour:

    def __init__(self):
        self.bands = ["black", "brown", "red", "orange", "yellow",
                      "green", "blue", "violet", "grey", "white"]

    def band_value(self, colour: str) -> int:
        return self.bands.index(colour)
