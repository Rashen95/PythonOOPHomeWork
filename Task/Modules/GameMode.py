from Modules import UiInterfaseMess as Ui
from Modules import UserInput
import random
from Modules import SaveWritter as Sw
from Modules import Game


def with_bot():
    UIn = Ui.UiInterfaceMess()
    print(UIn.get_first_name_set())
    first_player = UserInput.input_()
    move = random.randint(1, 3)
    Sw.write(first_player, "Бот", move, 200)
    Game.game(first_player, "Бот", move, 200)


def with_friend():
    UIn = Ui.UiInterfaceMess()
    print(UIn.get_first_name_set())
    first_player = UserInput.input_()
    print(UIn.get_second_name_set())
    second_player = UserInput.input_()
    move = random.randint(1, 3)
    Sw.write(first_player, second_player, move, 200)
    Game.game(first_player, second_player, move, 200)
