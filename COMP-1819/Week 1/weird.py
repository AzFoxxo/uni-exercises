"""
Says if the number is weird
:param number: Number to check
"""
def weird_number(number: float) -> None:
    if number % 2 == 1:
        print("Weird")
    elif number > 1 and number < 10:
            print("Not Weird")
    elif number > 9 and number < 31:
         print("Weird")
    elif number % 2 == 0 or number > 30:
        print("Weird")

if __name__ == "__main__":
    for i in range(1, 100):
        print(f"{i} is ", end="")
        weird_number(i)
