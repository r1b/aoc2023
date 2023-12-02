import sys

class GameTurn:
    blue: int
    green: int
    red: int

    def __init__(self, turn):
        self.blue = 0
        self.green = 0
        self.red = 0

        for record in turn.split(", "):
            raw_count, color = record.split(" ")
            count = int(raw_count)

            if color == "blue":
                self.blue = count
            elif color == "green":
                self.green = count
            elif color == "red":
                self.red = count

class Game:
    id_: int
    turns: list[GameTurn]

    def __init__(self, game):
        header, rest = game.split(":")
        self.id_ = int(header[len("Game "):])
        self.turns = [GameTurn(turn.strip()) for turn in rest.split(";")]


def part2(puzzle):
    games = [Game(line) for line in puzzle]
    total = 0

    for game in games:
        blue, green, red = 0, 0, 0
        for turn in game.turns:
            blue = max(blue, turn.blue)
            green = max(green, turn.green)
            red = max(red, turn.red)
        total += blue * green * red

    print(total)

if __name__ == "__main__":
    with open(sys.argv[1]) as puzzle:
        part2(puzzle)
