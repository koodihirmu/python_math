import numpy as np


def get_radians(degrees: float) -> float:
    return np.radians(degrees)


def get_degrees(radians: float) -> float:
    return np.degrees(radians)


def print_table_from_deg(degrees: list) -> None:
    print("  DEG  |  RAD  ")
    if not degrees:
        return
    for x in degrees:
        print(f"{x}|{get_radians(x):.2f}")
    return


list_of_rad = [2.493, 0.911]
list_of_deg = [137.7, 62.3]

table_of_deg = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]


if __name__ == "__main__":
    for item in list_of_rad:
        print(f"{item} rad == {get_degrees(item):.2f} deg")
    print()
    for item in list_of_deg:
        print(f"{item} deg == {get_radians(item):.2f} rad")
    print()
    print_table_from_deg(table_of_deg)
    input("press enter ...")
