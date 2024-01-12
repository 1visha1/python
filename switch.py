from typing import List

def areaSwitchCase(ch: int, a: List[float]) -> float:
    if ch == 1:
        # Choice 1: Calculate the area of a circle (pi * r^2)
        area = (3.14159 * (a[0] ** 2))
        area = "{:.5f}".format(area)
        return area
    elif ch == 2:
        # Choice 2: Calculate the area of a rectangle (l * b)
        l, b = a
        area = l * b
        area = "{:.5f}".format(area)
        return area
    pass

# Example usage:
print(areaSwitchCase(1,[3]))