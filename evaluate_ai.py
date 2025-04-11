import random
from ai.minimax import get_best_ai_move
from ai.random_ai import get_random_ai_move

def play_game(max_move, minimax_starts):
    total = 0
    is_minimax_turn = minimax_starts

    while total < 30:
        if is_minimax_turn:
            move = get_best_ai_move(total, max_move)
        else:
            move = get_random_ai_move(total, max_move)

        total += move
        if total >= 30:
            return not is_minimax_turn 

        is_minimax_turn = not is_minimax_turn

def evaluate(minimax_first=True, iterations=10000, max_move=3):
    minimax_wins = 0

    for i in range(iterations):
        starts = minimax_first if i % 2 == 0 else not minimax_first
        if play_game(max_move, starts):
            minimax_wins += 1

    print(f"\nResults after {iterations} games with max_move = {max_move}:")
    print(f"✅ Minimax AI wins: {minimax_wins}")
    print(f"❌ Random AI wins: {iterations - minimax_wins}")
    print(f"🏆 Win rate: {minimax_wins / iterations * 100:.2f}%")

if __name__ == "__main__":
    for max_move in range(2, 6):  
        evaluate(minimax_first=True, iterations=10000, max_move=max_move)
        print("-" * 40)
