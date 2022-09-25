from typing import Optional

from PIL import Image as PILImg

_ASCII_CHARS = ["@", "$", "#", "%", "?", "x", "+", ";", ":", ",", "."]


class AsciiImage:
    def __init__(self, img_path: str, width: Optional[int] = None) -> None:
        """
        Args:
            img_path (str): Path to the image.
            width (Optional[int]): The width to resize the given image to.
        """
        self._img = PILImg.open(img_path)
        self._width = width if width is not None else self._img.size[0]

        self._resize_image()
        self._to_black_and_white()
        self._to_ascii()

    def print(self) -> None:
        print(self._ascii_img)

    def _resize_image(self) -> None:
        """
        Resize the image based on the new scale.
        """
        original_width, original_height = self._img.size
        scale = self._width / original_width
        self._img = self._img.resize(
            (round(self._width), round(original_height * scale * 0.5))
        )

    def _to_black_and_white(self) -> None:
        self._img = self._img.convert("L")

    def _to_ascii(self) -> None:
        pixels = self._img.getdata()
        ascii_pixels = list(_ASCII_CHARS[pixel // 25] for pixel in pixels)

        self._ascii_img = "\n".join(
            "".join(ascii_pixels[i : i + self._width])
            for i in range(0, len(ascii_pixels), self._width)
        )

    def __str__(self) -> str:
        return self._ascii_img
