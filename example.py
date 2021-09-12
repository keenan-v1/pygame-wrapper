#!/usr/bin/env python3
from game import Game
from game import color
import pygame


def game_logic(game: Game, pressed: list[str]) -> None:
    keys = "".join(pressed)
    if keys != "":
        game.screen.fill(color.GREEN)
        game.print("monospace", 35, keys, color.WHITE, (10, 10))


def main() -> None:
    game = Game()

    keys_held: list[str] = []

    def on_keyup(evt: pygame):
        keys_held.remove(evt.unicode)
        if len(keys_held) == 0:
            game.screen.fill(color.BLACK)

    game.listen(pygame.KEYUP, on_keyup)
    game.listen(pygame.KEYDOWN, lambda evt: keys_held.append(evt.unicode))
    while game.loop():
        game_logic(game, list(dict.fromkeys(keys_held)))


if __name__ == "__main__":
    main()
