def is_year_leap(year):
    return year % 4 == 0


chosen_year = 2020

leap_year_result = is_year_leap(chosen_year)

print(f"Год {chosen_year}: {leap_year_result}")
