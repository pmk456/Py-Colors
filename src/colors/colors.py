"""
Author: Patan Musthakheem
Licence: Apache 2.0
Version: 0.1
"""
import os
import sys

_colors = ["RED", "BLUE", "CYAN", "YELLOW", "GREEN", "MAGENTA", "WHITE", "BLACK"]
backgrounds = ["BG_RED", "BG_BLUE", "BG_CYAN", "BG_YELLOW", "BG_GREEN", "BG_MAGENTA", "BG_WHITE", "BG_BLACK"]
styles = ['BOLD', 'REVERSE', 'UNDERLINE', 'RESET', 'ITALIC', 'BLINK', 'INVISIBLE', "RED_UNDERLINE",
          "GREEN_UNDERLINE", 'DOUBLE_UNDERLINE', 'STRIKE', 'RED_UNDERLINE', 'GREEN_UNDERLINE', 'INVISIBLE']
if sys.platform == "win32":
    path = __file__
    if not os.path.exists(path.replace(
            "colors.py", "completed")):
        print("Registering Colors In Windows Registry......")
        cmd = os.popen(r'reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 0x00000001 '
                       '/f').read()
        assert cmd.rstrip() == "The operation completed successfully.", "Run As Administrator"
        with open(path.replace("colors.py", "completed"), "x") as file: ...
        print("Successfully Registered Colors In Windows Registry")
colors = {
    'RED': "\033[1;31m", 'BLUE': "\033[1;34m", 'CYAN': "\033[1;36m", 'YELLOW': "\u001b[33m", 'GREEN': "\033[0;32m",
    'MAGENTA': "\u001b[35m", 'WHITE': "\u001b[37m", 'BLACK': "\u001b[30m", 'BG_BLACK': "\u001b[40m",
    'BG_RED': "\u001b[41m", 'BG_GREEN': "\u001b[42m", 'BG_YELLOW': "\u001b[43m", 'BG_BLUE': "\u001b[44m",
    'BG_MAGENTA': "\u001b[45m", 'BG_CYAN': "\u001b[46m", 'BG_WHITE': "\u001b[47m", 'RESET': "\033[0;0m",
    'BOLD': "\033[;1m", 'REVERSE': "\033[7m", 'UNDERLINE': "\u001b[4m", 'ITALIC': "\u001b[3m", 'BLINK': "\033[5m",
    'INVISIBLE': "\033[8m", 'RED_UNDERLINE': "\u001b[4m\u001b[31m", 'GREEN_UNDERLINE': "\u001b[4m\u001b[32m",
    'STRIKE': "\u001b[9m", "CURLY_UNDERLINE": '\u001b[4:3m'}


def is_string(string):
    """
    :param string: string to check weather it is a string
    :raise ValueError if string is not a string
    """
    if not isinstance(string, str):
        raise ValueError("Please Enter A String Not %s" % str(type(string))[8:].replace("'>", ""))


def color(string, fg=None, bg=None, style=None):
    """
    :param string: String
    :param fg: ForeGround Color
    :param bg: BackGround Color
    :param style: Style To use
    :return: string Formatted with fg, bg and style
    """
    is_string(string)
    if fg is not None:
        if fg.upper() not in _colors:
            raise ValueError("%s Not Available" % fg)
        string = colors[fg.upper()] + string
    if bg is not None:
        if "BG_" + bg.upper() not in backgrounds:
            raise ValueError("%s Not Available" % bg)
        string = colors["BG_" + bg.upper()] + string
    if style is not None:
        if style.upper() not in styles:
            raise ValueError("%s Style Not Available" % style)
        string = colors[style.upper()] + string
    string += reset
    return string


# Shortcut For Foreground Colors
blue = colors['BLUE']
green = colors['GREEN']
yellow = colors["YELLOW"]
white = colors["WHITE"]
cyan = colors["CYAN"]
magenta = colors["MAGENTA"]
red = colors["RED"]
black = colors["BLACK"]
# Shortcut For Background Colors
bg_black = colors["BG_BLACK"]
bg_red = colors["BG_RED"]
bg_blue = colors["BG_BLUE"]
bg_cyan = colors["BG_CYAN"]
bg_white = colors["BG_WHITE"]
bg_green = colors["BG_GREEN"]
bg_magenta = colors["BG_MAGENTA"]
bg_yellow = colors["BG_YELLOW"]
# Shortcut For Styles
bold = colors["BOLD"]
italic = colors["ITALIC"]
reverse = colors['REVERSE']
underline = colors['UNDERLINE']
red_underline = colors['RED_UNDERLINE']
green_underline = colors['GREEN_UNDERLINE']
invisible = colors['INVISIBLE']
blink = colors['BLINK']
strike = colors['STRIKE']
curly_underline = colors["CURLY_UNDERLINE"]
reset = colors["RESET"]


def print_all_colors():
    for k, v in colors.items():
        print(v, k, reset)
