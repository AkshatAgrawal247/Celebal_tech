n = int(input("Enter number of integers: ")) 
numbers = input("Enter the numbers: ").split()
integer_tuple = tuple(int(num) for num in numbers) 
print("Hash value:", hash(integer_tuple))
