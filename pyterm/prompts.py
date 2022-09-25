from typing import Optional

from pyterm.color import colorify


def prompt_yes_no(message: str, is_yes_default: bool = True) -> Optional[bool]:
    y = "Y" if is_yes_default else "y"
    n = "n" if is_yes_default else "N"
    ans = input(f"{message} [{colorify(y, 'green')}/{colorify(n, 'yellow')}]").lower()

    if ans in ("y", "yes"):
        return True
    elif ans in ("n", "no"):
        return False
    return None
