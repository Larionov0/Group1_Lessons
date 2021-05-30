MAFIA = 'мафиозник'
CIVILIAN = 'мирный'
SHERIFF = 'шериф'
DOCTOR = 'доктор'


def input_int(text):
    while True:
        ans = input(text)
        if ans.isdigit():
            return int(ans)
        else:
            print('Надо бы число!')


class Player:
    def __init__(self, name, role, is_alive=True):
        self.name = name
        self.role = role
        self.is_alive = is_alive
        self.is_killed_now = False

    def day_move(self, players):
        alive_players = get_alive_players(players)
        i = 1
        for player in alive_players:
            print(f"{i} - {player.name}")
            i += 1
        index = input_int(f'Дневной голос для {self.name}: ') - 1
        player = alive_players[index]

    def night_move(self, players):
        input(f'Ночной ход для {self.name}')
        if self.role == MAFIA:
            self.mafia_night_menu(players)
        elif self.role == CIVILIAN:
            self.civilian_night_menu()
        elif self.role == SHERIFF:
            self.sheriff_night_menu(players)
        elif self.role == DOCTOR:
            self.doctor_night_menu(players)
        input('Конец хода')

    def mafia_night_menu(self, players):
        alive_players = get_alive_players(players)
        i = 1
        for player in alive_players:
            print(f"{i} - {player.name}")
            i += 1
        index = input_int('Кого вы выбираете: ') - 1
        player = alive_players[index]
        if player is not self:
            player.is_killed_now = True
            print(f'Удачно извлечен {player.name}')
        else:
            print('Самоубийца - это не ваша роль')

    def civilian_night_menu(self):
        print('Вы спите:)')

    def sheriff_night_menu(self, players):
        alive_players = get_alive_players(players)
        i = 1
        for player in alive_players:
            print(f"{i} - {player.name}")
            i += 1
        index = input_int('Кого вы выбираете: ') - 1
        player = alive_players[index]
        if player is not self:
            player.name += '_sus'
            print(f'вы подозриваете {player.name}')
        else:
            print('ты шериф!!! ты не можеш быть мафией')

    def doctor_night_menu(self, players):
        alive_players = get_alive_players(players)
        i = 1
        for player in alive_players:
            print(f"{i} - {player.name}")
            i += 1
        index = input_int('Кого вы выбираете: ') - 1
        player = alive_players[index]
        if player is not self:
            print(f'Удачно выличен {player.name}')
        else:
            print('Ты серйозно? ну ладно. ну типа')
        player.is_killed_now = False


def get_alive_players(players):
    alive_players = []
    for player in players:
        if player.is_alive:
            alive_players.append(player)
    return alive_players


def no4naia_proverka(players):
    for player in players:
        if player.is_killed_now == True:
            print('Выбыл из игры: ', player.name)
            player.is_alive = False


def main(players):
    round_ = 1
    while True:
        print('Остались в живых:')
        for player in get_alive_players(players):
            print('-', player.name)
        print(f'День {round_} начался')
        for player in get_alive_players(players):
            player.day_move(players)

        print(f'Ночь {round_} началась')
        for player in get_alive_players(players):
            player.night_move(players)

        no4naia_proverka(players)

        round_ += 1


players = [
    Player('Саша', CIVILIAN),
    Player('Катя', MAFIA),
    Player('Гоша', CIVILIAN),
    Player('Василий', SHERIFF),
    Player('Жора', DOCTOR)
]

main(players)