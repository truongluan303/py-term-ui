from typing import Optional

__all__ = ["colorify"]


def colorify(
    string: str,
    foreground: Optional[str] = None,
    background: Optional[str] = None,
    effect: Optional[str] = None,
) -> str:
    return (
        TermStyles.PREFIX
        + ";".join(
            filter(
                None,
                [
                    TermStyles.BG.get(background),
                    TermStyles.FG.get(foreground),
                    TermStyles.EFFECTS.get(effect),
                ],
            )
        )
        + "m"
        + string
        + TermStyles.RESET
    )


class TermStyles:
    EFFECTS = {
        "bold": "01",
        "disable": "02",
        "underline": "04",
        "reverse": "07",
        "strikethrough": "09",
        "invisible": "08",
    }

    FG = {
        "black": "30",
        "red": "31",
        "green": "32",
        "orange": "33",
        "blue": "34",
        "purple": "35",
        "cyan": "36",
        "lightgrey": "37",
        "darkgrey": "90",
        "lightred": "91",
        "lightgreen": "92",
        "yellow": "93",
        "lightblue": "94",
        "pink": "95",
        "lightcyan": "96",
    }

    BG = {
        "black": "40",
        "red": "41",
        "green": "42",
        "orange": "43",
        "blue": "44",
        "purple": "45",
        "cyan": "46",
        "lightgrey": "47m",
    }

    RESET = "\033[0m"
    PREFIX = "\033["
