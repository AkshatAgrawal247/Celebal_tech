def solve_introduction_to_sets():
    n = int(input("How many numbers? "))
    numbers = list(map(int, input("Enter the numbers: ").split()))
    unique_numbers = set(numbers)  # Remove duplicates
    avg = sum(unique_numbers) / len(unique_numbers)
    print("Average of unique numbers is:", avg)
