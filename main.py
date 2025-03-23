from game_logic import play_game
from utils.helpers import clear_screen

def main():
    clear_screen()
    print("=== Welcome to Count to 30 AI Game ===")

    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for playing. Goodbye!")
            break
        clear_screen()

if __name__ == "__main__":
    main()