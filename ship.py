from error import Board_Used_Exception
from point import Point2D


class Ship:
    def __init__(self, point: Point2D, direction: int, size: int) -> None:
        point.out()
        self._hp = size
        self._location = self.gen_location(point, direction)
        self._exclusion_zone = [exclusion_zone for item in self._location for exclusion_zone in item.exclusion_zone]
        self._hit = []

    @property
    def location(self) -> list[Point2D]:
        return self._location

    @property
    def hit(self) -> list[Point2D]:
        return self._hit

    def set_hit(self, point: Point2D) -> None:
        if point in self._location:
            if point in self._hit:
                raise Board_Used_Exception
            self._hit.append(point)
            return True
        else:
            return False

    @property
    def exclusion_zone(self) -> list[Point2D]:
        return self._exclusion_zone

    def gen_location(self, point: Point2D, direction: int) -> list[Point2D]:
        _list = [point]
        if direction == 1:
            for item in range(1, self._hp):
                new_point = Point2D(point.x + item, point.y)
                new_point.out()
                _list.append(new_point)
        else:
            for item in range(1, self._hp):
                new_point = Point2D(point.x, point.y + item)
                new_point.out()
                _list.append(new_point)
        return _list

    def check_hp(self) -> bool:
        return len(self._hit) == self._hp

    def __eq__(self, ship) -> bool:
        for item in ship.location:
            if item in self._exclusion_zone:
                return True
        return False

    def __repr__(self) -> str:
        return f"<Ship {self._location}>"
