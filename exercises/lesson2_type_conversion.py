# Create a variable called 'price' as a string with the value '19.99'.
price = "29.99"
# Convert 'price' to a float and store it in a new variable called 'price_float'.
price_float = float(price)
# Create a variable called 'quantity' as an integer with a value 5.
quantity = 10
# Calculate the total cost by multiplying 'price_float' and 'quantity', and store it in a variable called 'total_cost'.
total_cost = price_float * quantity
# Convert 'total_cost' to an integer (round down) and store it in a variable called 'total_cost_int'.
total_cost_int = int(total_cost)
# Print out 'price', 'price_float', 'quantaty', 'total_cost', 'total_cost_int' along with theit types.
print(f"price (string): {price}, type: {type(price)}")
print(f"price (float): {price_float}, type: {type(price_float)}")
print(f"quantity: {quantity}, type: {type(quantity)}")
print(f"total cost: {total_cost}, type: {type(total_cost)}")
print(f"total cost (int): {total_cost_int}, type: {type(total_cost)}")
