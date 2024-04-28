restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Water": 1.99, "Soda": 2.50}

restaurant_menu["Main Course"]["Steak"] = 17.99

del restaurant_menu["Starters"]["Bruschetta"]

print("Updated Restaurant Menu:")
for category, items in restaurant_menu.items():
    print(category + ":")
    for item, price in items.items():
        print(f"- {item}: ${price}")
