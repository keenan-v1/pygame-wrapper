#!/usr/bin/env python3

# Note: If you've pip installed the pygame_wrapper package, you do not need a try/except.
import collections
from typing import Optional

try:
    from pygame_wrapper import Game, event, color, gui, pygame, keys
except ImportError:
    import sys
    sys.path.append("..")
    from pygame_wrapper import Game, event, color, gui, pygame, keys


class DemoWindow(gui.elements.UIWindow):
    def __init__(self, manager):
        super().__init__(
            pygame.Rect((20, 50), (300, 200)),
            manager,
            window_display_title="Demo Window",
            object_id="#demo_window"
        )


class DemoApp(Game):
    def __init__(self):
        super().__init__(gui=True, title="GUI Demo", theme_path='./data/gui_demo_theme.json')

        self.map_key(keys.KEY_F1, lambda _: self.open_window())
        self.listen_gui(event.UI_WINDOW_CLOSE, lambda _: self.clear_window())
        self.window: Optional[gui.UIManager] = None

    def open_window(self) -> None:
        if self.window is None:
            self.window = DemoWindow(self.manager)

    def clear_window(self) -> None:
        self.window = None

    def run(self) -> None:
        while self.loop():
            pass


if __name__ == "__main__":
    game = DemoApp()
    game.run()
