# inventory.py

inventory = {"1":"buy fruits","2":"buy clothes","3":"buy sugar","3":"buy sugar","4":"buy sugar"}

def add_item():
    name = input("Enter item name: ").strip()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    inventory[name] = {"quantity": quantity, "price": price}
    print(f"✅ Added '{name}' to inventory.\n")

def view_inventory():
    if not inventory:
        print("📦 Inventory is empty.\n")
        return

    print("\n--- Current Inventory ---")
    for name, details in inventory.items():
        print(f"{name}: {details['quantity']} units @ ₹{details['price']:.2f} each")
    print()

def update_item():
    name = input("Enter item name to update: ").strip()
    if name not in inventory:
        print("❌ Item not found.\n")
        return

    quantity = int(input("Enter new quantity: "))
    price = float(input("Enter new price: "))

    inventory[name]["quantity"] = quantity
    inventory[name]["price"] = price
    print(f"✅ Updated '{name}' successfully.\n")

def remove_item():
    name = input("Enter item name to remove: ").strip()
    if name in inventory:
        del inventory[name]
        print(f"🗑️ Removed '{name}' from inventory.\n")
    else:
        print("❌ Item not found.\n")

def main():
    while True:
        print("==== INVENTORY MENU ====")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
