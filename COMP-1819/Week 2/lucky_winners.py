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
    results: Tuple[int, int, int] = find_top_three_ids(sequence)
    end: float = time.time()
    print(f"Squeeze size: {squeeze_size}")
    print(f"Three largest numbers: {results[0]}, {results[1]}, {results[2]}")
    print(f"Time taken: {end - start:.21f}")
    utils.print_divider()

"""
Return top IDs from a sequence
:param sequence: sequence (int)
:return: tuple of the three biggest IDs
"""
def find_top_three_ids(ids: List[int]) -> Tuple[int, int, int]:
    # Get three largest numbers
    a: int = 0
    b: int = 0
    c: int = 0

    for i in ids:
        if i > a:
            c = b
            b = a
            a = i
        elif i > b:
            c = b
            b = i
        elif i > c:
            c = i

    return a, b, c

if __name__ == "__main__":
    run_time_tests()