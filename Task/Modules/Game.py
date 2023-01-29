from Modules import UiInterfaseMess as Ui
from Modules import SelectionOfSweets as Sos
from Modules import SaveWritter as Sw
from Modules import Bot
import os


def game(first_player, second_player, move, number_of_candies):
    while number_of_candies > 0:
        if move == 1:
            print(Ui.player_turn(first_player))
            number_of_candies = Sos.sel(number_of_candies)
            move = 2
            Sw.write(first_player, second_player, move, number_of_candies)
        else:
            if second_player != "Бот":
                print(Ui.player_turn(second_player))
                number_of_candies = Sos.sel(number_of_candies)
            else:
                number_of_candies = Bot.selection_of_sweets(number_of_candies)
            move = 1
            Sw.write(first_player, second_player, move, number_of_candies)
    if move == 1:
        print(Ui.player_win(second_player))
    else:
        print(Ui.player_win(first_player))
    os.remove("save.txt")
