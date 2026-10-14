shopping_list = []

while True:
    choice = input("add / remove / show / done: ").strip().lower()

    if choice == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f"{item} added to your list.")

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("Your shopping list:")
            for item in shopping_list:
                print(item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please pick add, remove, show, or done.")
