from universal_globals import (width, height)

class Shrek:
    def __init__(self):
        self.canvas = [([" "] * width) for x in range(height-1)]
    def overwrite_char(self, x, y, char):
        self.canvas[y][x] = char
    def print(self):
        print("\n".join(["".join(x) for x in self.canvas]))