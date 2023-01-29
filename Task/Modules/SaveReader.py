from Modules import Game


def read():
    with open("save.txt", "r", encoding="utf8") as save_file:
        save = save_file.read().split(" ")
    Game.game(save[0], save[1], int(save[2]), int(save[3]))
