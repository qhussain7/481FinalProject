import unittest
from ai.minimax import get_best_ai_move

class TestMinimaxAI(unittest.TestCase):

    def test_ai_never_chooses_invalid_move(self):
        for max_move in range(2, 6):
            for total in range(0, 30):
                move = get_best_ai_move(total, max_move)
                self.assertIn(move, range(1, max_move + 1))
                self.assertLessEqual(total + move, 30)

    def test_ai_wins_when_it_should(self):
        # If total = 26 and max_move = 3, AI can force player to say 30
        total = 26
        max_move = 3
        move = get_best_ai_move(total, max_move)
        self.assertEqual(move, 3)  # 26 + 3 = 29 → player is forced to say 30

    def test_ai_blocks_player_win(self):
        # If total = 27 and max_move = 3, player could win unless AI plays 2
        total = 27
        max_move = 3
        move = get_best_ai_move(total, max_move)
        self.assertEqual(move, 2)  # Leaves player at 29

if __name__ == "__main__":
    unittest.main()
