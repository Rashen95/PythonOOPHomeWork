def bot_turn(subtrahend):
    return f"\nБот взял {subtrahend} конфет"


def player_win(player_name):
    return f"\n{player_name} стал победителем"


def get_selection_of_sweets(number_of_candies):
    return f"Осталось {number_of_candies} конфет. Сколько возьмете?"


def player_turn(player_name):
    return f"\n{player_name}, ход за вами"


class UiInterfaceMess:
    __greetings = "\nВы запустили игру в конфетки"
    __regulations = "Перед вами лежит 200 конфет. За один ход можно брать от 1 до 28 конфет. " \
                    "Побеждает тот, кто возьмет последние конфеты"
    __errorDigit = "\nВы ввели не число"
    __errorSweetsNumber = "\nВы ввели неверное количество\nМожно взять от 1 до 28 конфет"
    __errorRemainingSweets = "\nВы хотите взять больше конфет чем осталось"
    __mainMenuWithSave = "\n1. Играть с ботом\n2. Играть с другом\n3. Загрузить прошлую игру\n4. Выйти из игры"
    __mainMenuWithOutSave = "\n1. Играть с ботом\n2. Играть с другом\n3. Выйти из игры"
    __errorItemMissing = "\nНет такого пункта меню"
    __firstNameSet = "\nВведите имя первого игрока"
    __secondNameSet = "\nВведите имя второго игрока"
    __exitGame = "\nЗавершаю работу игры"

    def get_greetings(self):
        return self.__greetings

    def get_regulations(self):
        return self.__regulations

    def get_error_digit(self):
        return self.__errorDigit

    def get_error_sweets_number(self):
        return self.__errorSweetsNumber

    def get_error_remaining_sweets(self):
        return self.__errorRemainingSweets

    def get_main_menu_with_save(self):
        return self.__mainMenuWithSave

    def get_main_menu_with_out_save(self):
        return self.__mainMenuWithOutSave

    def get_error_item_missing(self):
        return self.__errorItemMissing

    def get_first_name_set(self):
        return self.__firstNameSet

    def get_second_name_set(self):
        return self.__secondNameSet

    def get_exit_game(self):
        return self.__exitGame
