from collections import Counter  # To count items easily

def solve_collections_counter():
    # Step 1: Input total number of shoes in the shop
    total_shoes = int(input("How many shoes are in the shop? "))
    
    # Step 2: Input the sizes of all shoes
    sizes = list(map(int, input("Enter all shoe sizes: ").split()))
    
    # Step 3: Use Counter to keep track of how many of each size
    stock = Counter(sizes)
    
    # Step 4: Input number of customers
    customers = int(input("How many customers? "))
    total_earnings = 0   

    # Step 5: For each customer, take order and check if shoe available
    for _ in range(customers):
        size, price = map(int, input("Enter desired shoe size and offered price: ").split())
        if stock[size] > 0:       
            total_earnings += price
            stock[size] -= 1      

    # Step 6: Print total money earned
    print("Total earnings:", total_earnings)
