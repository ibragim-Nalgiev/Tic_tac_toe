from utils import *


def main():
    print("Добро пожаловать в игру 'Крестики-нолики'!")
    count_players = int(input("Хотите поиграть с компьютером или с другим игроком? "
                              "Нажмите 1: для выбора компьютера, 2: - для игры с другим человеком: "))
    field = create_field()
    if count_players == 1:
        print("Вы будете играть с компьютером!")
        player_sigh = int(input("Выберете, пожалуйста, знак: 1 - крестик, 2 - нолик: "))
        if player_sigh == 1:
            computer_sign = 2
        else:
            computer_sign = 1
        while True:
            show(field)
            choice_game_field(count_players)(field, player_sigh, computer_sign)
            win_status = update_current_game(field)
            if win_status == 0:
                continue
            elif win_status == player_sigh:
                show(field)
                print("Поздравляю, вы выиграли!")
                break
            elif win_status == 3:
                show(field)
                print("Вы сыграли в ничью!")
                break
            else:
                show(field)
                print("Главное не победа, а участие. Не расстраивайтесь, повезет в следующий раз")
                break
    else:
        print("Вы выбрали играть с другим игроком")
        print("Как у первого игрока ваш знак крестик, а у второго игрока нолик. ")
        while True:
            show(field)
            choice_game_field(count_players)(field)
            win_status = update_current_game(field)
            if win_status == 0:
                continue
            elif win_status == 1:
                show(field)
                print("Поздравляю Игрок1, вы выиграли!")
                break
            elif win_status == 2:
                show(field)
                print("Поздравляю Игрок2, вы выиграли!")
                break
            elif win_status == 3:
                show(field)
                print("Побебила дружба, вы сыграли в ничью!")
                break


if __name__ == '__main__':
    main()

