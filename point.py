from error import Board_Out_Exception, Ship_Out_Exception


class Point2D:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def exclusion_zone(self) -> list:
        return [
            Point2D(self.x - 1, self.y - 1),
            Point2D(self.x, self.y - 1),
            Point2D(self.x + 1, self.y - 1),

            Point2D(self.x - 1, self.y),
            self,
            Point2D(self.x + 1, self.y),

            Point2D(self.x - 1, self.y + 1),
            Point2D(self.x, self.y + 1),
            Point2D(self.x + 1, self.y + 1),
        ]

    def out(self, _type='ship') -> None:
        if not (0 < self.x < 8) or not (0 < self.y < 8):
            if _type == 'ship':
                raise Ship_Out_Exception
            else:
                raise Board_Out_Exception

    def __eq__(self, value) -> bool:
        return self.x == value.x and self.y == value.y
    
    def __ne__(self, value) -> bool:
        return self.x != value.x or self.y != value.y
    
    def __repr__(self) -> str:
        return f"{self.x}{self.y}"
