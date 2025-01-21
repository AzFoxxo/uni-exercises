import random
import time
from typing import List
import utils

class Results:
    def __init__(self, a: int, b: int, c: int, duplicate: bool, duplicates: List[int]) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.duplicate = duplicate
        self.duplicates = duplicates

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
    sequence: List[float] = change_some_entries_to_be_duplicates([i for i in range(squeeze_size)])
    start: float = time.time()
    results: Results = find_top_three_ids(sequence)
    end: float = time.time()
    print(f"Squeeze size: {squeeze_size}")
    print(f"Three largest numbers: {results.a}, {results.b}, {results.c}")
    print(f"Duplicate found: {results.duplicate if "Yes" else "No"}")
    if results.duplicate:
        print(f"Duplicate numbers: ", end="")
        for i in results.duplicates:
            print(i, end="\n" if i == results.duplicates[-1] else ", ")
    print(f"Time taken: {end - start:.21f}")
    utils.print_divider()

"""
Add a random number of duplicates to the sequence
:param ids: sequence of IDs
:return: sequence of IDs with duplicates
"""
def change_some_entries_to_be_duplicates(ids: List[int]) -> List[int]:
    # Choose X random numbers to change
    random_count_min: int = 10
    random_count_max: int = 100
    # 1 either side to avoid reading out of bounds
    random_numbers: List[int] = random.sample(range(1, len(ids) - 1), random.randint(random_count_min, random_count_max))
    for i in random_numbers:
        # Flip the coin if to set the value to the previous or next one
        if random.choice([True, False]):
            ids[i] = ids[i-1]
        else:
            ids[i] = ids[i+1]
    return ids

"""
Return top IDs from a sequence
:param sequence: sequence (int)
:return: Results with the three biggest IDs and if a duplicate was found and the duplicate numbers
"""
def find_top_three_ids(ids: List[int]) -> Results:
    iterated_over: List[int] = []

    # Get three largest numbers
    a: int = 0
    b: int = 0
    c: int = 0
    duplicate: bool = False
    duplicates: List[int] = []

    for i in ids:
        # Update numbers iterated over
        iterated_over.append(i)
            
        if i > a:
            c = b
            b = a
            a = i
        elif i > b:
            c = b
            b = i
        elif i > c:
            c = i

    # Check for duplicates
    iterated_ids: dict[int, int] = {}
    for i in iterated_over:
        # Check the key exists
        if i in iterated_ids:
            duplicate = True
            iterated_ids[i] += 1
            if i not in duplicates:
                duplicates.append(i)
        else:
            iterated_ids[i] = 1

    return Results(a, b, c, duplicate, duplicates)

if __name__ == "__main__":
    run_time_tests()