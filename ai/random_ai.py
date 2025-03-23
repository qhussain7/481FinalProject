import random

def get_random_ai_move(current_total, max_move):
    """
    Returns a random move between 1 and max_move.
    AI will never choose a move that goes beyond 30.
    """
    valid_moves = [i for i in range(1, max_move + 1) if current_total + i <= 30]
    return random.choice(valid_moves) if valid_moves else 1
