def solve_capitalize():
    text = input("Enter a sentence: ")
    words = text.split(" ")  # Split the sentence into words
    result = ""
    for word in words:
        result += word.capitalize() + " "  
    print("Capitalized:", result.strip())  # Remove extra space at the end
