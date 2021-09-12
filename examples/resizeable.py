#!/usr/bin/env python3

# Note: If you've pip installed the pygame_wrapper package, you do not need a try/except.
from collections import Callable

try:
    from pygame_wrapper import Game, event, color
except ImportError:
    import sys
    sys.path.append("..")
    from pygame_wrapper import Game, event, color


def on_resize(game: Game) -> Callable[[event.Event], None]:
    def resize(evt: event.Event) -> None:
        game.resize((evt.w, evt.h))
        game.screen.fill(color.BLACK)
    return resize


def main() -> None:
    game = Game(title="Resizeable Demo", resizeable=True)
    keys_held: list[str] = []

    def on_keyup(evt: event.Event):
        keys_held.remove(evt.unicode)
        if len(keys_held) == 0:
            game.screen.fill(color.BLACK)

    game.listen(event.VIDEORESIZE, on_resize(game))
    game.listen(event.KEYUP, on_keyup)
    game.listen(event.KEYDOWN, lambda evt: keys_held.append(evt.unicode))

    while game.loop():
        keys = "".join(list(dict.fromkeys(keys_held)))
        if keys != "":
            game.screen.fill(color.GREEN)
            game.print("monospace", 35, keys, color.BLACK, (10, 10))


if __name__ == "__main__":
    main()
