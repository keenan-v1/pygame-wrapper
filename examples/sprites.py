#!/usr/bin/env python3

# Note: If you've pip installed the pygame_wrapper package, you do not need a try/except.
import pygame

try:
    from pygame_wrapper import Game, event, color, sprites, keys
except ImportError:
    import sys
    sys.path.append("..")
    from pygame_wrapper import Game, event, color, sprites, keys


class App(Game):
    def __init__(self):
        super().__init__(title="Sprite Demo", screen_width=800, screen_height=600, background_color=(128, 128, 128))
        self.sprite_sheet = sprites.Sheet("data/sprites.png")
        xy = (self.sprite_sheet.size()[0]-1, 0)
        self.sprite_list = self.sprite_sheet.slice_sheet(3, 4, 4, 8, self.sprite_sheet.color_at(*xy))
        self.max_cols = 2

    def scale_up(self):
        for i in range(len(self.sprite_list)):
            new_sprite = pygame.Surface((self.sprite_list[i].get_size()[0]*2, self.sprite_list[i].get_size()[1]*2))
            new_sprite.set_colorkey(self.sprite_list[i].get_colorkey())
            pygame.transform.scale(self.sprite_list[i], new_sprite.get_size(), new_sprite)
            self.sprite_list[i] = new_sprite

    def scale_down(self):
        for i in range(len(self.sprite_list)):
            new_sprite = pygame.Surface((self.sprite_list[i].get_size()[0]/2, self.sprite_list[i].get_size()[1]/2))
            new_sprite.set_colorkey(self.sprite_list[i].get_colorkey())
            pygame.transform.scale(self.sprite_list[i], new_sprite.get_size(), new_sprite)
            self.sprite_list[i] = new_sprite

    def draw(self):
        next_sprite_x = 10
        next_sprite_y = 10
        cols = 0
        for sprite in self.sprite_list:
            self.screen.blit(sprite, (next_sprite_x, next_sprite_y))
            next_sprite_x += sprite.get_size()[0] + 10
            cols += 1
            if cols > 2:
                cols = 0
                next_sprite_x = 10
                next_sprite_y += sprite.get_size()[1] + 10


def main() -> None:
    game = App()

    game.map_key(keys.KEY_EQUALS, lambda _: game.scale_up())
    game.map_key(keys.KEY_MINUS, lambda _: game.scale_down())
    game.on_draw(game.draw)

    while game.loop():
        pass


if __name__ == "__main__":
    main()
