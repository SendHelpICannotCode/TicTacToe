import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"  # Aktueller Spieler
        self.board = [""] * 9  # Spielfeld (leere Zeichen für leere Felder)

        self.buttons = []  # Liste zur Speicherung der Buttons
        for i in range(9):
            button = tk.Button(root, text="", font=("Helvetica", 24), width=4, height=2, command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)  # Füge den Button zur Liste hinzu

    def make_move(self, position):
        if not self.board[position]:
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)  # Setze den Text auf den Button
            if self.check_winner():
                messagebox.showinfo("Spielende", f"Spieler {self.current_player} hat gewonnen!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Spielende", "Unentschieden!")
                self.reset_board()
            else:
                self.current_player = "X" if self.current_player == "O" else "O"  # Wechsle den Spieler

    def check_winner(self):
        # Kombinationen für den Sieg
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_board(self):
        for i in range(9):
            self.board[i] = ""  # Setze das Spielfeld zurück
            self.buttons[i].config(text="")  # Setze den Button-Text zurück
        self.current_player = "X"  # Setze den Startspieler auf "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
