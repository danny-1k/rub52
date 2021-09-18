from .cubie import Cubie


class Face:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color
        self.cubies = [Cubie([c, r], color)
                       for r in range(h) for c in range(h)]

    def clock_wise_turn(self):
        for cubie in self.cubies:
            p = [0, 0]
            p[1] = self.w-cubie.pos[0]-1
            p[0] = abs(self.h-self.h-cubie.pos[1])
            cubie.pos = p

    def counter_clock_wise_turn(self):
        for cubie in self.cubies:
            p = [0, 0]
            p[1] = cubie.pos[0]
            p[0] = self.w-cubie.pos[1]-1
            cubie.pos = p

    def __repr__(self):
        new_cubies = []
        cubies = [str(cubie) for cubie in self.cubies]
        for row in range(self.h):
            new_cubies.append(cubies[row*self.w:][:self.w])
        return '\n'.join([' '.join(i) for i in new_cubies])
