#!/usr/bin/env python3

# Note: If you've pip installed the pygame_wrapper package, you do not need a try/except.
try:
    from pygame_wrapper import Game, event, color
except ImportError:
    import sys
    sys.path.append("..")
    from pygame_wrapper import Game, event, color


def main() -> None:
    game = Game()
    keys_held: list[str] = []

    def on_keyup(evt: event.Event):
        keys_held.remove(evt.unicode)
        if len(keys_held) == 0:
            game.screen.fill(color.BLACK)

    game.listen(event.KEYUP, on_keyup)
    game.listen(event.KEYDOWN, lambda evt: keys_held.append(evt.unicode))

    def draw():
        keys = "".join(list(dict.fromkeys(keys_held)))
        if keys != "":
            game.screen.fill(color.GREEN)
            game.print("monospace", 35, keys, color.BLACK, (10, 10))
    game.on_draw(draw)

    while game.loop():
        pass

if __name__ == "__main__":
    main()
