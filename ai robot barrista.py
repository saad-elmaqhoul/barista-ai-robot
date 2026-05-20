import time

print("=== WELCOME TO THE AI BARISTA PRO ===\n")

# Swlna l-kliyane 3la smito o l-3mar dyalo
name = input("Write your name = ")
last_name = input("Write your last name = ")
age = int(input("Write your age = "))

print(f"\nHello {name} {last_name}! Welcome back to our coffee shop.")

# L-Menu dyal l-qahwa m3a l-as3ar
menu = {
    "1": {"name": "Espresso", "price": 15},
    "2": {"name": "Café au lait", "price": 20},
    "3": {"name": "Cappuccino", "price": 25},
    "4": {"name": "Hot Chocolate", "price": 22}
}

# L-Menu dyal l-idafat (Add-ons)
customizations = {
    "1": {"name": "Extra Sugar", "price": 2},
    "2": {"name": "Caramel Syrup", "price": 5},
    "3": {"name": "Whipped Cream", "price": 4},
    "4": {"name": "No Additions", "price": 0}
}

order_items = []
total_bill = 0

# Hna derna wahd l-boucle (while loop) bach l-kliyane yqder y3zel bzaf d l-mchrwbat
while True:
    print("\n--- OUR MENU ---")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - {item['price']} DH")
    
    choice = input("\nPlease enter the number of your drink (1-4): ")
    
    if choice in menu:
        selected_drink = menu[choice]
        print(f"\nYou selected: {selected_drink['name']}") 
        
        # Ikhtiyar l-idafat
        print("\n--- CUSTOMIZE YOUR DRINK ---")
        for c_key, c_item in customizations.items():
            print(f"{c_key}. {c_item['name']} (+{c_item['price']} DH)")
            
        c_choice = input("Choose an addition (1-4): ")
        selected_addon = customizations.get(c_choice, customizations["4"])
        
        # Hsabi l-taman dyal l-kass wahed m3a l-idafat
        item_total = selected_drink['price'] + selected_addon['price']
        total_bill += item_total
        
        # Hifd l-talab f l-qaima
        order_items.append(f"{selected_drink['name']} x1 (+ {selected_addon['name']})")
        print(f"Added to cart! Current Total: {total_bill} DH")
    else:
        print("Invalid choice. Please select from the menu.")
        continue
        
    # Sowl l-kliyane wach bgha yzid chi haja khra
    another = input("\nDo you want to order anything else? (yes/no): ").lower()
    if another != 'yes' and another != 'y':
        break

# Hna fin kankh rjo l-fatora nadiya
print("\n" + "="*40)
print(f"--- DIGITAL RECEIPT FOR {name.upper()} ---")
print("="*40)
print("Items Ordered:")
for item in order_items:
    print(f"- {item}")

print("-"*40)
tva = total_bill * 0.10  # 10% dyal l-dariba
final_total = total_bill + tva

print(f"Subtotal: {total_bill} DH")
print(f"TVA (10%): {tva:.2f} DH")
print(f"Total Bill: {final_total:.2f} DH")
print("="*40)

# Marhalat l-khalas (Payment)
while True:
    try:
        cash = float(input(f"\nPlease enter cash amount ({final_total:.2f} DH or more): "))
        if cash >= final_total:
            change = cash - final_total
            print(f"Thank you! Your change is: {change:.2f} DH")
            print("\nPreparing your order...")
            time.sleep(2) # Wahd l-waqt khfif dial l-khidma
            print("☕ Your coffee is ready! Enjoy your day!")
            break
        else:
            print(f"Not enough cash. You still owe {final_total - cash:.2f} DH")
    except ValueError:
        print("Please enter a valid number.") 
