def solve_text_wrap():
    text = input("Enter a string: ")
    width = int(input("Enter width to wrap: "))
    
    for i in range(0, len(text), width):
        print(text[i:i+width])  
