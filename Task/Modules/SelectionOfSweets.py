from Modules import UiInterfaseMess as Ui
from Modules import UserInput


def sel(number_of_candies, flag=False):
    UIn = Ui.UiInterfaceMess()
    while not flag:
        print(Ui.get_selection_of_sweets(number_of_candies))
        number = UserInput.input_()
        if number.isdigit():
            number = int(number)
            if 0 < number < 29:
                if number <= number_of_candies:
                    flag = True
                    number_of_candies = number_of_candies - number
                else:
                    print(UIn.get_error_remaining_sweets())
            else:
                print(UIn.get_error_sweets_number())
        else:
            print(UIn.get_error_digit())
    return number_of_candies
