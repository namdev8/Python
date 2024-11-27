day=int(input("Enter the day (1-31):"))
month=int(input("Enter the month (1-12):"))
year=int(input("Enter the year (eg: 2024):"))
print(f"The entered date is: {day:02d}-{month:02d}-{year}")
if (year%4==0 and year%100!=0 or year%400==0):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")