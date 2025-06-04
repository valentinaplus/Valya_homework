import math


def square(side):
    area = side ** 2
    return math.ceil(area)


side_length = 5

square_area = square(side_length)

print(f"Площадь квадрата со стороной {side_length}): {square_area}")
