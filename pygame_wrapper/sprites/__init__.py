from typing import Tuple, Optional, Union, List

import pygame


class Sheet:
    def __init__(self, file_name: str) -> None:
        """Sheet represents a sprite sheet.

        Keyword arguments:
            file_name -- the name of the file containing the sprites.
        """
        try:
            self._sheet = pygame.image.load(file_name).convert()
        except pygame.error as e:
            print(f"Unable to load sprite sheet image: {file_name}")
            raise e

    def sprite_at(self, rectangle: Union[Tuple[int, int, int, int], pygame.rect.Rect],
                  color_key: Optional[Union[Tuple[int, int, int, int], int]] = None) -> pygame.Surface:
        """Returns a specific sprite from a rectangle.

        Keyword arguments:
            rectangle -- Either a tuple[int,int,int,int] or a pygame.rect.Rect. It is the area to load from the sheet.
            color_key -- Sets the color keys for the image (the color which represents transparency). Default: none
                      -- Note: a color_key value of -1 pulls the color_key from the top left of the image.
        """
        if type(rectangle) is not pygame.rect.Rect:
            rectangle = pygame.rect.Rect(rectangle)
        image = pygame.Surface(rectangle.size).convert()
        image.blit(self._sheet, (0, 0), rectangle)
        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key, pygame.RLEACCEL)
        return image

    def sprites_at(self, rectangles: List[Union[Tuple[int, int, int, int], pygame.rect.Rect]],
                   color_key: Optional[Union[Tuple[int, int, int, int], int]] = None) -> List[pygame.Surface]:
        """Loads multiple sprites from the given rectangles.

        Keyword arguments:
            rectangles -- Either a tuple[int,int,int,int] or a pygame.rect.Rect. It is the area to load from the sheet.
            color_key -- Sets the color keys for the image (the color which represents transparency). Default: none
                      -- Note: a color_key value of -1 pulls the color_key from the top left of the image.
        """
        return [self.sprite_at(rectangle, color_key) for rectangle in rectangles]

    def get_strip(self, rectangle: Tuple[int, int, int, int], image_count: int,
                  color_key: Optional[Union[Tuple[int, int, int, int], int]] = None) -> List[pygame.Surface]:
        """Loads a strip of sprites contained in the rectangle area provided.

        Keyword arguments:
            rectangle -- A tuple containing the points of the rectangle.
            image_count -- The number of images to expect in the strip.
            color_key -- Sets the color keys for the image (the color which represents transparency). Default: none
                      -- Note: a color_key value of -1 pulls the color_key from the top left of the image.
        """
        rectangles = [(rectangle[0]+rectangle[2]*x, rectangle[1], rectangle[2], rectangle[3])
                      for x in range(image_count)]
        return self.sprites_at(rectangles, color_key)

    def color_at(self, x: int, y: int) -> Tuple[int, int, int, int]:
        """Returns the color at a specific point on the sprite sheet."""
        return self._sheet.get_at((x, y))

    def size(self) -> Tuple[int, int]:
        return self._sheet.get_size()

    def slice_sheet(self, rows: int, cols: int, margin: Union[Tuple[int, int], int] = 0,
                    padding: Union[Tuple[int, int], int] = 0,
                    color_key: Optional[Union[Tuple[int, int, int, int], int]] = None) -> List[pygame.Surface]:
        """Slices a sprite sheet based upon the arguments provided.

        Keyword arguments:
            rows -- number of rows to slice the sheet into.
            cols -- number of columns to slice the sheet into.
            margin -- either a tuple[x,y] of margin, or an integer to use for both.
            padding -- either a tuple[x,y] of padding, or an integer to use for both.
            color_key -- Sets the color keys for the image (the color which represents transparency). Default: none
                      -- Note: a color_key value of -1 pulls the color_key from the top left of the image.
        """
        margin_x = margin[0] if type(margin) == tuple else margin
        margin_y = margin[1] if type(margin) == tuple else margin
        padding_x = padding[0] if type(padding) == tuple else padding
        padding_y = padding[1] if type(padding) == tuple else padding

        w, h = self._sheet.get_rect().size
        size_x = (w - 2 * margin_x - (cols - 1) * padding_x) / cols
        size_y = (h - 2 * margin_y - (rows - 1) * padding_y) / rows

        rectangles = []
        for row in range(rows):
            for col in range(cols):
                x = margin_x + col * (size_x + padding_x)
                y = margin_y + row * (size_y + padding_y)
                rectangles.append((x, y, size_x, size_y))

        return self.sprites_at(rectangles, color_key)
