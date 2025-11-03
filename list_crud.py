# Fruit Basket Program - Fully Fixed

basket = []

def print_basket():
    print("\n--- Current Fruits in Basket ---")
    if not basket:
        print("[No fruits yet!]")
    else:
        for i, fruit in enumerate(basket, start=1):
            print(f"{i}) {fruit.capitalize()}")
    print("-------------------------------")

while True:
    print("\n===== FRUIT BASKET MENU =====")
    print("1. Show Basket")
    print("2. Add Fruit")
    print("3. Remove Fruit")
    print("4. Quit")
    print("==============================")

    option = input("Select an option [1-4]: ").strip()

    if not option.isdigit():
        print("Invalid input! Enter a number from 1 to 4.")
        continue

    option = int(option)

    if option == 1:
        print_basket()

    elif option == 2:
        new_fruit = input("Enter the fruit you want to add: ").strip().lower()
        if new_fruit:
            basket.append(new_fruit)
            print(f"\n'{new_fruit}' has been added to your basket.")
        else:
            print("No fruit entered.")
        print_basket()

    elif option == 3:
        if not basket:
            print("Basket is empty. Nothing to remove.")
            continue

        print_basket()
        remove_choice = input("Enter the fruit name or number to remove: ").strip().lower()

        # Remove by number
        if remove_choice.isdigit():
            index = int(remove_choice)
            if 1 <= index <= len(basket):
                removed = basket.pop(index - 1)
                print(f"\n'{removed}' has been removed from your basket.")
            else:
                print("Invalid number!")
        # Remove by name
        else:
            # Find first item in basket matching user input (case-insensitive)
            found = False
            for fruit in basket:
                if fruit.lower() == remove_choice:
                    basket.remove(fruit)
                    print(f"\n'{fruit}' has been removed from your basket.")
                    found = True
                    break
            if not found:
                print(f"'{remove_choice}' is not in your basket.")

        print_basket()

    elif option == 4:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 4.")
