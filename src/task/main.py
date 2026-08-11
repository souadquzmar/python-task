import string_utils
from list_utils import remove_duplicates
from dict_utils import merge_dicts
from file_utils import save_and_read_notes, show_last_notes


def main():
    while True:
        print("=== PYTHON PRACTICE MENU ===")
        print("1. Run User Input Task")
        print("2. Run List Duplicates Task")
        print("3. Run Merge Dictionaries Task")
        print("5A. Add Note (Append to file)")
        print("5B. Show Last 5 Notes")
        print("6. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            print(string_utils.get_user_info())
        elif choice == "2":
            sample = [10, 20, 20, 30, 10, 40, 50, 40]
            print(f"Unique list: {remove_duplicates(sample)}")
        elif choice == "3":
            print(merge_dicts({"apples": 5, "bananas": 3}, {"apples": 4, "oranges": 8}))
        elif choice.upper() == "5A":
            read_user_input = string_utils.read_raw_input()
            save_and_read_notes("notes.txt", read_user_input)
        elif choice.upper() == "5B":
            show_last_notes("notes.txt", limit=5)
        elif choice == "6":
            break


if __name__ == "__main__":
    main()
