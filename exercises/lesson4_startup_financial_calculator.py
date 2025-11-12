# Startup Financial Calculator 

# Description
# You're an aspiring entrepreneur with a brilliant idea for a 
# new software-as-as-sevice (SaaS)startup. Before pitching to investors,
# you need to create a financial model to project your costs, revenue,
# and break-even point. Your task is to complete a Python script 
# that calculates these crusial finacial metrics.

# 1. Caculate Total Startup Cost: Sum up the individual startup costs
# (development, marketing, and equipent) to get the total initial 
# investment needed.

# 2. Project Monthly Revenue: Calculate the expected monthly revenue 
# based on the number users in each subsciption tier and their respective 
# prices. 

# 3. Calculate Monthly Operating Costs: Sum up all the monthly 
# recurring costs to determine your total monthly operating expenses.

# 4. Determine Monthly Profit: Substract the monthly operating costs
# from the monthly revenue to find out how much profit (or loss)
# you're making each month.

# 5. Estimate Time to Break Even: Calculate how many months it will take
# to recover your initial investment based on your monthly profit.

# 6. Implement Sensitivity Analysis: Create code that adjusts the number of
# users in each tier and recalculate all financial metrics. This will help
# you understant how changes in user aquisition affect your projects.

# 7. Format and Display Results: Use f-string to format the results nicely,
# diplaying currency value with commas and two decimal places, and rounding 
# the break-even time to one decimal place. 

# Startip costs
dev_cost = 50000
marketing_cost = 20000
equipment_cost = 10000

# Subscription tiers
basic_tier_price = 9.99
pro_tier_price = 19.99
basic_tier_users = 1000
pro_tier_users = 500

# Monthly operating costs
server_cost = 1000
support_cost = 5000
misc_cost = 2000

# TODO: Calculate total startup cost
total_startup_cost = dev_cost + marketing_cost + equipment_cost

# TODO: Caculate monthly revenue
monthly_revenue = (basic_tier_price * basic_tier_users) + (pro_tier_price * pro_tier_users)

# TODO: Calculte monthly operating cost
monthly_operating_cost = server_cost + support_cost + misc_cost

# TODO: Calculate monthly profit
months_profit = monthly_revenue - monthly_operating_cost


# TODO: Calculate months to break even

months_to_break_even = total_startup_cost / months_profit

# TODO: Display results using formated strings
print("Financial Projects:")
print(f"print total startup cost: ${total_startup_cost:,.2f}")
print(f"monthly revenue: ${monthly_revenue:,.2f}")
print(F"monthly profit: ${months_profit:,.2f}")
print(F"months to break even: {months_to_break_even:,.1f}")
# Use f-strings to display the results here

# Sensativity analysis
print("\nSensitivity Analysis:")
# TODO: Adjust user numbers
basic_tier_users += 500
pro_tier_users += 200

# TODO: Recalculate metrics with new users numbers
new_monthly_revenue = (basic_tier_price * basic_tier_users) + (pro_tier_price * pro_tier_users)
new_monthly_profit = new_monthly_revenue - monthly_operating_cost
new_months_to_break_even = total_startup_cost / new_monthly_profit

# TODO: Display updated results
print("Updated Financial Projects:")
# Use f-srings to display the updated results here
print(f"new monthly revenue: ${new_monthly_revenue:,.2f}")
print(f"new monthly profit: ${new_monthly_profit:,.2f}")
print(f"new months to break even: {new_months_to_break_even:,.1f}")

#calculate and display the impact of changes
revenue_increase = new_monthly_revenue - monthly_revenue
profit_increase = new_monthly_profit - months_profit
break_even_improvement = months_to_break_even - new_months_to_break_even

print("\nImpact of user increase:")
print(f"Revenue Increase: ${revenue_increase:,.2f}")
print(F"Profit Increase: ${profit_increase:,.2f}")
print(f"Break-Even Time Reduction: {break_even_improvement:,.1f}")














































