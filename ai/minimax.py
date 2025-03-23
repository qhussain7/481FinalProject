def minimax(current_total, max_move, is_ai_turn, alpha, beta):
    """
    Recursive Minimax algorithm with Alpha-Beta Pruning.
    AI tries to force the opponent to say 30.
    Returns a score: +1 if AI wins, -1 if AI loses.
    """
    if current_total >= 30:
        return -1 if is_ai_turn else 1

    if is_ai_turn:
        max_eval = float('-inf')
        for move in range(1, max_move + 1):
            if current_total + move <= 30:
                eval = minimax(current_total + move, max_move, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for move in range(1, max_move + 1):
            if current_total + move <= 30:
                eval = minimax(current_total + move, max_move, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


def get_best_ai_move(current_total, max_move):
    """
    Returns the best possible move for the AI using Minimax.
    """
    best_score = float('-inf')
    best_move = 1

    for move in range(1, max_move + 1):
        if current_total + move <= 30:
            score = minimax(current_total + move, max_move, False, float('-inf'), float('inf'))
            if score > best_score:
                best_score = score
                best_move = move

    return best_move
