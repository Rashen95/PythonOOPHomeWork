def write(first_player, second_player, move, number_of_candies):
    with open("save.txt", "w", encoding="utf8") as save_file:
        save_file.write(f"{first_player} {second_player} {move} {number_of_candies}")
