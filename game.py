import numpy as np

class DotsAndBoxes:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows + 1, cols + 1), dtype=int)
        self.lines = np.zeros((rows, cols), dtype=int)
        self.scores = [0, 0]
        self.current_player = 0

    def print_grid(self):
        for r in range(self.rows + 1):
            for c in range(self.cols + 1):
                print(f"{self.grid[r, c]:2}", end=" ")
            print()
            if r < self.rows:
                for c in range(self.cols):
                    if self.lines[r, c] == 1:
                        print(" ---", end="")
                    else:
                        print("    ", end="")
                print()
                for c in range(self.cols + 1):
                    if self.lines[r, c] == 2:
                        print("|", end="   ")
                    else:
                        print(" ", end="   ")
                print()

    def make_move(self, r, c, direction):
        if direction == "H":
            if r < self.rows and 0 <= c < self.cols and self.lines[r, c] == 0:
                self.lines[r, c] = 1
                if self.check_box_completion(r, c, direction):
                    self.scores[self.current_player] += 1
                    return True
                return False
        elif direction == "V":
            if 0 <= r < self.rows and c < self.cols and self.lines[r, c] == 0:
                self.lines[r, c] = 2
                if self.check_box_completion(r, c, direction):
                    self.scores[self.current_player] += 1
                    return True
                return False
        return False

    def check_box_completion(self, r, c, direction):
        completed = False
        if direction == "H":
            if r > 0 and self.lines[r - 1, c] == 2 and self.lines[r, c] == 1:
                if self.lines[r - 1, c] == 2 and self.lines[r, c] == 1:
                    completed = True
            if r < self.rows - 1 and self.lines[r + 1, c] == 2 and self.lines[r, c] == 1:
                if self.lines[r + 1, c] == 2 and self.lines[r, c] == 1:
                    completed = True
        elif direction == "V":
            if c > 0 and self.lines[r, c - 1] == 1 and self.lines[r, c] == 2:
                if self.lines[r, c - 1] == 1 and self.lines[r, c] == 2:
                    completed = True
            if c < self.cols - 1 and self.lines[r, c + 1] == 1 and self.lines[r, c] == 2:
                if self.lines[r, c + 1] == 1 and self.lines[r, c] == 2:
                    completed = True
        return completed

    def play(self):
        while True:
            self.print_grid()
            print(f"Player {self.current_player + 1}'s turn")
            try:
                r, c, direction = input("Enter move (row col direction): ").split()
                r, c = int(r), int(c)
                if self.make_move(r, c, direction.upper()):
                    print("Box completed!")
                else:
                    self.current_player = 1 - self.current_player
            except (ValueError, IndexError):
                print("Invalid input. Please enter in the format 'row col direction'.")

            if np.all(self.lines > 0):
                self.print_grid()
                print("Game over!")
                print(f"Player 1 score: {self.scores[0]}")
                print(f"Player 2 score: {self.scores[1]}")
                if self.scores[0] > self.scores[1]:
                    print("Player 1 wins!")
                elif self.scores[1] > self.scores[0]:
                    print("Player 2 wins!")
                else:
                    print("It's a tie!")
                break

# Example usage:
if __name__ == "__main__":
    rows = 3
    cols = 3
    game = DotsAndBoxes(rows, cols)
    game.play()
