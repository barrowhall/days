print("Welcome to love calculator !!!")

first = input("What is the first name ? ")
second = input("What is the second name? ")

combined = first.lower() + second.lower()

t = int(combined.count("t"))
r = int(combined.count("r"))
u = int(combined.count("u"))
e = int(combined.count("e"))

l = int(combined.count("l"))
o = int(combined.count("o"))
v = int(combined.count("v"))
e1 = int(combined.count("e"))

true = t + r + u + e
love = l + o + v + e1

percent = int(str(true) + str(love))

if percent < 10 or percent > 90:
    print(f"Your score is {percent}, you go together like coke and mentos.")

elif percent >= 40 and percent <= 50:
    print(f"Your score is {percent}, you are alright together.")

else:
    print(f"Your score is {percent}.")
