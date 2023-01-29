from Modules import UiInterfaseMess


def selection_of_sweets(number_of_candies):
    if number_of_candies > 28 and number_of_candies % 29 > 0:
        subtrahend = number_of_candies % 29
        number_of_candies -= subtrahend
        print(UiInterfaseMess.bot_turn(subtrahend))
    elif number_of_candies > 28:
        number_of_candies -= 1
        print(UiInterfaseMess.bot_turn(1))
    else:
        print(UiInterfaseMess.bot_turn(number_of_candies))
        number_of_candies -= number_of_candies
    return number_of_candies
