total_cost = 0  # Initialize total cost

# First item input
print("You have now initialized the STORE CHECKOUT")
item_name = input("Please enter the ITEM's NAME: ")
item_quantity = int(input("Please enter the ITEM's QUANTITY: "))
item_cost = int(input("Please enter the ITEM's COST: "))
total_cost += item_cost * item_quantity  # Multiply cost by quantity

# Loop to add more items
while True:
    user_response = input("Do you want to add another item? (YES / NO): ").lower()
    
    if user_response == "yes":
        item_name = input("Please enter the ITEM's NAME: ")
        item_quantity = int(input("Please enter the ITEM's QUANTITY: "))
        item_cost = int(input("Please enter the ITEM's COST: "))
        total_cost += item_cost * item_quantity  # Multiply cost by quantity
    
    elif user_response == "no":
        break  # Exit the loop if user says "no"

# Print the total cost
print(f"The total cost of the items is: {total_cost}")
print("Thank You for shopping with us!")