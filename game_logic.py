import random
from ai.minimax import get_best_ai_move
from utils.helpers import get_valid_user_input

def play_game():
    print("\nStarting a new game of Count to 30!")

    max_move = random.randint(2, 5)
    print(f"🔢 This game's max move per turn is: {max_move}")

    total = 0
    player_turn = True  # True = User, False = AI

    while total < 30:
        print(f"\nCurrent total: {total}")

        if player_turn:
            move = get_valid_user_input(max_move)
            total += move
            print(f"🧑 You chose: {move}")
            if total >= 30:
                print("❌ You said 30. You lose!")
                break
        else:
            move = get_best_ai_move(total, max_move)
            print(f"🤖 AI chooses: {move}")
            total += move
            if total >= 30:
                print("✅ AI said 30. AI loses!")
                break

        player_turn = not player_turn
