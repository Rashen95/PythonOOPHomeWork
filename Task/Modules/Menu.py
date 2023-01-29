from Modules import UiInterfaseMess as Ui
from Modules import SaveChecker as Sc
from Modules import UserInput
from Modules import GameMode as Gm
from Modules import SaveReader as Sr


def start_menu():
    UIn = Ui.UiInterfaceMess()
    print(UIn.get_greetings())
    print(UIn.get_regulations())
    main_menu()


def main_menu(flag=False):
    UIn = Ui.UiInterfaceMess()
    if Sc.check():
        while not flag:
            print(UIn.get_main_menu_with_save())
            change = UserInput.input_()
            if change == "1":
                flag = True
                Gm.with_bot()
            elif change == "2":
                flag = True
                Gm.with_friend()
            elif change == "3":
                flag = True
                Sr.read()
            elif change == "4":
                flag = True
                print(UIn.get_exit_game())
            else:
                print(UIn.get_error_item_missing())
    else:
        while not flag:
            print(UIn.get_main_menu_with_out_save())
            change = UserInput.input_()
            if change == "1":
                flag = True
                Gm.with_bot()
            elif change == "2":
                flag = True
                Gm.with_friend()
            elif change == "3":
                flag = True
                print(UIn.get_exit_game())
            else:
                print(UIn.get_error_item_missing())
