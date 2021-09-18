class Cubie:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def __repr__(self):
        return f'|{self.color} {self.pos}|'
