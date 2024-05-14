import configparser
from time import sleep

from player import User, AI

config = configparser.ConfigParser()
config.read("text.ini", encoding="utf8")


class Game:
    def __init__(self) -> None:
        self._player = User()
        self._ai = AI()
        self.run_game = self.menu()

    def end(self) -> bool:
        if self._player.dead:
            print('Победитель соперник!!!')
            return True
        if self._ai.dead:
            print('Победитель игрок!!!')
            return True
        return False

    def game(self) -> None:
        print(config['game']['game_start'])
        while True:
            sleep(2)
            if self.end(): break
            print(self._ai.board)
            while True:
                try:
                    shot = self._player.shot()
                    self._ai.hit(shot)
                    break
                except Exception as e:
                    print(e)
            sleep(1)
            print(self._ai.board)
            sleep(2)
            if self.end(): break
            print(self._player.board)
            sleep(1)
            print('Ход соперника!')
            while True:
                try:
                    shot = self._ai.shot()
                    print(f'Координаты: {shot}')
                    self._player.hit(shot)
                    break
                except Exception as e:
                    print(e)
            sleep(1)
            print(self._player.board)
            
    def game_start(self) -> None:
        print(config['game']['start'])
        self._player.create_ship()
        self.game()

    def menu(self) -> bool:
        print(config['menu']['welcome'])
        while True:
            print('-' * 17)
            print(config['menu']['menu'])
            print('-' * 17)
            run = input(config['menu']['input'])
            if run == '1':
                self.game_start()
            elif run == '2':
                self.rules()
            elif run == '3':
                return False

    def rules(self) -> None:
        ms = '-' * 17
        ms += config['menu']['rules']
        print(ms)
