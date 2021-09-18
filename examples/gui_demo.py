#!/usr/bin/env python3

# Note: If you've pip installed the pygame_wrapper package, you do not need a try/except.
import collections
from typing import Optional

try:
    from pygame_wrapper import Game, event, color, gui, pygame
except ImportError:
    import sys
    sys.path.append("..")
    from pygame_wrapper import Game, event, color, gui, pygame


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

        self.listen(event.KEYDOWN, self.on_keydown())
        self.listen_gui(event.UI_WINDOW_CLOSE, lambda evt: self.clear_window())
        self.on_draw(lambda: self.screen.fill(color.BLACK))
        self.window: Optional[gui.UIManager] = None

    def on_keydown(self) -> collections.Callable[[event.Event], None]:
        def handler(evt: event.Event) -> None:
            if evt.key == pygame.K_F1 and self.window is None:
                self.window = DemoWindow(self.manager)
        return handler

    def clear_window(self):
        self.window = None

    def run(self):
        while self.loop():
            pass


if __name__ == "__main__":
    game = DemoApp()
    game.run()
