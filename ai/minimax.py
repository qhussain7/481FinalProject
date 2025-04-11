from functools import lru_cache

# Wrapper function (keeps alpha/beta signature for compatibility)
def minimax(current_total, max_move, is_ai_turn, alpha, beta):
    return _minimax_cached(current_total, max_move, is_ai_turn)

# Cached internal minimax function
@lru_cache(maxsize=None)
def _minimax_cached(current_total, max_move, is_ai_turn):
    # Base case: whoever just moved loses if total hits or exceeds 30
    if current_total >= 30:
        return 1 if is_ai_turn else -1

    if is_ai_turn:
        best_score = float('-inf')
        for move in range(1, max_move + 1):
            if current_total + move <= 30:
                score = _minimax_cached(current_total + move, max_move, False)
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in range(1, max_move + 1):
            if current_total + move <= 30:
                score = _minimax_cached(current_total + move, max_move, True)
                best_score = min(best_score, score)
        return best_score

# Public function to select the best move
def get_best_ai_move(current_total, max_move):
    best_score = float('-inf')
    best_move = 1

    for move in range(1, max_move + 1):
        if current_total + move <= 30:
            score = minimax(current_total + move, max_move, False, float('-inf'), float('inf'))
            print(f"AI considers move {move} → score: {score}")
            if score > best_score:
                best_score = score
                best_move = move

    print(f"AI chooses best move: {best_move} with score: {best_score}")
    return best_move
