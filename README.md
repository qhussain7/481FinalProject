# 🎮 Count to 30 AI Game (Minimax Edition)

This project is a strategic number game built for an Artificial Intelligence course. Players take turns adding numbers to a running total — whoever says **30** loses.

The AI opponent is powered by the **Minimax algorithm with Alpha-Beta Pruning**, ensuring optimal decision-making each turn.

---

## 🧠 How the Game Works

- At the **start of each game**, a random max move (between **2 and 5**) is chosen.
- On each turn, the player or AI can choose any number from **1 up to that max**.
- The number is added to a running total starting from **0**.
- The player who reaches **30** **loses the game**.
- After each game, players can **choose to play again**.

---

## 🧱 Folder Structure

```
count_to_30_ai/
│
├── main.py                  # Entry point
├── game_logic.py            # Game logic and flow
│
├── ai/
│   ├── __init__.py
│   ├── minimax.py           # Minimax with Alpha-Beta AI logic
│   └── random_ai.py         # Simple random-move AI (used for testing)
│
├── utils/
│   ├── __init__.py
│   └── helpers.py           # Input handling and screen clearing
│
├── data/
│   └── scores.json          # Track wins and losses
│
├── tests/
│   ├── __init__.py
│   └── test_ai_logic.py     # Unit tests for Minimax logic
│
└── README.md
```

---

## ▶️ How to Run the Game

```bash
python main.py
```

To run the unit tests:

```bash
python -m unittest tests/test_ai_logic.py
```

---

## 🎓 Course Context

This project was developed for a college-level **Artificial Intelligence course**, demonstrating:
- Game-playing agents
- Search-based AI (Minimax + Alpha-Beta Pruning)
- Handling dynamic rule constraints (randomized per game)

---

## 👥 Team Members

- Qasim Hussain  
- Justin Ramirez  
- Ethan Wu  
- Quang Le

---

## ✅ Requirements

- Python 3.6 or newer
- No external libraries required

---

## 💡 Future Enhancements

- [ ] GUI using Pygame  
- [ ] AI difficulty levels  
- [ ] Scoreboard tracking in `scores.json`  
- [ ] Option to let player choose who goes first

---