from .face import Face


class Cube:
    def __init__(self, size=(3, 3)):
        self.size = size
        # top,bottom,left,right,front,back
        self.colors = ['o', 'r', 'g', 'b', 'w', 'y']

        self.cube = [Face(size[0], size[1], c) for c in self.colors]

    def F(self):
        # F turns the front face clock-wise
        # the faces we're gonna alter
        # bottom,front,left,right,top

        # Green is facing us
        for idx, cubie in enumerate(self.cube[2].cubies):
            if (idx+1) % self.size[0] == 0:
                pos1 = cubie.pos  # g pos
                color1 = cubie.color  # g

                pos2 = self.cube[1].cubies[idx].pos  # r pos
                color2 = self.cube[1].cubies[idx].color  # r

                pos3 = self.cube[0].cubies[idx].pos  # o pos
                color3 = self.cube[0].cubies[idx].color  # o

                pos4 = self.cube[-3].cubies[idx].pos  # b pos
                color4 = self.cube[-3].cubies[idx].color  # b

                cubie.color = color2
                cubie.pos = pos2

                self.cube[1].cubies[idx].pos = pos4
                self.cube[1].cubies[idx].color = color4

                self.cube[0].cubies[idx].pos = pos1
                self.cube[0].cubies[idx].color = color1

                self.cube[-3].cubies[idx].pos = pos3
                self.cube[-3].cubies[idx].color = color3

        self.cube[-2].clock_wise_turn()  # rotate white face clock-wise

    def F_(self):
        # F_ turns the front face counter-clock-wise
        # the faces we're gonna alter
        # bottom,front,left,right,top

        # Green is facing us
        for idx, cubie in enumerate(self.cube[2].cubies):
            if (idx+1) % self.size[0] == 0:
                pos1 = cubie.pos  # g pos
                color1 = cubie.color  # g

                pos2 = self.cube[1].cubies[idx].pos  # r pos
                color2 = self.cube[1].cubies[idx].color  # r

                pos3 = self.cube[0].cubies[idx].pos  # o pos
                color3 = self.cube[0].cubies[idx].color  # o

                pos4 = self.cube[-3].cubies[idx].pos  # b pos
                color4 = self.cube[-3].cubies[idx].color  # b

                cubie.color = color3
                cubie.pos = pos3

                self.cube[1].cubies[idx].pos = pos1
                self.cube[1].cubies[idx].color = color1

                self.cube[0].cubies[idx].pos = pos4
                self.cube[0].cubies[idx].color = color4

                self.cube[-3].cubies[idx].pos = pos2
                self.cube[-3].cubies[idx].color = color2

        # rotate white face counter-clock-wise
        self.cube[-2].counter_clock_wise_turn()

    def B(self):
        # B turns the back face clock-wise
        # the faces we're gonna alter
        # bottom,left,right,top,back

        # Green is facing us
        for idx, cubie in enumerate(self.cube[2].cubies):
            if idx % self.size[0] == 0:
                pos1 = cubie.pos  # g pos
                color1 = cubie.color  # g

                pos2 = self.cube[1].cubies[idx].pos  # r pos
                color2 = self.cube[1].cubies[idx].color  # r

                pos3 = self.cube[0].cubies[idx].pos  # o pos
                color3 = self.cube[0].cubies[idx].color  # o

                pos4 = self.cube[-3].cubies[idx].pos  # b pos
                color4 = self.cube[-3].cubies[idx].color  # b

                cubie.color = color3
                cubie.pos = pos3

                self.cube[1].cubies[idx].pos = pos1
                self.cube[1].cubies[idx].color = color1

                self.cube[0].cubies[idx].pos = pos4
                self.cube[0].cubies[idx].color = color4

                self.cube[-3].cubies[idx].pos = pos2
                self.cube[-3].cubies[idx].color = color2

        # rotate yellow face counter-clock-wise
        self.cube[-1].clock_wise_turn()

    def B_(self):
        # B_ turns the back face counter-clock-wise
        # the faces we're gonna alter
        # bottom,left,right,top,back

        # Green is facing us
        for idx, cubie in enumerate(self.cube[2].cubies):
            if idx % self.size[0] == 0:
                pos1 = cubie.pos  # g pos
                color1 = cubie.color  # g

                pos2 = self.cube[1].cubies[idx].pos  # r pos
                color2 = self.cube[1].cubies[idx].color  # r

                pos3 = self.cube[0].cubies[idx].pos  # o pos
                color3 = self.cube[0].cubies[idx].color  # o

                pos4 = self.cube[-3].cubies[idx].pos  # b pos
                color4 = self.cube[-3].cubies[idx].color  # b

                cubie.color = color2
                cubie.pos = pos2

                self.cube[1].cubies[idx].pos = pos4
                self.cube[1].cubies[idx].color = color4

                self.cube[0].cubies[idx].pos = pos1
                self.cube[0].cubies[idx].color = color1

                self.cube[-3].cubies[idx].pos = pos3
                self.cube[-3].cubies[idx].color = color3

        # rotate yellow face counter-clock-wise
        self.cube[-1].counter_clock_wise_turn()

    def U(self):
        # U turns the up face clock-wise
        # the faces we're gonna alter
        # top,left,right,front,back

        # White is facing us
        for idx, cubie in enumerate(self.cube[-2].cubies):
            if idx < self.size[0]:
                pos1 = cubie.pos  # w pos
                color1 = cubie.color  # w

                pos2 = self.cube[2].cubies[idx].pos  # g pos
                color2 = self.cube[2].cubies[idx].color  # g

                pos3 = self.cube[3].cubies[idx].pos  # b pos
                color3 = self.cube[3].cubies[idx].color  # b

                pos4 = self.cube[-1].cubies[idx].pos  # y pos
                color4 = self.cube[-1].cubies[idx].color  # y

                cubie.color = pos3
                cubie.pos = color3

                self.cube[3].cubies[idx].pos = pos4
                self.cube[3].cubies[idx].color = color4

                self.cube[-1].cubies[idx].pos = pos2
                self.cube[-1].cubies[idx].color = color2

                self.cube[2].cubies[idx].pos = pos1
                self.cube[2].cubies[idx].color = color1

        # rotate orange face counter-clock-wise
        self.cube[0].counter_clock_wise_turn()

    def U_(self):
        # U_ turns the right face counter-clock-wise
        # the faces we're gonna alter
        # top,left,right,front,back

        # White is facing us
        for idx, cubie in enumerate(self.cube[-2].cubies):
            if idx < self.size[0]:
                pos1 = cubie.pos  # w pos
                color1 = cubie.color  # w

                pos2 = self.cube[2].cubies[idx].pos  # g pos
                color2 = self.cube[2].cubies[idx].color  # g

                pos3 = self.cube[3].cubies[idx].pos  # b pos
                color3 = self.cube[3].cubies[idx].color  # b

                pos4 = self.cube[-1].cubies[idx].pos  # y pos
                color4 = self.cube[-1].cubies[idx].color  # y

                cubie.color = pos2
                cubie.pos = color2

                self.cube[3].cubies[idx].pos = pos1
                self.cube[3].cubies[idx].color = color1

                self.cube[-1].cubies[idx].pos = pos3
                self.cube[-1].cubies[idx].color = color3

                self.cube[2].cubies[idx].pos = pos4
                self.cube[2].cubies[idx].color = color4

        # rotate orange face clock-wise
        self.cube[0].clock_wise_turn()

    def D(self):
        # D turns the down face clock-wise
        # the faces we're gonna alter
        # bottom,left,right,front,back

        # White is facing us
        for idx, cubie in enumerate(self.cube[-2].cubies):
            if idx >= self.size[0]*self.size[1]-self.size[0]:
                pos1 = cubie.pos  # w pos
                color1 = cubie.color  # w

                pos2 = self.cube[2].cubies[idx].pos  # g pos
                color2 = self.cube[2].cubies[idx].color  # g

                pos3 = self.cube[3].cubies[idx].pos  # b pos
                color3 = self.cube[3].cubies[idx].color  # b

                pos4 = self.cube[-1].cubies[idx].pos  # y pos
                color4 = self.cube[-1].cubies[idx].color  # y

                cubie.color = pos2
                cubie.pos = color2

                self.cube[3].cubies[idx].pos = pos1
                self.cube[3].cubies[idx].color = color1

                self.cube[-1].cubies[idx].pos = pos3
                self.cube[-1].cubies[idx].color = color3

                self.cube[2].cubies[idx].pos = pos4
                self.cube[2].cubies[idx].color = color4

        # rotate red face counter-clock-wise
        self.cube[1].counter_clock_wise_turn()

    def D_(self):
        # D_ turns the down face counter-clock-wise
        # the faces we're gonna alter
        # bottom,left,right,front,back

        # White is facing us
        for idx, cubie in enumerate(self.cube[-2].cubies):
            if idx >= self.size[0]*self.size[1]-self.size[0]:
                pos1 = cubie.pos  # w pos
                color1 = cubie.color  # w

                pos2 = self.cube[2].cubies[idx].pos  # g pos
                color2 = self.cube[2].cubies[idx].color  # g

                pos3 = self.cube[3].cubies[idx].pos  # b pos
                color3 = self.cube[3].cubies[idx].color  # b

                pos4 = self.cube[-1].cubies[idx].pos  # y pos
                color4 = self.cube[-1].cubies[idx].color  # y

                cubie.color = pos3
                cubie.pos = color3

                self.cube[3].cubies[idx].pos = pos4
                self.cube[3].cubies[idx].color = color4

                self.cube[-1].cubies[idx].pos = pos2
                self.cube[-1].cubies[idx].color = color2

                self.cube[2].cubies[idx].pos = pos1
                self.cube[2].cubies[idx].color = color1

        # rotate red face clock-wise
        self.cube[1].clock_wise_turn()

    def R(self):
        # R_ turns the right face clock-wise
        # the faces we're gonna alter
        # back,bottom,front,right,top

        # White is facing us
        for idx, cubie in enumerate(self.cube[-2].cubies):
            if (idx+1) % self.size[0] == 0:
                pos1 = cubie.pos  # w pos
                color1 = cubie.color  # w

                pos2 = self.cube[1].cubies[idx].pos  # r pos
                color2 = self.cube[1].cubies[idx].color  # r

                pos3 = self.cube[0].cubies[idx].pos  # o pos
                color3 = self.cube[0].cubies[idx].color  # o

                pos4 = self.cube[-1].cubies[idx].pos  # y pos
                color4 = self.cube[-1].cubies[idx].color  # y

                cubie.color = color2
                cubie.pos = pos2

                self.cube[1].cubies[idx].pos = pos4
                self.cube[1].cubies[idx].color = color4

                self.cube[0].cubies[idx].pos = pos1
                self.cube[0].cubies[idx].color = color1

                self.cube[-1].cubies[idx].pos = pos3
                self.cube[-1].cubies[idx].color = color3

        self.cube[-3].clock_wise_turn()  # rotate blue face clock-wise

    def R_(self):
        # R turns the right face counter-clock-wise
        # the faces we're gonna alter
        # back,bottom,front,right,top

        # White is facing us
        for idx, cubie in enumerate(self.cube[-2].cubies):
            if (idx+1) % self.size[0] == 0:
                pos1 = cubie.pos  # r pos
                color1 = cubie.color  # r

                pos2 = self.cube[1].cubies[idx].pos  # y pos
                color2 = self.cube[1].cubies[idx].color  # y

                pos3 = self.cube[0].cubies[idx].pos  # w pos
                color3 = self.cube[0].cubies[idx].color  # w

                pos4 = self.cube[-1].cubies[idx].pos  # o pos
                color4 = self.cube[-1].cubies[idx].color  # o

                cubie.color = color3
                cubie.pos = pos3

                self.cube[1].cubies[idx].pos = pos1
                self.cube[1].cubies[idx].color = color1

                self.cube[0].cubies[idx].pos = pos4
                self.cube[0].cubies[idx].color = color4

                self.cube[-1].cubies[idx].pos = pos2
                self.cube[-1].cubies[idx].color = color2

        # rotate blue face counter-clock-wise
        self.cube[-3].counter_clock_wise_turn()

    def L(self):
        # L turns the left face clock-wise
        # the faces we're gonna alter
        # back,bottom,front,left,top

        # White is facing us
        for idx, cubie in enumerate(self.cube[-2].cubies):
            if idx % self.size[0] == 0:
                pos1 = cubie.pos  # r pos
                color1 = cubie.color  # r

                pos2 = self.cube[1].cubies[idx].pos  # y pos
                color2 = self.cube[1].cubies[idx].color  # y

                pos3 = self.cube[0].cubies[idx].pos  # w pos
                color3 = self.cube[0].cubies[idx].color  # w

                pos4 = self.cube[-1].cubies[idx].pos  # o pos
                color4 = self.cube[-1].cubies[idx].color  # o

                cubie.color = color3
                cubie.pos = pos3

                self.cube[1].cubies[idx].pos = pos1
                self.cube[1].cubies[idx].color = color1

                self.cube[0].cubies[idx].pos = pos4
                self.cube[0].cubies[idx].color = color4

                self.cube[-1].cubies[idx].pos = pos2
                self.cube[-1].cubies[idx].color = color2

        # rotate green face counter-clock-wise
        self.cube[2].counter_clock_wise_turn()

    def L_(self):
        # L_ turns the left face counter-clock-wise
        # the faces we're gonna alter
        # back,bottom,front,right,top

        # White is facing us
        for idx, cubie in enumerate(self.cube[-2].cubies):
            if idx % self.size[0] == 0:
                pos1 = cubie.pos  # w pos
                color1 = cubie.color  # w

                pos2 = self.cube[1].cubies[idx].pos  # r pos
                color2 = self.cube[1].cubies[idx].color  # r

                pos3 = self.cube[0].cubies[idx].pos  # o pos
                color3 = self.cube[0].cubies[idx].color  # o

                pos4 = self.cube[-1].cubies[idx].pos  # y pos
                color4 = self.cube[-1].cubies[idx].color  # y

                cubie.color = color2
                cubie.pos = pos2

                self.cube[1].cubies[idx].pos = pos4
                self.cube[1].cubies[idx].color = color4

                self.cube[0].cubies[idx].pos = pos1
                self.cube[0].cubies[idx].color = color1

                self.cube[-1].cubies[idx].pos = pos3
                self.cube[-1].cubies[idx].color = color3

        self.cube[2].clock_wise_turn()  # rotate green face clock-wise

    def __repr__(self):
        return '\n\n'.join([str(color) for color in self.cube])
        # for color in self.cube:
        #     for face in color:
        #         print(face)
