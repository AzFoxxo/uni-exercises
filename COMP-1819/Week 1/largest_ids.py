from typing import List

def main() -> None:
    with open("resources/lucky_ids_4.txt", "r") as file:
        # Read file contents
        file_contents: List[str] = [line.strip() for line in file.readlines()]
        
        # Get largest ID values
        largest_ids: List[int] = get_three_largest_ids(file_contents)
        
        print(f"These the are three biggest IDs: {largest_ids[0]}, {largest_ids[1]} and {largest_ids[2]}.")
        
"""
    Update biggest IDs
    :param biggest: The list of IDs to update
    :param id: The ID to update
"""
def update_biggest_ids(biggest: List[int], id: int) -> None:
    # Check bigger than first
    if id > biggest[0]:
        biggest[2] = biggest[1]
        biggest[1] = biggest[0]
        biggest[0] = id
    # Check bigger than second
    elif id > biggest[1]:
        biggest[2] = biggest[1]
        biggest[1] = id
    # Must be bigger than third
    else:
        biggest[2] = id

"""
    Get the three biggest IDs
    :param file_contents: File contents (lines)
    :return: The three biggest IDs
"""
def get_three_largest_ids(file_contents: List[str]) -> List[int]:
    # Convert the IDs to their corresponding integer values
    ids: List[int] = [int(id) for id in file_contents]
    
    # Iterate over the list, finding the three biggest IDs
    biggest: List[int] = [-1, -1, -1]
    
    for id in ids:
        # Update ID if bigger than the third biggest
        if id > biggest[2]:
            update_biggest_ids(biggest, id)
            
    return biggest

if __name__ == "__main__":
    main()