import os

"""
    Print a divider to the console
"""
@staticmethod
def print_divider() -> None:
    print("-" * os.get_terminal_size().columns)