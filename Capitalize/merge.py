def solve_merge_the_tools():
    string = input("Enter the string: ")
    k = int(input("Enter the part size: "))

    for i in range(0, len(string), k):
        part = string[i:i+k]
        seen = ""
        for char in part:
            if char not in seen:
                seen += char
        print(seen)
