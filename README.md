# 🎮 Count to 30 AI Game (Minimax Edition)

This project is a strategic number game built for an Artificial Intelligence course. Players take turns adding numbers to a running total — **whoever says 30 loses**.

The AI opponent is powered by the **Minimax algorithm with Alpha-Beta Pruning and memoization**, ensuring near-perfect decision-making each turn. You can also play against the AI interactively using a **Tkinter GUI**.

---

## 🧠 How the Game Works

- At the start of each game, a **max move limit** is selected (2 to 5).
- On each turn, the player and AI can choose any number from **1 to max_move**.
- That number is added to a **running total starting from 0**.
- The first to say **30** **loses the game**.
- The game continues until one player hits 30, then offers a replay.

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
Graphical Tkinter version

```bash
python gui.py
```
Benchmark the AI (Minimax vs Random over 10,000 games):
```bash
python evaluate_ai.py
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
