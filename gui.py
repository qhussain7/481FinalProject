import tkinter as tk
from ai.minimax import get_best_ai_move
import random

MAX_MOVE = 3  #default max move per turn
TARGET_TOTAL = 30

class CountTo30GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Count to 30 AI Game")
        self.total = 0
        self.max_move = 3  
        self.game_over = False

        self.select_label = tk.Label(root, text="Select max move per turn:", font=("Arial", 14))
        self.select_label.pack(pady=(10, 0))

        self.max_move_var = tk.IntVar(value=self.max_move)
        self.dropdown = tk.OptionMenu(root, self.max_move_var, 2, 3, 4, 5)
        self.dropdown.config(font=("Arial", 12))
        self.dropdown.pack()

        self.start_button = tk.Button(root, text="Start Game", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=10)

        self.label = tk.Label(root, text="", font=("Arial", 24))
        self.buttons_frame = tk.Frame(root)
        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.reset_button = tk.Button(root, text="Play Again", font=("Arial", 14),
                                      command=self.reset_game, state="disabled")

    def start_game(self):
        self.max_move = self.max_move_var.get()
        self.start_button.config(state="disabled")
        self.dropdown.config(state="disabled")

        self.label.config(text=f"Current total: {self.total}")
        self.label.pack(pady=20)
        self.buttons_frame.pack()
        self.result_label.pack(pady=10)
        self.reset_button.pack(pady=10)

        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        self.buttons = []
        for i in range(1, self.max_move + 1):
            btn = tk.Button(self.buttons_frame, text=str(i), font=("Arial", 18),
                            command=lambda m=i: self.user_move(m), width=5)
            btn.grid(row=0, column=i-1, padx=5)
            self.buttons.append(btn)

    def user_move(self, move):
        if self.game_over or self.total + move > TARGET_TOTAL:
            return

        self.total += move
        self.label.config(text=f"Current total: {self.total}")
        if self.total >= TARGET_TOTAL:
            self.result_label.config(text="❌ You said 30. You lose!")
            self.end_game()
            return

        self.root.after(500, self.ai_move)

    def ai_move(self):
        if self.game_over:
            return

        move = get_best_ai_move(self.total, MAX_MOVE)
        self.total += move
        self.label.config(text=f"Current total: {self.total}")
        self.result_label.config(text=f"🤖 AI chose {move}")

        if self.total >= TARGET_TOTAL:
            self.result_label.config(text="✅ AI said 30. AI loses! You win!")
            self.end_game()

    def end_game(self):
        self.game_over = True
        for btn in self.buttons:
            btn.config(state="disabled")
        self.reset_button.config(state="normal")

    def reset_game(self):
        self.total = 0
        self.game_over = False
        self.label.config(text="")
        self.result_label.config(text="")
        for btn in self.buttons:
            btn.config(state="normal")
        self.reset_button.config(state="disabled")
        self.start_button.config(state="normal")
        self.dropdown.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = CountTo30GUI(root)
    root.mainloop()
