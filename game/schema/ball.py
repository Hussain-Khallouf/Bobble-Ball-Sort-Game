class Ball:
    color: str

    def __init__(self, color: str):
        self.color = color

    def __str__(self):
        return self.color

    def __eq__(self, other):
        return self.color == other.color

    def getColor(self):
        return self.color
