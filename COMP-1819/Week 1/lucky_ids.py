from typing import List

def main() -> None:
    with open("resources/lucky_ids_4.txt", "r") as file:
        id: str = "001059317"
        
        # Read file contents
        file_contents: List[str] = [line.strip() for line in file.readlines()]
        
        # Check if the ID matches the pattern
        if check_id_match(id, file_contents):
            print(f"The ID {id} is a winner!")
        else:
            print(f"The ID {id} is not lucky!")
        

"""
    Check ID if the ID exists in the file
    :param id: The ID to check
    :param file_contents: The contents of the file (line by line)
    :return: Whether the ID is found
"""
def check_id_match(id: str, file_contents: List[str]) -> bool:
    # Check each line for a match - ID matches
    for i in range(len(file_contents)):
        if id == file_contents[i]:
            return True
        
    return False    

if __name__ == "__main__":
    main()