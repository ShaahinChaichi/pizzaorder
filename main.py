# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

price = 0

if size == "s":
    price = price + 15
elif size == "m":
    price = price + 20
elif size == 'l':
    price = price + 25
else:
    if add_pepperoni == "y":
        if size == "s":
            price = price + 2
        elif size == "m":
            price == price + 3
        elif size == "l":
            price = price + 3
        else:
            price = price + 1
    else:
        if extra_cheese == "y":
            price = price + 1
        else:
            print("\n")

print(f"Your final bill is: ${price}")
