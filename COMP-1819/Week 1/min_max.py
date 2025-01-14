from typing import Tuple, List

"""
Return min and max value of a sequence
:param sequence: sequence of floats
:return: tuple(min, max) of sequence

"""
def min_max(sequence: List[float]) -> Tuple[float, float]:
    greatest: float = sequence[0]
    least: float = sequence[0]

    # Update smallest and biggest numbers
    for i in sequence:
        if i > greatest:
            greatest = i
        if i < least:
            least = i

    return (least, greatest)

if __name__ == "__main__":
    sequence: List[float] = [10, 45, 653, 4, -4, 1]
    min_max_results: Tuple[float, float] = min_max(sequence)
    print(f"From sequence {sequence}, min value is {min_max_results[0]} and max value is {min_max_results[1]}")