def solve_set_discard_remove_pop():
    n = int(input("How many elements in set? "))
    s = set(map(int, input("Enter the elements: ").split()))
    commands = int(input("How many commands? "))

    for _ in range(commands):
        parts = input("Enter command: ").split()
        if parts[0] == "pop":
            s.pop()
        elif parts[0] == "remove":
            s.remove(int(parts[1]))
        elif parts[0] == "discard":
            s.discard(int(parts[1]))

    print("Sum after operations:", sum(s))
