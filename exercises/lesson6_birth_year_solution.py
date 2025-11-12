from datetime import datetime
#current_year = 2025
birth_year = input("enter a year born: ")
current_year = datetime.now().year

age = current_year - int(birth_year)

print(f"You are approximately {age} years old.")