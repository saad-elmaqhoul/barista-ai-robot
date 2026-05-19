print("=== WELCOME TO THE AI BARISTA ===\n")

# Swlna l-kliyane 3la smito o l-3mar dyalo
name = input("Write your name = ")
last_name = input("Write your last name = ")
age = int(input("Write your age = "))

print(f"\nHello {name} {last_name}! Welcome to our coffee shop.")

# L-Menu dyal l-qahwa
menu = {
    "1": {"name": "Espresso", "price": 15},
    "2": {"name": "Café au lait", "price": 20},
    "3": {"name": "Cappuccino", "price": 25},
    "4": {"name": "Hot Chocolate", "price": 22}
}

# Hna derna wahd l-boucle (while loop) bach ila bgha y-bdel l-ikhtiyar, n-rejj3oh hna
while True:
    print("\n--- OUR MENU ---")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - {item['price']} DH")

    choice = input("\nPlease enter the number of your drink (1-4): ")

    if choice in menu:
        selected_drink = menu[choice]["name"]
        price = menu[choice]["price"]

        # Hna fin l-robot dki o kay-tchika l-3mar
        if age < 12 and choice == "1":
            print(f"\n[AI Barista]: {selected_drink} might be too strong for your age!")
            # Robot daba ghadi y-khallih y-khtar: y-kemmel awla y-bdel
            decision = input("Do you want to keep your choice or change it? (Type 'keep' or 'change'): ").lower()

            if decision == 'change':
                print("\n[AI Barista]: Alright, let's look at the menu again.")
                continue  # had 'continue' kat-rejj3o l-bdaya d l-menu bach y-khtar mn jdid
            else:
                print("\n[AI Barista]: As you wish!")

        # Ila l-3mar kbir awla l-kliyane sghir o bgha y-kemmel
        print(f"\n[AI Barista]: Great choice! Preparing your {selected_drink}...")
        print(f"That will be {price} DH. Enjoy your drink, {name}!")
        break  # l-loop kat-sali hit l-order t-gad

    else:
        print("\n[AI Barista]: Sorry, that item is not in our menu. Please try again!")