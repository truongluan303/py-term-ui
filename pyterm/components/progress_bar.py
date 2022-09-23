from dataclasses import dataclass


@dataclass
class ProgressBar:
    max_val: float
    title: str = "Progress"
    bar_length: int = 30
    filled_cell: str = "█"
    empty_cell: str = "-"

    def __post_init__(self) -> None:
        self._current_val = -1
        self.increment()

    def increment(self, val: float = 1) -> None:
        """
        Increase the progress.

        Args:
            `val`: How much more progress has been made. Defaults to 1.
        """
        if self.is_done:
            return

        self._current_val += val
        self._current_val = min(self._current_val, self.max_val)

        filled_len = int(self.bar_length * self._current_val // self.max_val)
        empty_len = self.bar_length - filled_len

        bar = self.filled_cell * filled_len + self.empty_cell * empty_len
        percent = round(100.0 * self._current_val / self.max_val, 1)
        
        print(
            f"\r{self.title} |{bar}| {percent}%",
            end="\r" if not self.is_done else " ✅\n",
        )

    @property
    def is_done(self) -> bool:
        return self._current_val >= self.max_val
