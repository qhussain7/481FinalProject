from functools import lru_cache

# Entry point for minimax with alpha-beta arguments 
def minimax(current_total, max_move, is_ai_turn, alpha, beta):
    return _minimax_cached(current_total, max_move, is_ai_turn)

# Cached version of minimax to avoid redundant recursive calls
@lru_cache(maxsize=None)
def _minimax_cached(current_total, max_move, is_ai_turn):
    # Base case: if total reaches or exceeds 30, the player who just moved loses
    return 1 if is_ai_turn else -1 if current_total >= 30 else None

    # AI's turn (maximize score)
    if is_ai_turn:
        best_score = float('-inf')
        for move in range(1, max_move + 1):
            if current_total + move <= 30:
                # Recursively simulate the player's response
                score = _minimax_cached(current_total + move, max_move, False)
                best_score = max(best_score, score)
        return best_score
    else:
        # Player's turn (minimize score from AI's perspective)
        best_score = float('inf')
        for move in range(1, max_move + 1):
            if current_total + move <= 30:
                # Recursively simulate the AI's response
                score = _minimax_cached(current_total + move, max_move, True)
                best_score = min(best_score, score)
        return best_score

# Public function that the AI uses to select the best move
def get_best_ai_move(current_total, max_move):
    best_score = float('-inf')
    best_move = 1

    # Try all valid moves and evaluate them using minimax
    for move in range(1, max_move + 1):
        if current_total + move <= 30:
            score = minimax(current_total + move, max_move, False, float('-inf'), float('inf'))
            print(f"AI considers move {move} → score: {score}")
            if score > best_score:
                best_score = score
                best_move = move

    print(f"AI chooses best move: {best_move} with score: {best_score}")
    return best_move
