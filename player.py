import configparser
from random import randint

from board import Board
from error import Ship_Contact_Exception, Wrong_Point_Exception, Board_Used_Exception
from point import Point2D
from ship import Ship

config = configparser.ConfigParser()
config.read("text.ini", encoding="utf8")


class Player:
    def __init__(self, hid: bool) -> None:
        self._ships = []
        self._board = Board(hid)

    def add_ship(self, ship: Ship) -> None:
        if ship in self._ships:
            raise Ship_Contact_Exception
        self._ships.append(ship)

    def hit(self, point: Point2D) -> None:
        self._board.hit(point)
        if any([ship.set_hit(point) for ship in self._ships]):
            print('Попал!')
        else:
            print('Мимо!')
        self._board.update_ships(self._ships)

    @property
    def board(self) -> Board:
        return self._board

    @property
    def dead(self) -> bool:
        return all([item.check_hp() for item in self._ships])


class User(Player):
    def __init__(self) -> None:
        super().__init__(True)

    def shot(self) -> Point2D:
        while True:
            try:
                print('Твой ход!')
                _input = input('Введи координаты: ').replace(" ", "")
                sh = list(map(int, _input))
                if len(sh) != 2:
                    raise Wrong_Point_Exception
                sh = Point2D(sh[0], sh[1])
                sh.out("shot")
                return sh
            except ValueError:
                print('Неправильно введены координаты!')
            except Exception as e:
                print(e)

    def create_ship(self) -> None:
        for num in [3, 2, 2, 1, 1, 1, 1]:
            while True:
                try:
                    print(self._board)
                    _input = input(f'Введите кординаты начала и направление корабля на {num} клетки(ку): ').replace(" ", "")
                    ship = list(map(int, _input))
                    if num != 1 and len(ship) != 3:
                        raise Wrong_Point_Exception
                    elif num == 1 and len(ship) != 2:
                        raise Wrong_Point_Exception
                    elif num == 1 and len(ship) == 2:
                        ship.append(1)
                    ship = Ship(Point2D(ship[0], ship[1]), ship[2], num)
                    self.add_ship(ship)
                    self._board.update_ships(self._ships)
                    print('Успешно!')
                    break
                except ValueError:
                    print('Неправильно введены координаты!')
                except Exception as e:
                    print(e)
        print(self._board)


class AI(Player):
    def __init__(self) -> None:
        super().__init__(True)
        self._board = self.random_board()

    def shot(self) -> Point2D:
        sh = Point2D(randint(1, 7), randint(1, 7))
        return sh

    def random_board(self):
        board = None
        while board is None:
            board = self.create_board()
        return board

    def create_board(self) -> Board | None:
        board = Board(False)
        attempts = 0
        for num in [3, 2, 2, 1, 1, 1, 1]:
            while True:
                try:
                    attempts += 1
                    if attempts > 2000:
                        return None
                    ship = Ship(Point2D(randint(1, 7), randint(1, 7)), randint(0, 1), num)
                    self.add_ship(ship)
                    board.update_ships(self._ships)
                    break
                except Exception:
                    ...
        return board
