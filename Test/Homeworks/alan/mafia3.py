MAFIA = 'мафиозник'
CIVILIAN = 'мирный'
SHERIFF = 'шериф'


class Player:
    def __init__(self, name, role, is_alive=True):
        self.name = name
        self.role = role
        self.is_alive = is_alive

    def day_move(self, players):
        input(f'Дневной ход для {self.name}')

    def night_move(self, players):
        input(f'Ночной ход для {self.name}')
        if self.role == MAFIA:
            self.mafia_night_menu(players)
        elif self.role == CIVILIAN:
            self.civilian_night_menu()
        elif self.role == SHERIFF:
            self.sheriff_night_menu(players)
        input('Конец хода')

    def mafia_night_menu(self, players):
        alive_players = get_alive_players(players)
        i = 1
        for player in alive_players:
            print(f"{i} - {player.name}")
            i += 1
        index = int(input('Кого вы выбираете: ')) - 1
        player = alive_players[index]
        if player is not self:
            player.is_alive = False
            print(f'Удачно извлечен {player.name}')
        else:
            print('Самоубийца - это не ваша роль')

    def civilian_night_menu(self):
        print('Вы спите:)')

    def sheriff_night_menu(self, players):
        pass


def get_alive_players(players):
    alive_players = []
    for player in players:
        if player.is_alive:
            alive_players.append(player)
    return alive_players


def main(players):
    round_ = 1
    while True:
        print('Остались в живых:')
        for player in get_alive_players(players):
            print('-', player.name)
        print(f'День {round_} начался')
        # day
        # каждому игроку даем возможность проголосовать
        for player in get_alive_players(players):
            player.day_move(players)

        print(f'Ночь {round_} началась')
        # night
        # каждому игроку надо дать походить ночью
        for player in get_alive_players(players):
            player.night_move(players)

        round_ += 1


players = [
    Player('Саша', CIVILIAN),
    Player('Катя', MAFIA),
    Player('Гоша', CIVILIAN),
    Player('Василий', SHERIFF)
]


main(players)
