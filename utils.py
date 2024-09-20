import random
from typing import Any


def create_field(size: int = 3) -> list[list[Any]]:
    """
    Функция для создания игрового поля
    """
    lst = [['#' for _ in range(size)] for _ in range(size)]
    return lst


def show(field: list[list[Any]]) -> None:
    """
    Функция выводит в консоль текущее состояние игрового поля
    """
    for row in field:
        print(*map(lambda x: 'x' if x == 1 else '0' if x == 2 else '#', row))


def update_current_game(field: list[list[Any]], win_status: int = 0) -> int:
    """
    Данная функция обновляет текущий статус игры
    win_status = 0: игра еще не окончена
    win_status = 1: победил игрок, играющий крестиками
    win_status = 2: ничья
    """
    for i in range(len(field)):
        if field[i][0] == 1 and field[i][1] == 1 and field[i][2] == 1 or \
                field[0][i] == 1 and field[1][i] == 1 and field[2][i] == 1:
            win_status = 1
        if field[i][0] == 2 and field[i][1] == 2 and field[i][2] == 2 or \
                field[0][i] == 2 and field[1][i] == 2 and field[2][i] == 2:
            win_status = 2

        if field[0][0] == 1 and field[1][1] == 1 and field[2][2] == 1 or \
                field[0][-1] == 1 and field[1][-2] == 1 and field[2][-3] == 1:
            win_status = 1
        if field[0][0] == 2 and field[1][1] == 2 and field[2][2] == 2 or \
                field[0][-1] == 2 and field[1][-2] == 2 and field[2][-3] == 2:
            win_status = 2

    if not any((i == '#' for i in row) for row in field):
        win_status = 3
    return win_status


def game_with_computers(field: list[list[Any]], player_sigh: int, computer_sigh: int) -> list[list[Any]]:
    """
    Закладывает основной функционал. По очереди ходят игром и затем компьютер
    """
    while True:
        step = tuple(
            map(int, input("Выберите координаты(два числа от 0 до 2), куда будет поставлен ваш символ: ").split()))
        r, c = step
        if field[r][c] != '#':
            print("Это клетка уже занята")
            continue
        if field[r][c] == '#':
            field[r][c] = player_sigh
            break

    while True:
        r = random.randint(0, 2)
        c = random.randint(0, 2)
        if field[r][c] == '#':
            field[r][c] = computer_sigh
            break
    return field


def step_first_player(field: list[list[Any]], player1_sigh: int = 1) -> None:
    """
    Для хода первого игрока.
    """
    while True:
        step1 = tuple(map(int, input(
            "Игрок1: выберите координаты(два числа от 0 до 2), куда будет поставлен ваш символ: ").split()))
        r, c = step1
        if field[r][c] != '#':
            print("Это клетка уже занята")
            continue
        if field[r][c] == '#':
            field[r][c] = player1_sigh
            break


def step_second_player(field: list[list[Any]], player2_sigh: int = 2) -> None:
    """
    Для хода второго игрока.
    """
    while True:
        step2 = tuple(map(int, input(
            "Игрок2: выберите координаты(два числа от 0 до 2), куда будет поставлен ваш символ: ").split()))
        r, c = step2
        if field[r][c] != '#':
            print("Это клетка уже занята")
            continue
        if field[r][c] == '#':
            field[r][c] = player2_sigh
            break


def choice_game_field(count_players: int = 1):
    """
    Вспомогательная функция, позволяет выбрать играть с компьютером или с другим человеком.
    В зависимости от выбора игры, возвращается соответственная функция
    """
    if not type(count_players) == int or count_players not in (1, 2):
        raise ValueError("Можно выбрать только 1 или 2")

    if count_players == 1:
        return game_with_computers
