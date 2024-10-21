from typing import List

import numpy as np


class Triangle:
    def __init__(self, side_a=None, side_b=None, hypothenusa=None) -> None:
        """
        Creates a triangle object that calculates one missing side automatically
        """
        # assign variables to a dict
        self.hyp = hypothenusa
        self.side_a = side_a
        self.side_b = side_b
        self.valid = True

        # amount of known sides
        known_sides = 0
        if self.hyp:
            known_sides += 1
        if self.side_a:
            known_sides += 1
        if self.side_b:
            known_sides += 1

        # check if input triangle is correct
        if known_sides < 2:
            print("Not enough known sides to calculate")
            self.valid = False
            return
        elif known_sides > 2:
            print("Triangle is solved already")
            return

        # calculating and figuring out which side is missing
        # a²+b²=c²
        if self.hyp and self.side_a:
            self.side_b = np.sqrt(abs(np.square(self.hyp) - np.square(self.side_a)))
            return
        if self.hyp and self.side_b:
            self.side_a = np.sqrt(abs(np.square(self.hyp) - np.square(self.side_b)))
            return
        if self.side_a and self.side_b:
            self.hyp = np.sqrt(np.square(self.side_a) + np.square(self.side_b))
            return

    def __del__(self) -> None:
        print("Triangle deleted")

    def print(self) -> None:
        # check if the triangle is valid before printing
        if self.valid:
            print("____________________________")
            print(f"side_a | {self.side_a:.2f}")
            print(f"side_b | {self.side_b:.2f}")
            print(f"hyp    | {self.hyp:.2f}")
            print("____________________________")
        else:
            print("Invalid triangle")


if __name__ == "__main__":
    triangle: List[Triangle] = [Triangle(2.3, 1.6)]

    # if we are in debug mode assign some more triangles
    if __debug__:
        triangle.append(Triangle(2.3, None, 2.8))
        triangle.append(Triangle(None, None, None))
        triangle.append(Triangle(2.3, 1.6, 2.8))

    for tri in triangle:
        tri.print()
    input("press enter ...")
