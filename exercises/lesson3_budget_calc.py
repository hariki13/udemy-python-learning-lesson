# Trip Budget Calculater

# TODO: Set up your variables here
total_budget = 1500  # Total budget for the trip
gas_cost = 600  # Expected cost for gas
food_cost = 300  # Expected cost for food
accommodation_cost = 200  # Expected cost for accommodation
souvenir_cost = 25  # Cost of each souverir
supplies_cost = 1000 # cost of each supplies like tissue,shopping bag

# TODO: Calculate the total expenses
expenses = gas_cost + food_cost + accommodation_cost + souvenir_cost + supplies_cost
remaining_money = total_budget - expenses
# TODO: Calculate the remaining money after expenses
print("budget left for expenses:", remaining_money)
# TODO: Calculate the number of souvenirs you can buy 
num_souvenirs = remaining_money // souvenir_cost
# Hint: Use integer division (//) for this step

# TODO: Print the result
print("money left for souvenir:", num_souvenirs)
# Hint: Use an f-string to format your output
print(f"you can buy {num_souvenirs} souvenirs on your trip!")
money_left_after_souvenir = remaining_money % souvenir_cost


# Bonus: Calculate and print how much money is left after buying souvenirs
print(f"you will have ${money_left_after_souvenir} left after buying souvenirs.")

# Hint: Use the modulo operator (%) to get the remainder.