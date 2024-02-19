import random

class Ship:
    def __init__(self, positions):
        self.positions = positions
        self.hits = [False] * len(positions)

class Board:
    def __init__(self, size):
        self.size = size
        self.ships = []
        self.grid = [['O' for _ in range(size)] for _ in range(size)]

    def place_ship(self, ship):
        for x, y in ship.positions:
            self.grid[x][y] = '■'

    def print_board(self):
        print("   | 1 | 2 | 3 | 4 | 5 | 6 |")
        for i in range(self.size):
            print(f"{i+1} | {' | '.join(self.grid[i])} |")

    def check_hit(self, x, y):
        if self.grid[x][y] == '■':
            self.grid[x][y] = 'X'
            for ship in self.ships:
                if (x, y) in ship.positions:
                    ship.hits[ship.positions.index((x, y))] = True
                    if all(ship.hits):
                        print("Корабль потоплен!")
            return True
        elif self.grid[x][y] == 'O':
            self.grid[x][y] = 'T'
            return False
        else:
            raise ValueError("Вы уже стреляли в эту клетку!")

def generate_ship_positions(size, length):
    positions = []
    while len(positions) < length:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        position = (x, y)
        if position not in positions:
            positions.append(position)
    return positions

def main():
    player_board = Board(6)
    computer_board = Board(6)

    for _ in range(4):
        ship_positions = generate_ship_positions(6, 1)
        player_board.ships.append(Ship(ship_positions))
        player_board.place_ship(player_board.ships[-1])

        ship_positions = generate_ship_positions(6, 1)
        computer_board.ships.append(Ship(ship_positions))
        computer_board.place_ship(computer_board.ships[-1])

    player_board.print_board()

    while True:
        try:
            player_move_x = int(input("Введите номер строки для выстрела (1-6): ")) - 1
            player_move_y = int(input("Введите номер столбца для выстрела (1-6): ")) - 1

            if player_board.check_hit(player_move_x, player_move_y):
                print("Попадание!")
            else:
                print("Промах!")

            player_board.print_board()

            # Ход компьютера
            computer_move_x = random.randint(0, 5)
            computer_move_y = random.randint(0, 5)

            if computer_board.check_hit(computer_move_x, computer_move_y):
                print("Компьютер попал!")
            else:
                print("Компьютер промахнулся!")

            computer_board.print_board()

            if all(all(cell != '■' for cell in row) for row in player_board.grid):
                print("Победил компьютер!")
                break
            elif all(all(cell != '■' for cell in row) for row in computer_board.grid):
                print("Вы победили!")
                break

        except (ValueError, IndexError):
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
