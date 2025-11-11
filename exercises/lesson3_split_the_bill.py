# Split the bill program

# Step 1: Set up our vriables
total_bill = 355 # Your code here
number_of_friends = 7 # Your code here

# Step 2: Calculate the individual share
individual_share = total_bill / number_of_friends # Your code here



# Bonus challenge
# 1. Include a 15% tip in the total bill before splitting.
# 2. Round the individual share to two decimal places ( hint: look up the round() function)
tip_percentage = 0.15
tip_amount = total_bill * tip_percentage
total_with_tip = total_bill + tip_amount
rounded_share = round(individual_share, 2)

# Step 3: Display the results
print(f"original bill: ${total_bill}")
print(f"tip amount (15%): ${tip_amount}")
print(f"Total bill with tip: ${total_with_tip}")
print(f"Number of friends: {number_of_friends}")
print(f"Each person should pay: ${rounded_share}")