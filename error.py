class Board_Out_Exception(Exception):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"


class Board_Used_Exception(Exception):
    def __str__(self):
        return "Вы уже стреляли в эту клетку!"


class Ship_Contact_Exception(Exception):
    def __str__(self):
        return "Нельзя ставить корабли так близко!"


class Ship_Out_Exception(Exception):
    def __str__(self):
        return "Нельзя ставить корабли за пределы доски!"


class Wrong_Point_Exception(Exception):
    def __str__(self):
        return "Неправильно введены координаты!"
