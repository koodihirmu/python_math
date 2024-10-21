from typing import List

import numpy as np


class Triangle:
    def __init__(self, side_a=None, side_b=None, hypothenusa=None) -> None:
        """
        Creates a triangle object that calculates one missing side automatically
        """
        # assign variables to a dict
        self.known_sides = {}
        if hypothenusa:
            self.known_sides["hyp"] = hypothenusa
        if side_a:
            self.known_sides["side_a"] = side_a
        if side_b:
            self.known_sides["side_b"] = side_b

        # check if input triangle is correct
        if len(self.known_sides.keys()) < 2:
            print("Not enough known sides")
            return
        if len(self.known_sides.keys()) >= 3:
            print("Triangle is already solved")
            return

        # calculating and figuring out which side is missing
        try:
            if self.known_sides["hyp"] and self.known_sides["side_a"]:
                self.known_sides["side_b"] = np.sqrt(
                    abs(
                        np.square(self.known_sides["hyp"])
                        - np.square(self.known_sides["side_a"])
                    )
                )
                # a²+b²=c²
            return
        except:
            print("hypothenusa or side_a not found")
        try:
            if self.known_sides["hyp"] and self.known_sides["side_b"]:
                self.known_sides["side_a"] = np.sqrt(
                    abs(
                        np.square(self.known_sides["hyp"])
                        - np.square(self.known_sides["side_b"])
                    )
                )
            return
        except:
            print("hypothenusa or side_b not found")
        try:
            if self.known_sides["side_a"] and self.known_sides["side_b"]:
                self.known_sides["hyp"] = np.sqrt(
                    np.square(self.known_sides["side_a"])
                    + np.square(self.known_sides["side_b"])
                )
            return
        except:
            print("side_a or side_b not found")

    def __del__(self) -> None:
        print("Triangle deleted")

    def print(self) -> None:
        keys = list(self.known_sides.keys())
        for key in keys:
            print(f"{key} | {self.known_sides[key]:.2f}")


if __name__ == "__main__":
    triangle: List[Triangle] = [Triangle(2.3, 1.6)]
    triangle.append(Triangle(2.3, None, 2.8))
    triangle.append(Triangle(None, 1.6, 2.8))
    for tri in triangle:
        tri.print()
    input("press enter ...")
