import time
from typing import List
import utils

"""
Test how long the function takes to run given X sized sequence
"""
def run_time_tests() -> None:
    number_of_primes_to_check: int = 10000
    sequence: List[int] = [i for i in range(number_of_primes_to_check)]

    first_iteration_time: float = 0
    last_iteration_time: float = 0
    
    for number in sequence:
        if number == 0 or number == 1:
            first_iteration_time = perform_individual_test(3)
        else:
            last_iteration_time = perform_individual_test(number+1)

    # Calculate the time difference between
    print(f"First prime number (not an edge case) took {first_iteration_time:.21f} seconds to execute")
    print(f"Last prime number took {last_iteration_time:.21f} seconds to execute")
    print(f"Time difference to calculate the prime is {last_iteration_time - first_iteration_time:.21f} seconds for {number_of_primes_to_check+1} ")

"""
Run a specific test
:param squeeze_size: sequence size
:param number: time to check
"""
def perform_individual_test(number: int) -> float:
    start_time: float = time.time()
    results: bool = is_prime(number)
    end_time: float = time.time()
    print(f"{number} is {"not " if not results else ""}a prime number and was calculated in {end_time - start_time:.21f} seconds")
    utils.print_divider()
    return end_time - start_time
    
"""
Returns if a number is prime
:param number: number to check
:return: True (is a prime) else False (is not a prime)
"""
def is_prime(number: int) -> bool:
    # Edge cases
    if number == 1 or number == 0 or number < 0:
        return False
    
    for i in range(2,int(number**0.5)+1):
        # Check divisibility
        if (number % i) == 0:
            return False
    
    return True

if __name__ == "__main__":
    run_time_tests()