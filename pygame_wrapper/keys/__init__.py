from collections import Callable

import pygame


class Key:
    def __init__(self, code: int, name: str) -> None:
        self.code = code
        self.name = name
        self.is_held = False


class KeyEvent:
    def __init__(self, key: Key, modifiers: int) -> None:
        self.key = key
        self.modifiers = modifiers


class KeyMap:
    def __init__(self, key: Key, func: Callable[[KeyEvent], None], trigger_on_hold: bool = False) -> None:
        """Creates a key mapping.

        Keyword Arguments:
            trigger_on_hold -- Trigger on the key being trigger_on_hold instead of just on press.
        """
        self.key = key
        self.trigger_on_hold = trigger_on_hold
        self.func = func


def get_key(code: int) -> Key:
    for item in globals():
        if not item.startswith("KEY_"):
            continue
        key: Key = globals()[item]
        if key.code == code:
            return key
    return KEY_UNKNOWN


KEY_0 = Key(pygame.K_0, '0')
KEY_1 = Key(pygame.K_1, '1')
KEY_2 = Key(pygame.K_2, '2')
KEY_3 = Key(pygame.K_3, '3')
KEY_4 = Key(pygame.K_4, '4')
KEY_5 = Key(pygame.K_5, '5')
KEY_6 = Key(pygame.K_6, '6')
KEY_7 = Key(pygame.K_7, '7')
KEY_8 = Key(pygame.K_8, '8')
KEY_9 = Key(pygame.K_9, '9')
KEY_AC_BACK = Key(pygame.K_AC_BACK, 'AC_BACK')
KEY_AMPERSAND = Key(pygame.K_AMPERSAND, 'AMPERSAND')
KEY_ASTERISK = Key(pygame.K_ASTERISK, 'ASTERISK')
KEY_AT = Key(pygame.K_AT, 'AT')
KEY_BACKQUOTE = Key(pygame.K_BACKQUOTE, 'BACKQUOTE')
KEY_BACKSLASH = Key(pygame.K_BACKSLASH, 'BACKSLASH')
KEY_BACKSPACE = Key(pygame.K_BACKSPACE, 'BACKSPACE')
KEY_BREAK = Key(pygame.K_BREAK, 'BREAK')
KEY_CAPSLOCK = Key(pygame.K_CAPSLOCK, 'CAPSLOCK')
KEY_CARET = Key(pygame.K_CARET, 'CARET')
KEY_CLEAR = Key(pygame.K_CLEAR, 'CLEAR')
KEY_COLON = Key(pygame.K_COLON, 'COLON')
KEY_COMMA = Key(pygame.K_COMMA, 'COMMA')
KEY_CURRENCYSUBUNIT = Key(pygame.K_CURRENCYSUBUNIT, 'CURRENCYSUBUNIT')
KEY_CURRENCYUNIT = Key(pygame.K_CURRENCYUNIT, 'CURRENCYUNIT')
KEY_DELETE = Key(pygame.K_DELETE, 'DELETE')
KEY_DOLLAR = Key(pygame.K_DOLLAR, 'DOLLAR')
KEY_DOWN = Key(pygame.K_DOWN, 'DOWN')
KEY_END = Key(pygame.K_END, 'END')
KEY_EQUALS = Key(pygame.K_EQUALS, 'EQUALS')
KEY_ESCAPE = Key(pygame.K_ESCAPE, 'ESCAPE')
KEY_EURO = Key(pygame.K_EURO, 'EURO')
KEY_EXCLAIM = Key(pygame.K_EXCLAIM, 'EXCLAIM')
KEY_F1 = Key(pygame.K_F1, 'F1')
KEY_F10 = Key(pygame.K_F10, 'F10')
KEY_F11 = Key(pygame.K_F11, 'F11')
KEY_F12 = Key(pygame.K_F12, 'F12')
KEY_F13 = Key(pygame.K_F13, 'F13')
KEY_F14 = Key(pygame.K_F14, 'F14')
KEY_F15 = Key(pygame.K_F15, 'F15')
KEY_F2 = Key(pygame.K_F2, 'F2')
KEY_F3 = Key(pygame.K_F3, 'F3')
KEY_F4 = Key(pygame.K_F4, 'F4')
KEY_F5 = Key(pygame.K_F5, 'F5')
KEY_F6 = Key(pygame.K_F6, 'F6')
KEY_F7 = Key(pygame.K_F7, 'F7')
KEY_F8 = Key(pygame.K_F8, 'F8')
KEY_F9 = Key(pygame.K_F9, 'F9')
KEY_GREATER = Key(pygame.K_GREATER, 'GREATER')
KEY_HASH = Key(pygame.K_HASH, 'HASH')
KEY_HELP = Key(pygame.K_HELP, 'HELP')
KEY_HOME = Key(pygame.K_HOME, 'HOME')
KEY_INSERT = Key(pygame.K_INSERT, 'INSERT')
KEY_KP_0 = Key(pygame.K_KP_0, 'KP_0')
KEY_KP_1 = Key(pygame.K_KP_1, 'KP_1')
KEY_KP_2 = Key(pygame.K_KP_2, 'KP_2')
KEY_KP_3 = Key(pygame.K_KP_3, 'KP_3')
KEY_KP_4 = Key(pygame.K_KP_4, 'KP_4')
KEY_KP_5 = Key(pygame.K_KP_5, 'KP_5')
KEY_KP_6 = Key(pygame.K_KP_6, 'KP_6')
KEY_KP_7 = Key(pygame.K_KP_7, 'KP_7')
KEY_KP_8 = Key(pygame.K_KP_8, 'KP_8')
KEY_KP_9 = Key(pygame.K_KP_9, 'KP_9')
KEY_KP_DIVIDE = Key(pygame.K_KP_DIVIDE, 'KP_DIVIDE')
KEY_KP_ENTER = Key(pygame.K_KP_ENTER, 'KP_ENTER')
KEY_KP_EQUALS = Key(pygame.K_KP_EQUALS, 'KP_EQUALS')
KEY_KP_MINUS = Key(pygame.K_KP_MINUS, 'KP_MINUS')
KEY_KP_MULTIPLY = Key(pygame.K_KP_MULTIPLY, 'KP_MULTIPLY')
KEY_KP_PERIOD = Key(pygame.K_KP_PERIOD, 'KP_PERIOD')
KEY_KP_PLUS = Key(pygame.K_KP_PLUS, 'KP_PLUS')
KEY_LALT = Key(pygame.K_LALT, 'LALT')
KEY_LCTRL = Key(pygame.K_LCTRL, 'LCTRL')
KEY_LEFT = Key(pygame.K_LEFT, 'LEFT')
KEY_LEFTBRACKET = Key(pygame.K_LEFTBRACKET, 'LEFTBRACKET')
KEY_LEFTPAREN = Key(pygame.K_LEFTPAREN, 'LEFTPAREN')
KEY_LESS = Key(pygame.K_LESS, 'LESS')
KEY_LGUI = Key(pygame.K_LGUI, 'LGUI')
KEY_LMETA = Key(pygame.K_LMETA, 'LMETA')
KEY_LSHIFT = Key(pygame.K_LSHIFT, 'LSHIFT')
KEY_LSUPER = Key(pygame.K_LSUPER, 'LSUPER')
KEY_MENU = Key(pygame.K_MENU, 'MENU')
KEY_MINUS = Key(pygame.K_MINUS, 'MINUS')
KEY_MODE = Key(pygame.K_MODE, 'MODE')
KEY_NUMLOCK = Key(pygame.K_NUMLOCK, 'NUMLOCK')
KEY_NUMLOCKCLEAR = Key(pygame.K_NUMLOCKCLEAR, 'NUMLOCKCLEAR')
KEY_PAGEDOWN = Key(pygame.K_PAGEDOWN, 'PAGEDOWN')
KEY_PAGEUP = Key(pygame.K_PAGEUP, 'PAGEUP')
KEY_PAUSE = Key(pygame.K_PAUSE, 'PAUSE')
KEY_PERCENT = Key(pygame.K_PERCENT, 'PERCENT')
KEY_PERIOD = Key(pygame.K_PERIOD, 'PERIOD')
KEY_PLUS = Key(pygame.K_PLUS, 'PLUS')
KEY_POWER = Key(pygame.K_POWER, 'POWER')
KEY_PRINT = Key(pygame.K_PRINT, 'PRINT')
KEY_PRINTSCREEN = Key(pygame.K_PRINTSCREEN, 'PRINTSCREEN')
KEY_QUESTION = Key(pygame.K_QUESTION, 'QUESTION')
KEY_QUOTE = Key(pygame.K_QUOTE, 'QUOTE')
KEY_QUOTEDBL = Key(pygame.K_QUOTEDBL, 'QUOTEDBL')
KEY_RALT = Key(pygame.K_RALT, 'RALT')
KEY_RCTRL = Key(pygame.K_RCTRL, 'RCTRL')
KEY_RETURN = Key(pygame.K_RETURN, 'RETURN')
KEY_RGUI = Key(pygame.K_RGUI, 'RGUI')
KEY_RIGHT = Key(pygame.K_RIGHT, 'RIGHT')
KEY_RIGHTBRACKET = Key(pygame.K_RIGHTBRACKET, 'RIGHTBRACKET')
KEY_RIGHTPAREN = Key(pygame.K_RIGHTPAREN, 'RIGHTPAREN')
KEY_RMETA = Key(pygame.K_RMETA, 'RMETA')
KEY_RSHIFT = Key(pygame.K_RSHIFT, 'RSHIFT')
KEY_RSUPER = Key(pygame.K_RSUPER, 'RSUPER')
KEY_SCROLLLOCK = Key(pygame.K_SCROLLLOCK, 'SCROLLLOCK')
KEY_SCROLLOCK = Key(pygame.K_SCROLLOCK, 'SCROLLOCK')
KEY_SEMICOLON = Key(pygame.K_SEMICOLON, 'SEMICOLON')
KEY_SLASH = Key(pygame.K_SLASH, 'SLASH')
KEY_SPACE = Key(pygame.K_SPACE, 'SPACE')
KEY_SYSREQ = Key(pygame.K_SYSREQ, 'SYSREQ')
KEY_TAB = Key(pygame.K_TAB, 'TAB')
KEY_UNDERSCORE = Key(pygame.K_UNDERSCORE, 'UNDERSCORE')
KEY_UNKNOWN = Key(pygame.K_UNKNOWN, 'UNKNOWN')
KEY_UP = Key(pygame.K_UP, 'UP')
KEY_A = Key(pygame.K_a, 'A')
KEY_B = Key(pygame.K_b, 'B')
KEY_C = Key(pygame.K_c, 'C')
KEY_D = Key(pygame.K_d, 'D')
KEY_E = Key(pygame.K_e, 'E')
KEY_F = Key(pygame.K_f, 'F')
KEY_G = Key(pygame.K_g, 'G')
KEY_H = Key(pygame.K_h, 'H')
KEY_I = Key(pygame.K_i, 'I')
KEY_J = Key(pygame.K_j, 'J')
KEY_K = Key(pygame.K_k, 'K')
KEY_L = Key(pygame.K_l, 'L')
KEY_M = Key(pygame.K_m, 'M')
KEY_N = Key(pygame.K_n, 'N')
KEY_O = Key(pygame.K_o, 'O')
KEY_P = Key(pygame.K_p, 'P')
KEY_Q = Key(pygame.K_q, 'Q')
KEY_R = Key(pygame.K_r, 'R')
KEY_S = Key(pygame.K_s, 'S')
KEY_T = Key(pygame.K_t, 'T')
KEY_U = Key(pygame.K_u, 'U')
KEY_V = Key(pygame.K_v, 'V')
KEY_W = Key(pygame.K_w, 'W')
KEY_X = Key(pygame.K_x, 'X')
KEY_Y = Key(pygame.K_y, 'Y')
KEY_Z = Key(pygame.K_z, 'Z')