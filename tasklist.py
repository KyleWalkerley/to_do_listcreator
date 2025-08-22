from pathlib import Path
import json
from uuid import uuid4

tasks: list[dict] = []
DATA_PATH = Path("tasks.json")

#user will select one of the follwoing options from the menu
def print_menu():
    menu_options = [
        "Add a task",
        "List tasks",
        "View all tasks",
        "Mark done",
        "Delete",
        "Save",
        "Load",
        "Exit",
    ]
    print("\n=== TO‑DO ===")
    for idx, option in enumerate(menu_options, 1):
        print(f"{idx}. {option}")

def get_choice(min_opt: int, max_opt: int) -> int:
    while True:
        try:
            choice = int(input(f"Select an option ({min_opt}-{max_opt}): ").strip())
            if min_opt <= choice <= max_opt:
                return choice
            print("Out of range. Try again.")
        except ValueError:
            print("Please enter a number.")


def add_task():
    print("[Add task] — not implemented yet.")

def list_pending():
    print("[List pending] — not implemented yet.")

def list_all():
    print("[View all] — not implemented yet.")

def mark_done():
    print("[Mark done] — not implemented yet.")

def delete_task():
    print("[Delete] — not implemented yet.")

def save_tasks():
    print("[Save] — not implemented yet.")

def load_tasks():
    print("[Load] — not implemented yet.")


# Mai loop being run
def main():
    while True:
        print_menu()
        choice = get_choice(1, 8)
        if choice == 1:
            add_task()
        elif choice == 2:
            list_pending()
        elif choice == 3:
            list_all()
        elif choice == 4:
            mark_done()
        elif choice == 5:
            delete_task()
        elif choice == 6:
            save_tasks()
        elif choice == 7:
            load_tasks()
        elif choice == 8:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()