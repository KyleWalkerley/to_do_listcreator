#user will select one of the follwoing options from the menu
menu_options = [
    "Add a task",
    "list tasks",
    "View all tasks",
    "Mark done",
    "Delete",
    "Save",
    "Load",
    "Exit"
]

for idx, option in enumerate(menu_options, 1):
    print(f"{idx}. {option}")

choice = int(input("Select an option (1-8): "))

