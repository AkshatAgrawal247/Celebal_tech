def solve_exceptions():
    tests = int(input("How many test cases? "))
    for _ in range(tests):
        try:
            a, b = input("Enter two numbers: ").split()
            result = int(a) // int(b)
            print(result)
        except Exception as e:
            print("Error Code:", e)
