from colorama import Fore, Back, init
from datetime import datetime
import shutil
import time
import os

def clear(): os.system("cls")

init(convert=True)

class cf(): #colorama fore
    w = Fore.LIGHTWHITE_EX  # Light white
    b = Fore.LIGHTBLUE_EX   # Light blue
    y = Fore.LIGHTYELLOW_EX # Light yellow
    g = Fore.LIGHTGREEN_EX  # Light green
    r = Fore.LIGHTRED_EX    # Light red
    bl = Fore.LIGHTBLACK_EX # Light black
    re = Fore.RESET

class cb(): #colorama back
    w = Back.LIGHTWHITE_EX  # Light white
    b = Back.LIGHTBLUE_EX   # Light blue
    y = Back.LIGHTYELLOW_EX # Light yellow
    g = Back.LIGHTGREEN_EX  # Light green
    r = Back.LIGHTRED_EX    # Light red
    bl = Back.LIGHTBLACK_EX # Light black
    re = Back.RESET

arrow = f"{cf.b}>>{cf.re}"

def log(text, status: int):
    t = datetime.now().strftime('%H:%M')
    status_map = {
        0: (cb.g, '+'), # Success
        1: (cb.r, '-'), # Failure
        2: (cb.y, '!'), #  Error
        3: (cb.b, '#')  #  Debug  (info)
    }
    color, symbol = status_map.get(status, (cb.re, '?'))
    print(f'{cf.bl} {t} {cf.re}{color} {symbol} {cb.re} {text}')

def ask(text):
    t = datetime.now().strftime('%H:%M')
    x = input(f'{cf.bl} {t} {cf.re}{cb.b} ? {cb.re} {text} {arrow} ')
    return x

def bar(text, seconds, _finally = None): #/// print a progress bar

    t = datetime.now().strftime('%H:%M')

    if not _finally: _finally=text
    seconds = float(seconds)

    bar_size = 30
    step_duration = seconds / bar_size

    for i in range(bar_size+1):
        bar = f'{cf.b}━{cf.re}' * i + f'{cf.bl}━{cf.re}' * (bar_size - i)
        time_left = int(seconds - i * step_duration)

        print(f"\r{cf.bl} {t} {cf.re}{cb.b} # {cb.re} {bar} {time_left} │ {text}", end="")
        time.sleep(step_duration)
    
    print(f"\r{cf.bl} {t} {cf.re}{cb.b} # {cb.re} {bar} 0 │ {_finally}                              ")

def table(title: str = "Table", rows: list = [], centered: bool = False, color = cf.w): 
    # Calculate the maximum row length and table width
    max_row_length = max((len(row) for row in rows), default=0)
    table_width = max(max_row_length, len(title)) + 2

    # Define table borders
    BORDER = f"{color}┌{'─' * table_width}┐{cf.re}"
    SEPARATOR = f"{color}├{'─' * table_width}┤{cf.re}"
    BOTTOM = f"└{'─' * table_width}┘"

    # Calculate console width
    console_width = shutil.get_terminal_size((80, 20)).columns

    # Calculate padding for centering
    padding = (console_width - table_width) // 2 if centered else 0
    padding_space = ' ' * padding

    # Print the table with optional centering
    print(padding_space + BORDER)
    print(padding_space + f"{color}│{cf.re} {title.center(table_width - 2)} {color}│{cf.re}")
    print(padding_space + SEPARATOR)

    for row in rows:
        print(padding_space + f"│ {row:<{table_width - 2}} │")

    print(padding_space + BOTTOM)

def box(text: list = ["Box"], centered: bool = False, color = cf.w):
    max_text_lenght = max((len(txt) for txt in text), default=0) + 2

    BORDER = f"{color}┌{'─' * max_text_lenght}┐"
    BOTTOM = f"└{'─' * max_text_lenght}┘{cf.re}"

    console_width = shutil.get_terminal_size((80, 20)).columns

    padding = (console_width - max_text_lenght) // 2 if centered else 0
    padding_space = ' ' * padding

    print(padding_space + BORDER)
    
    for txt in text:
        print(padding_space + f"│{cf.re} {txt:<{max_text_lenght - 2}} {color}│")

    print(padding_space + BOTTOM)

def pause():
    ask("Press enter to continue")