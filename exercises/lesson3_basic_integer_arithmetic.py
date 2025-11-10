# Shopping Calculator
print("Running 'Shopping Calculator App':")
wallet = 150  # You start with 150$
# Buy Some Items
book = 15
snack = 5
drink = 3
chocolate = 10
bread = 5
# Calculate total spent
total_spent = book + snack + drink + chocolate + bread
# Calculate remaining money
money_left = wallet - total_spent

print("You spent in $", total_spent)
print("You have in $", money_left, "left")

# Task: 
# 1. Add one more item to buy
number_of_items = 5 # we have 5 items now
# 2. Calculate the average cost of all items.
average_cost = total_spent / number_of_items
print("the average cost per item is $", average_cost)