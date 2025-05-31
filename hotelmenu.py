menu = {
    'pizza':100,
    'burger':200,
    'pasta':300,
    'salad':400,
    'icecream':500,
}

print("Welcome to python restaurant")
print("pizza:Rs40\npasta:Rs100\nburger:Rs20\nsalad:Rs30\nicecream:Rs50")


order_total = 0
item_1 = input("Enter the name of item you want to order =")

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1}has been added to your order")

else:
    print(f"ordered item{item_1}is not avaialable yet!")
another_order = input("Do you want to add another item?")


if another_order == "Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2}has been added to your order")
    else:
        print(f"ordered item{item_2}is not avaialable yet!")
else:
    print("Thank you for your order!")
print(f"Your total bill is {order_total}")
print("Thank you for your order!")

