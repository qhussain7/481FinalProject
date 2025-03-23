import os

def clear_screen():
    """
    Clears the terminal screen (cross-platform).
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_user_input(max_move):
    """
    Prompts the user until a valid move (1 to max_move) is entered.
    """
    while True:
        try:
            user_input = int(input(f"Your move (1 to {max_move}): "))
            if 1 <= user_input <= max_move:
                return user_input
            else:
                print(f"❗ Invalid input! Please choose between 1 and {max_move}.")
        except ValueError:
            print("❗ Please enter a valid number.")
