import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.player1_name = tk.simpledialog.askstring("Player 1", "Enter Player 1 name (X):")
        self.player2_name = tk.simpledialog.askstring("Player 2", "Enter Player 2 name (O):")

        if not self.player1_name:
            self.player1_name = "Player 1"
        if not self.player2_name:
            self.player2_name = "Player 2"

        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text=" ",
                    font=("Arial", 25),
                    width=6,
                    height=3,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == " ":
            if self.current_player == "X":
                button.config(text="X", fg="red")
            else:
                button.config(text="O", fg="blue")

            if self.check_winner():
                winner_name = self.player1_name if self.current_player == "X" else self.player2_name
                messagebox.showinfo("Game Over", f"🎉 Player {winner_name} wins!")
                self.reset_board()
                return

            if self.is_full():
                messagebox.showinfo("Game Over", "🤝 It's a draw!")
                self.reset_board()
                return

            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.buttons
        for row in b:
            if row[0]["text"] == row[1]["text"] == row[2]["text"] != " ":
                return True
        for col in range(3):
            if b[0][col]["text"] == b[1][col]["text"] == b[2][col]["text"] != " ":
                return True
        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] != " ":
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] != " ":
            return True
        return False

    def is_full(self):
        return all(self.buttons[r][c]["text"] != " " for r in range(3) for c in range(3))

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
