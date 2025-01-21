import time
from typing import Tuple, List
import utils

"""
Test how long the function takes to run given X sized sequence
"""
def run_time_tests() -> None:
    targets: List[int] = [9, 13, 18, 22]
    numbers: List[int] = [2, 7, 11, 15]

    for target in targets:
        perform_individual_test(target, numbers)

"""
Run a specific test
:param target: target number to reach
:param numbers: numbers to check
"""
def perform_individual_test(target: int, numbers: List[int]) -> None:
    time_start: float = time.time()
    results: Tuple[int, int] = pair_sum(target, numbers)
    time_end: float = time.time()
    if results[0] == -1 and results[1] == -1:
        print(f"Pair sum of {target} is not possible")
    else:
        print(f"Pair sum of {target} is {results} and was calculated in {time_end - time_start:.21f} seconds")
    utils.print_divider()

"""
Returns the pair sum of a target number
:param target: target number
:param numbers: numbers to use to build the pair sum
:return: pair sum
"""
def pair_sum(target: int, numbers: List[int]) -> Tuple[int, int]:
    left: int = 0
    right: int = len(numbers) - 1

    # Calculate the pair sum
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [numbers[left], numbers[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


if __name__ == "__main__":
    run_time_tests()