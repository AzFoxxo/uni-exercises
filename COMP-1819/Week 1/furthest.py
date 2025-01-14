from typing import List, Tuple
import math

points_to_check: List[Tuple[float, float]] = [(1, 1), (2, 5), (5, 589), (46, 42), (3100000000000, 100000000000)]

"""
Find two furthest points from 0:0
:param points: points to check
:return: tuple containing furthest and second furthest points
"""
def find_two_most_distant(points: List[Tuple[float, float]]):
    distances: List[float] = []

    # Calculate distance from 0:0 for each point
    for point in points:
        distance: float = math.sqrt(point[0]**2 + point[1]**2)
        distances.append(distance)
        print(f"Distance of {point[0]}:{point[1]} is {distance:.2f}.")

if __name__ == "__main__":
    find_two_most_distant(points_to_check)