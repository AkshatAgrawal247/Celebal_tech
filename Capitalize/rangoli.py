import string

def solve_alphabet_rangoli():
    n = int(input("Enter size (1 to 26): "))
    abc = string.ascii_lowercase   
    lines = []

    # Make the upper half of rangoli including middle row
    for i in range(n):
        left = abc[n-1:i:-1]      
        right = abc[i:n]          
        row = "-".join(left + right)  # Join with dashes
        lines.append(row.center(4*n - 3, "-"))  # Center it with dashes

    # Print top half
    for i in range(n-1, 0, -1):
        print(lines[i])

    # Print bottom half (including middle)
    for i in range(n):
        print(lines[i])
