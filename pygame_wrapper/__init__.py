from collections import Callable
from typing import Union, Optional

import pygame
import pygame_gui
from pygame_gui import PackageResource

from . import color, event


class Game:
    def __init__(self, screen_width: int = 640, screen_height: int = 480, title: str = "My Game",
                 icon: Optional[str] = None, sound: bool = False, fps: int = 30, screen_flags: int = 0,
                 gui: bool = False, theme_path: Union[str, PackageResource, None] = None) -> None:
        self.fps = fps
        pygame.init()
        self.title = title
        self.screen_flags = screen_flags
        self.screen = pygame.display.set_mode((screen_width, screen_height), self.screen_flags)
        pygame.display.set_caption(title)
        if icon is not None:
            pygame.display.set_icon(pygame.image.load(icon))
        if sound:
            pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen.fill(color.BLACK)
        self.manager: Optional[pygame_gui.UIManager] = None
        if gui:
            self.manager = pygame_gui.UIManager((screen_width, screen_height), theme_path=theme_path)
        self.listeners: dict[int, list[Callable[[event.Event], None]]] = {}
        self.gui_listeners: dict[Union[int, str], list[Callable[[event.Event], None]]] = {}
        self.drawers: list[Callable[None]] = []

    def listen(self, event_types: Union[int, list[int]], f: Callable[[event.Event], None]):
        if type(event_types) is not list:
            event_types = [event_types]
        for event_type in event_types:
            if event_type not in self.listeners:
                self.listeners[event_type] = []
            if f not in self.listeners[event_type]:
                self.listeners[event_type].append(f)

    def listen_gui(self, user_event_type: any, f: Callable[[event.Event], None]):
        if user_event_type not in self.gui_listeners:
            self.gui_listeners[user_event_type] = []
        if f not in self.gui_listeners[user_event_type]:
            self.gui_listeners[user_event_type].append(f)

    def on_draw(self, f: Callable[None]):
        if f not in self.drawers:
            self.drawers.append(f)

    def loop(self) -> bool:
        time_delta = self.clock.tick(self.fps) / 1000.0
        if pygame.event.peek(eventtype=pygame.QUIT):
            return False
        if len(self.listeners) != 0:
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    return False
                event_type = evt.type
                if evt.type == pygame.USEREVENT and evt.user_type in self.gui_listeners:
                    for listener in self.gui_listeners[evt.user_type]:
                        listener(evt)
                elif event_type in self.listeners:
                    for listener in self.listeners[event_type]:
                        listener(evt)
                if self.manager is not None:
                    self.manager.process_events(evt)
        for drawer in self.drawers:
            drawer()
        if self.manager is not None:
            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)
        pygame.display.update()
        return True

    def print(self, font_name: str, sz_pt: int, text: str, text_color: tuple[int, int, int], point: tuple[int, int],
              antialias: bool = True) -> None:
        pygame.init()
        font = pygame.font.SysFont(font_name, sz_pt)
        line = font.render(text, antialias, text_color)
        self.screen.blit(line, point)

    def resize(self, size: tuple[int, int]):
        self.screen = pygame.display.set_mode(size, self.screen_flags)
        pygame.display.set_caption(self.title)
        if self.manager is not None:
            self.manager = pygame_gui.UIManager(size)
