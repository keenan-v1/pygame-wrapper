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

    while game.loop():
        for evt in event.get():
            print(evt)


if __name__ == "__main__":
    main()
