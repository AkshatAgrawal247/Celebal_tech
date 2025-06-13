import re

def solve_incorrect_regex():
    test_cases = int(input("How many regex patterns? "))

    for _ in range(test_cases):
        pattern = input("Enter regex pattern: ")
        try:
            # Try using the pattern in re.search  
            re.search(pattern, "test")
            print(True)
        except re.error:
            print(False)
