import time
from typing import Tuple, List
import utils

"""
Test how long the function takes to run given X sized sequence
"""
def run_time_tests() -> None:
    K: int = 1000
    perform_individual_test(2 * K)
    perform_individual_test(10 * K)
    perform_individual_test(50 * K)
    perform_individual_test(200 * K)
    perform_individual_test(1000 * K)

"""
Run a specific test
:param squeeze_size: sequence size
"""
def perform_individual_test(squeeze_size: int) -> None:
    sequence: List[float] = [i for i in range(squeeze_size)]
    start: float = time.time()
    results: Tuple[float, float] = min_max(sequence)
    end: float = time.time()
    print(f"Squeeze size: {squeeze_size}")
    print(f"Min {results[0]} and max {results[1]}")
    print(f"Time taken: {end - start:.21f}")
    utils.print_divider()

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
    run_time_tests()