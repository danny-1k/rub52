# Rub52

A rubiks cube simulator in python

## Basic usage
```python
from rub52 import Cube

cube = Cube(size=(3,3))

cube.F()
cube.F2()
cube.F_()

cube.B()
cube.B2()
cube.B_()

cube.U()
cube.U2()
cube.U_()

cube.D()
cube.D2()
cube.D_()

cube.L()
cube.L2()
cube.L_()

print(cube)

#OUTPUT
# |o [2, 2]| |o [1, 2]| |r [0, 2]|
# |o [2, 1]| |o [1, 1]| |r [0, 1]|
# |o [2, 0]| |o [1, 0]| |r [0, 0]|

# |r [2, 2]| |r [1, 2]| |o [0, 2]|
# |r [2, 1]| |r [1, 1]| |o [0, 1]|
# |r [2, 0]| |r [1, 0]| |o [0, 0]|

# |g [2, 2]| |b [1, 2]| |g [0, 2]|
# |b [2, 1]| |g [1, 1]| |b [0, 1]|
# |g [2, 0]| |b [1, 0]| |g [0, 0]|

# |b [0, 0]| |g [1, 0]| |b [2, 0]|
# |g [0, 1]| |b [1, 1]| |g [2, 1]|
# |b [0, 2]| |g [1, 2]| |b [2, 2]|

# |w [2, 2]| |y [1, 2]| |y [0, 2]|
# |y [2, 1]| |w [1, 1]| |w [0, 1]|
# |w [2, 0]| |y [1, 0]| |y [0, 0]|

# |y [2, 2]| |w [1, 2]| |w [0, 2]|
# |w [2, 1]| |y [1, 1]| |y [0, 1]|
# |y [2, 0]| |w [1, 0]| |w [0, 0]|
```

You can scramble a cube:
```python
#--SNIP--
cube.scramble(steps=34,seed=0)
```
## TODO

- [ ] Graphics & 3d (Next 10^256 years)