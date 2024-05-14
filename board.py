from error import Board_Used_Exception
from point import Point2D
from ship import Ship


class Board:
    def __init__(self, hid: bool) -> None:
        self._hid = hid
        self._b = [["O"] * 7 for _ in range(7)]

    def update_ships(self, list_ship: list[Ship]) -> None:
        for ship in list_ship:
            for point in ship.location:
                if self._hid:
                    self._b[point.x - 1][point.y - 1] = "■"
            if ship.check_hp():
                for point in ship.exclusion_zone:
                    if 0 < point.x < 8 and 0 < point.y < 8:
                        self._b[point.x - 1][point.y - 1] = '.'
            for point in ship.hit:
                self._b[point.x - 1][point.y - 1] = "X"

    def hit(self, point: Point2D) -> None:
        if self._b[point.x - 1][point.y - 1] != "■" and self._b[point.x - 1][point.y - 1] != "O":
            raise Board_Used_Exception
        self._b[point.x - 1][point.y - 1] = '.'

    def __str__(self) -> str:
        ms = f"{'-' * 33}\n"
        if self._hid:
            ms += '|           Твоё поле           |\n'
        else:
            ms += '|        Поле соперника         |\n'
        ms += f"{'-' * 33}\n"
        ms += f"| ~ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n"
        for item in range(1, 8):
            ms += f"{'-' * 33}\n"
            ms += f"| {item} | {' | '.join(self._b[item - 1])} |\n"
        ms += f"{'-' * 33}"
        return ms
