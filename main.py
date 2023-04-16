# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

price = 0

if size == "s":
    price += 15
elif size == "m":
    price += 20
else:
    price += 25

if add_pepperoni == "y":
    if size == "s":
        price += 2
    else:
        price += 3

if extra_cheese == "y":
    price += 1

print(f"Your final bill is: ${price}")
