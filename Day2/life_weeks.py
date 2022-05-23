age = input("What is your age : ")

days = round(90 * 365 - int(age) * 365)
weeks = round(90 * 52 - int(age) * 52)
months = round(90 * 12 - int(age) * 12)

print(f"You have {days} days, {weeks} weeks and {months} months left.")

# Another way

years = 90 - int(age)

day = years * 365
week = years * 52
month = years * 12

print(f"You have {day} days, {week} weeks, and {month} months left!!!")