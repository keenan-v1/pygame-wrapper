from collections import Callable

import pygame

from . import color, event


class Game:
    def __init__(self, screen_width: int = 640, screen_height: int = 480, title: str = "My Game", icon: str = None,
                 sound: bool = False, fps: int = 30, resizeable: bool = False) -> None:
        self.fps = fps
        pygame.init()
        self.resizeable = resizeable
        self.title = title
        self.screen_flags = pygame.RESIZABLE if resizeable else 0
        self.screen = pygame.display.set_mode((screen_width, screen_height), self.screen_flags)
        pygame.display.set_caption(title)
        if icon is not None:
            pygame.display.set_icon(pygame.image.load(icon))
        if sound:
            pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen.fill(color.BLACK)
        self.listeners: dict[int, list[Callable[[event.Event], None]]] = {}

    def listen(self, event_type: int, f: Callable[[event.Event], None]):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        if f not in self.listeners[event_type]:
            self.listeners[event_type].append(f)

    def loop(self) -> bool:
        pygame.display.update()
        self.clock.tick(self.fps)
        if pygame.event.peek(eventtype=pygame.QUIT):
            return False
        if len(self.listeners) != 0:
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    return False
                if evt.type in self.listeners:
                    for listener in self.listeners[evt.type]:
                        listener(evt)
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

    @staticmethod
    def events(event_type: int = None) -> list[pygame.event.Event]:
        return pygame.event.get(eventtype=event_type)
