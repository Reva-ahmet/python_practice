from datetime import datetime

birth_year = int(input("Enert your birth year: "))
current_year = datetime.now().year
current_age = current_year - birth_year

year = int(input("Entey a year: "))
year_age = year - birth_year


print(f"Your current age is {current_age}, and your age in {year} will be {year_age} ")