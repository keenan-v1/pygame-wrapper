#!/usr/bin/env python3

# Note: If you've pip installed the pygame_wrapper package, you do not need a try/except.
from collections.abc import Callable
import random

try:
    from pygame_wrapper import Game, event, keys
except ImportError:
    import sys
    sys.path.append("..")
    from pygame_wrapper import Game, event, keys


def change_bg(game: Game) -> Callable[[keys.KeyEvent], None]:
    def f(_: keys.KeyEvent) -> None:
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        game.background_color = random_color
    return f


def main() -> None:
    game = Game()
    game.map_key(keys.KEY_F2, change_bg(game))
    game.map_key(keys.KEY_F3, change_bg(game), trigger_on_hold=True)

    while game.loop():
        pass


if __name__ == "__main__":
    main()
