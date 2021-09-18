from collections import Callable
from enum import Enum
from typing import Union, Optional

import pygame
import pygame_gui
from pygame_gui import PackageResource

from . import event, keys, color


class Game:
    def __init__(self, screen_width: int = 640, screen_height: int = 480, title: str = "My Game",
                 icon: Optional[str] = None, sound: bool = False, fps: int = 30, screen_flags: int = 0,
                 gui: bool = False, theme_path: Union[str, PackageResource, None] = None,
                 background_color: tuple[int, int, int] = color.BLACK) -> None:
        self.fps = fps
        pygame.init()
        self.title = title
        self.screen_flags = screen_flags
        self.screen = pygame.display.set_mode((screen_width, screen_height), self.screen_flags)
        self.background_color = background_color
        pygame.display.set_caption(title)
        if icon is not None:
            pygame.display.set_icon(pygame.image.load(icon))
        if sound:
            pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen.fill(self.background_color)
        self.manager: Optional[pygame_gui.UIManager] = None
        if gui:
            self.manager = pygame_gui.UIManager((screen_width, screen_height), theme_path=theme_path)
        self.listeners: dict[int, list[Callable[[event.Event], None]]] = {}
        self.gui_listeners: dict[Union[int, str], list[Callable[[event.Event], None]]] = {}
        self.drawers: list[Callable[None]] = []
        self.key_map: dict[keys.Key, list[keys.KeyMap]] = {}

    def map_key(self, key: keys.Key, f: Callable[[keys.KeyEvent], None], trigger_on_hold: bool = False) -> None:
        if key not in self.key_map:
            self.key_map[key] = []
        self.key_map[key].append(keys.KeyMap(key, f, trigger_on_hold=trigger_on_hold))

    def unmap_key(self, key: keys.Key, f: Callable[[keys.KeyEvent], None]) -> None:
        for km in self.key_map[key]:
            if km.func == f:
                self.key_map[key].remove(km)

    def listen(self, event_types: Union[int, list[int]], f: Callable[[event.Event], None]) -> None:
        if type(event_types) is not list:
            event_types = [event_types]
        for event_type in event_types:
            if event_type not in self.listeners:
                self.listeners[event_type] = []
            if f not in self.listeners[event_type]:
                self.listeners[event_type].append(f)

    def stop_listening(self, event_type: int, f: Callable[[event.Event], None]) -> None:
        if event_type in self.listeners and f in self.listeners[event_type]:
            self.listeners[event_type].remove(f)

    def listen_gui(self, user_event_type: any, f: Callable[[event.Event], None]) -> None:
        if user_event_type not in self.gui_listeners:
            self.gui_listeners[user_event_type] = []
        if f not in self.gui_listeners[user_event_type]:
            self.gui_listeners[user_event_type].append(f)

    def stop_listening_gui(self, user_event_type: any, f: Callable[[event.Event], None]) -> None:
        if user_event_type in self.gui_listeners and f in self.gui_listeners[user_event_type]:
            self.gui_listeners[user_event_type].remove(f)

    def on_draw(self, f: Callable[None]) -> None:
        if f not in self.drawers:
            self.drawers.append(f)

    def _handle_listeners(self) -> None:
        if len(self.listeners) > 0 or len(self.gui_listeners) > 0:
            for evt in pygame.event.get():
                if evt.type == pygame.USEREVENT and evt.user_type in self.gui_listeners:
                    for listener in self.gui_listeners[evt.user_type]:
                        listener(evt)
                elif evt.type in self.listeners:
                    for listener in self.listeners[evt.type]:
                        listener(evt)
                if self.manager is not None:
                    self.manager.process_events(evt)

    def _handle_keymap(self) -> None:
        for key, key_maps in self.key_map.items():
            if pygame.key.get_pressed()[key.code]:
                for km in key_maps:
                    if not key.is_held or km.trigger_on_hold:
                        key.is_held = True
                        km.func(keys.KeyEvent(key, pygame.key.get_mods()))
            elif key.is_held:
                key.is_held = False

    def loop(self) -> bool:
        time_delta = self.clock.tick(self.fps) / 1000.0
        if pygame.event.peek(eventtype=pygame.QUIT):
            return False
        self.screen.fill(self.background_color)
        self._handle_listeners()
        self._handle_keymap()
        for drawer in self.drawers:
            drawer()
        if self.manager is not None:
            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)
        pygame.display.update()
        return True

    def print(self, font_name: str, sz_pt: int, text: str, text_color: tuple[int, int, int],
              point: tuple[int, int], antialias: bool = True) -> None:
        pygame.init()
        font = pygame.font.SysFont(font_name, sz_pt)
        line = font.render(text, antialias, text_color)
        self.screen.blit(line, point)

    def resize(self, size: tuple[int, int]):
        self.screen = pygame.display.set_mode(size, self.screen_flags)
        pygame.display.set_caption(self.title)
        if self.manager is not None:
            self.manager = pygame_gui.UIManager(size)
